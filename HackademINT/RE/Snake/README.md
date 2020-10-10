# snake

![](img/Snake.png)

Donc pour ce challenge on nous fournissait un fichier se nommant `snake.pyc` l'extension nous dit donc que c'est un code python compilé j'ai alors utilisé `uncompyle6` pour décompiler ce code afin d'avoir le code python de base

```
❯ uncompyle6 snake.pyc
```
Ce qui nous renvoit 
```py
# uncompyle6 version 3.7.3
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
# [GCC 8.4.0]
# Embedded file name: snake.py
# Compiled at: 2020-09-15 15:08:03
x = raw_input('Oh no, a python! How to escape?\n')
key = [72, 97, 99, 107, 97, 100, 101, 109, 73, 78, 84, 123, 100, 51, 67, 111, 109, 112, 49, 108, 51, 95, 49, 55, 33, 33, 33, 125]
if len(x) != len(key):
    print 'My anaconda :(, NO!'
    exit()
for _ in range(28):
    if ord(x[_]) != key[_]:
        print 'My anaconda :(, NO!'
        exit()

print 'Nope, just Chuck Testa. You won'
# okay decompiling snake.pyc
```

D'accord donc là nous avons un tableau de bytecode nommé `key`.<br>
Le script va alors d'abord check si notre input fait la même taille que ce tableau dans quel cas il call la fonction exit(), il va ensuite check si chaque charactère de notre input casté en entier grâce à la foncton `ord` est égal à la valeur du tableau qui correspond, dans quel cas nous aurions le flag.<br><br>
Si nous réflechissons bien dans ce cas, il nous suffirait alors de convertir chaque valeur du tableau en un charactère (ce que fait la fonction `chr()`) pour que quand la string finale soit transformée en entier, celle-ci soit égale à la variable `key`

J'ai donc pour ça écrit un petit script qui fait la manipulation dite précédemment

```py
key = [72, 97, 99, 107, 97, 100, 101, 109, 73, 78, 84, 123, 100, 51, 67, 111, 109, 112, 49, 108, 51, 95, 49, 55, 33, 33, 33, 125]

flag = ""

for i in range(28):
	flag += chr(key[i])

print(flag)
```
Ce qui nous retourne ``HackademINT{d3Comp1l3_17!!!}``
