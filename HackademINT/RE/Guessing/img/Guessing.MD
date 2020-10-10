# Guessing

![](img/Guessing.png)

Pour ce challenge on ne nous donne également qu'un executable, essayons de l'executer pour voir ce qu'il se passe

```
Can you guess the next number (0-99)?
>> 15
Naaaah ... Better luck next time!
```

Hmm d'accord, essayons de ltrace pour voir ce qu'il se passe

```
❯ ltrace ./guessing
__libc_start_main(0x80491d6, 1, 0xff8d3d64, 0x80493a0 <unfinished ...>
srand(0, 1, 0xf7f55940, 0x80491ed)                                           = 0
puts("Can you guess the next number (0"...Can you guess the next number (0-99)?
)                                  = 38
printf(">> ")                                                                = 3
fgets(>> 15
"15\n", 20, 0xf7f055c0)                                                = 0xff8d3c7e
strtol(0xff8d3c7e, 0, 10, 0x80491ed)                                         = 15
rand(0, 0xc10000, 0, 0xff8d3d64)                                             = 0x6b8b4567
puts("Naaaah ... Better luck next time"...Naaaah ... Better luck next time!
)                                  = 34
+++ exited (status 0) +++
```
Ok donc ici il y a un fgets pour qui nous demande un nombre, ensuite la string que nous avons rentré va être castée en int avec la fonction `strtol()`, puis la fonction `rand()` va être appelée elle aussi et on suppose que sa valeur de retour va être comparée avec notre nombre.

Et si on regardait maintenant un peu au niveau du pseudocode

```C
undefined4 main(undefined4 param_1,undefined4 param_2)
{
  long lVar1;
  int iVar2;
  undefined4 uVar3;
  int in_GS_OFFSET;
  int local_58;
  int local_54;
  byte local_48 [5];
  undefined local_43;
  char local_42 [20];
  undefined4 local_2e;
  undefined4 local_2a;
  undefined4 local_26;
  undefined4 local_22;
  undefined4 local_1e;
  undefined4 local_1a;
  undefined2 local_16;
  int local_14;
  undefined *local_10;
  
  local_10 = &param_1;
  local_14 = *(int *)(in_GS_OFFSET + 0x14);
  local_2e = 0xb030128;
  local_2a = 0x2fafb01;
  local_26 = 0x522251e;
  local_22 = 0xfc42fc1e;
  local_1e = 0xebef131e;
  local_1a = 0x29e929d9;
  local_16 = 0xf1;
  srand(0);
  local_58 = 0;
  do {
    if (4 < local_58) {
LAB_0804937f:
      uVar3 = 0;
      if (local_14 != *(int *)(in_GS_OFFSET + 0x14)) {
        uVar3 = __stack_chk_fail_local();
      }
      return uVar3;
    }
    puts("Can you guess the next number (0-99)?");
    printf(">> ");
    fgets(local_42,0x14,stdin);
    lVar1 = strtol(local_42,(char **)0x0,10);
    iVar2 = rand();
    if (lVar1 != iVar2 % 100) {
      puts("Naaaah ... Better luck next time!");
      goto LAB_0804937f;
    }
    local_54 = 0;
    while (local_54 < 5) {
      local_48[local_54] =
           *(char *)((int)&local_2e + local_54 + local_58 * 5) + (char)local_58 * '\n' ^
           (char)local_58 + 0x60U;
      local_54 = local_54 + 1;
    }
    local_43 = 0;
    printf("Wow, you did it!\nHere is your reward: %s\n",local_48);
    local_58 = local_58 + 1;
  } while( true );
}
```

Ah voilà, ici on peut déjà y voir plus clair au niveau de notre comparaison ! <br>
Donc en gros il y a une condition qui va vérifier si notre input est égal au nombre aléatoire genéré par la fonction `rand()` modulo de 100 (cette opération ne sert en réalité à rien vu que les nombres sont compris entre de 0 à 99) dans quel cas il affiche normalement le flag. Dans le cas contraire, nous avons un message qui nous indique que nous n'avons pas réussi et le programme exit.


En se renseignant un peu sur la fonction `rand()` on s'apercoit que `srand()` est tout simplement la fonction appellée avant tout appel à `rand()` qui va permettre d'initialiser le générateur de nombres pseudoaléatoires avec une graine différente, et qu'ici cette graine est mise à 0. Ce qui voudrait dire les nombres vont être genérés aléatoirement mais l'aléatoire ne changera pas, les nombres générés seront toujours les mêmes, dans le même ordre.<br>
Super ! Ca rend tout de suite la situation moins compliquée. Il nous suffit alors de tester chaque nombre compris entre 0 et 100 (dit explicitement dans le message du programme juste avant de rentrer notre nombre) jusqu'à tomber sur le bon.
<br>
J'ai alors fait ce script 

```py
import os

a = 0

for i in range(100):
	print(a)
    os.system('(echo "' + str(a) + '\") | ./guessing')
	a += 1
```

```
❯ python solver.py

...

83
Can you guess the next number (0-99)?
>> Wow, you did it!
Here is your reward: Hacka
Can you guess the next number (0-99)?
>> Naaaah ... Better luck next time!
```

Hmmm ... On dirait qu'on a juste une partie du flag (car format de flag : Hackademint{flag}) et qu'il nous demande un autre nombre après, essayons alors de déterminer celui-ci aussi vu que maintenant nous savons que le premier nombre à rentrer est 83

```py
import os

a = 0

for i in range(100):
	print(a)
	os.system('(echo "83"; echo "' + str(a) + '\") | ./guessing')
	a += 1
```

```
❯ python solver.py

...

Here is your reward: Hacka
Can you guess the next number (0-99)?
>> Wow, you did it!
Here is your reward: demIN
Can you guess the next number (0-99)?
>> Naaaah ... Better luck next time!
```

Bon ... On doit faire la manipulation encore quelques fois on dirait, 1 nombre trouvé = 4 charactères du flag trouvés. C'est la même manipulation jusque la fin donc je vais vous épargner toutes les étapes et directement vous balancer le script final

```py
import os

a = 0

for i in range(100):
	os.system('(echo "83"; echo "86"; echo "77"; echo "15";  echo "93"; echo "' + str(a) + '\") | ./guessing')
	print(a)
	a += 1
```
Ce qui au final nous donne

```
❯ python solver.py

...

Can you guess the next number (0-99)?
>> Wow, you did it!
Here is your reward: Hacka
Can you guess the next number (0-99)?
>> Wow, you did it!
Here is your reward: demIN
Can you guess the next number (0-99)?
>> Wow, you did it!
Here is your reward: T{Pr4
Can you guess the next number (0-99)?
>> Wow, you did it!
Here is your reward: y_Rnj
Can you guess the next number (0-99)?
>> Wow, you did it!
Here is your reward: e5u5}
```

Si on reconstitues chaque bout de flag, on obtient bien ``HackademINT{Pr4y_Rnje5u5}``

Carré !