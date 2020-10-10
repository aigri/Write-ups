# easylogin

![](img/easylogin.png)

Pour ce challenge on ne nous fournit qu'un executable, voyons voir un peu à quoi il ressemble

```
❯ file easylogin
easylogin: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=a2b0f7dcfdd3cf18ed4d334a67e40bb107483de2, for GNU/Linux 3.2.0, not stripped
❯ ./easylogin
login ?
saymant
password ?
bg
Bad login: saymant
```

D'accord un simple système de login avec un username et un password, regardons un peu au niveau du code desassemblé maintenant

```
pwndbg> disass main
Dump of assembler code for function main:
   0x080491d6 <+0>:	lea    ecx,[esp+0x4]
   0x080491da <+4>:	and    esp,0xfffffff0
   0x080491dd <+7>:	push   DWORD PTR [ecx-0x4]
   0x080491e0 <+10>:	push   ebp
   0x080491e1 <+11>:	mov    ebp,esp
   0x080491e3 <+13>:	push   ebx
   0x080491e4 <+14>:	push   ecx
   0x080491e5 <+15>:	sub    esp,0x70
   0x080491e8 <+18>:	call   0x8049110 <__x86.get_pc_thunk.bx>
   0x080491ed <+23>:	add    ebx,0x2e13
   0x080491f3 <+29>:	mov    eax,ecx
   0x080491f5 <+31>:	mov    eax,DWORD PTR [eax+0x4]
   0x080491f8 <+34>:	mov    DWORD PTR [ebp-0x6c],eax
   0x080491fb <+37>:	mov    eax,gs:0x14
   0x08049201 <+43>:	mov    DWORD PTR [ebp-0xc],eax
   0x08049204 <+46>:	xor    eax,eax
   0x08049206 <+48>:	mov    DWORD PTR [ebp-0x43],0x73776e4b
   0x0804920d <+55>:	mov    DWORD PTR [ebp-0x3f],0x7e7d7378
   0x08049214 <+62>:	mov    DWORD PTR [ebp-0x3b],0x6f7e6b7c
   0x0804921b <+69>:	mov    WORD PTR [ebp-0x37],0x7c7f
   0x08049221 <+75>:	mov    BYTE PTR [ebp-0x35],0x0
   0x08049225 <+79>:	mov    DWORD PTR [ebp-0x51],0x45483e62
   0x0804922c <+86>:	mov    DWORD PTR [ebp-0x4d],0x41444258
   0x08049233 <+93>:	mov    DWORD PTR [ebp-0x49],0x4f444f50
   0x0804923a <+100>:	mov    WORD PTR [ebp-0x45],0x4e
   0x08049240 <+106>:	sub    esp,0xc
   0x08049243 <+109>:	lea    eax,[ebx-0x1ff8]
   0x08049249 <+115>:	push   eax
   0x0804924a <+116>:	call   0x8049080 <puts@plt>
   0x0804924f <+121>:	add    esp,0x10
   0x08049252 <+124>:	mov    eax,DWORD PTR [ebx-0x8]
   0x08049258 <+130>:	mov    eax,DWORD PTR [eax]
   0x0804925a <+132>:	sub    esp,0x4
   0x0804925d <+135>:	push   eax
   0x0804925e <+136>:	push   0x14
   0x08049260 <+138>:	lea    eax,[ebp-0x34]
   0x08049263 <+141>:	push   eax
   0x08049264 <+142>:	call   0x8049060 <fgets@plt>
   0x08049269 <+147>:	add    esp,0x10
   0x0804926c <+150>:	sub    esp,0x8
   0x0804926f <+153>:	push   0xa
   0x08049271 <+155>:	lea    eax,[ebp-0x34]
   0x08049274 <+158>:	push   eax
   0x08049275 <+159>:	call   0x8049090 <strchr@plt>
   0x0804927a <+164>:	add    esp,0x10
   0x0804927d <+167>:	mov    DWORD PTR [ebp-0x5c],eax
   0x08049280 <+170>:	cmp    DWORD PTR [ebp-0x5c],0x0
   0x08049284 <+174>:	je     0x804928c <main+182>
   0x08049286 <+176>:	mov    eax,DWORD PTR [ebp-0x5c]
   0x08049289 <+179>:	mov    BYTE PTR [eax],0x0
   0x0804928c <+182>:	sub    esp,0xc
   0x0804928f <+185>:	lea    eax,[ebx-0x1ff0]
   0x08049295 <+191>:	push   eax
   0x08049296 <+192>:	call   0x8049080 <puts@plt>
   0x0804929b <+197>:	add    esp,0x10
   0x0804929e <+200>:	mov    eax,DWORD PTR [ebx-0x8]
   0x080492a4 <+206>:	mov    eax,DWORD PTR [eax]
   0x080492a6 <+208>:	sub    esp,0x4
   0x080492a9 <+211>:	push   eax
   0x080492aa <+212>:	push   0x14
   0x080492ac <+214>:	lea    eax,[ebp-0x20]
   0x080492af <+217>:	push   eax
   0x080492b0 <+218>:	call   0x8049060 <fgets@plt>
   0x080492b5 <+223>:	add    esp,0x10
   0x080492b8 <+226>:	sub    esp,0x8
   0x080492bb <+229>:	push   0xa
   0x080492bd <+231>:	lea    eax,[ebp-0x20]
   0x080492c0 <+234>:	push   eax
   0x080492c1 <+235>:	call   0x8049090 <strchr@plt>
   0x080492c6 <+240>:	add    esp,0x10
   0x080492c9 <+243>:	mov    DWORD PTR [ebp-0x5c],eax
   0x080492cc <+246>:	cmp    DWORD PTR [ebp-0x5c],0x0
   0x080492d0 <+250>:	je     0x80492d8 <main+258>
   0x080492d2 <+252>:	mov    eax,DWORD PTR [ebp-0x5c]
   0x080492d5 <+255>:	mov    BYTE PTR [eax],0x0
   0x080492d8 <+258>:	sub    esp,0xc
   0x080492db <+261>:	lea    eax,[ebp-0x43]
   0x080492de <+264>:	push   eax
   0x080492df <+265>:	call   0x80490a0 <strlen@plt>
   0x080492e4 <+270>:	add    esp,0x10
   0x080492e7 <+273>:	mov    DWORD PTR [ebp-0x58],eax
   0x080492ea <+276>:	mov    DWORD PTR [ebp-0x64],0x0
   0x080492f1 <+283>:	jmp    0x8049311 <main+315>
   0x080492f3 <+285>:	lea    edx,[ebp-0x43]
   0x080492f6 <+288>:	mov    eax,DWORD PTR [ebp-0x64]
   0x080492f9 <+291>:	add    eax,edx
   0x080492fb <+293>:	movzx  eax,BYTE PTR [eax]
   0x080492fe <+296>:	sub    eax,0xa
   0x08049301 <+299>:	mov    ecx,eax
   0x08049303 <+301>:	lea    edx,[ebp-0x43]
   0x08049306 <+304>:	mov    eax,DWORD PTR [ebp-0x64]
   0x08049309 <+307>:	add    eax,edx
   0x0804930b <+309>:	mov    BYTE PTR [eax],cl
   0x0804930d <+311>:	add    DWORD PTR [ebp-0x64],0x1
   0x08049311 <+315>:	mov    eax,DWORD PTR [ebp-0x64]
   0x08049314 <+318>:	cmp    eax,DWORD PTR [ebp-0x58]
   0x08049317 <+321>:	jl     0x80492f3 <main+285>
   0x08049319 <+323>:	sub    esp,0x8
   0x0804931c <+326>:	lea    eax,[ebp-0x34]
   0x0804931f <+329>:	push   eax
   0x08049320 <+330>:	lea    eax,[ebp-0x43]
   0x08049323 <+333>:	push   eax
   0x08049324 <+334>:	call   0x8049040 <strcmp@plt>
   0x08049329 <+339>:	add    esp,0x10
   0x0804932c <+342>:	test   eax,eax
   0x0804932e <+344>:	je     0x8049350 <main+378>
   0x08049330 <+346>:	sub    esp,0x8
   0x08049333 <+349>:	lea    eax,[ebp-0x34]
   0x08049336 <+352>:	push   eax
   0x08049337 <+353>:	lea    eax,[ebx-0x1fe5]
   0x0804933d <+359>:	push   eax
   0x0804933e <+360>:	call   0x8049050 <printf@plt>
   0x08049343 <+365>:	add    esp,0x10
   0x08049346 <+368>:	mov    eax,0x0
   0x0804934b <+373>:	jmp    0x80493f1 <main+539>
   0x08049350 <+378>:	sub    esp,0xc
   0x08049353 <+381>:	lea    eax,[ebp-0x51]
   0x08049356 <+384>:	push   eax
   0x08049357 <+385>:	call   0x80490a0 <strlen@plt>
   0x0804935c <+390>:	add    esp,0x10
   0x0804935f <+393>:	mov    DWORD PTR [ebp-0x58],eax
   0x08049362 <+396>:	mov    DWORD PTR [ebp-0x60],0x0
   0x08049369 <+403>:	jmp    0x8049396 <main+448>
   0x0804936b <+405>:	lea    edx,[ebp-0x51]
   0x0804936e <+408>:	mov    eax,DWORD PTR [ebp-0x60]
   0x08049371 <+411>:	add    eax,edx
   0x08049373 <+413>:	movzx  eax,BYTE PTR [eax]
   0x08049376 <+416>:	sub    eax,0x3d
   0x08049379 <+419>:	mov    ecx,eax
   0x0804937b <+421>:	lea    edx,[ebp-0x43]
   0x0804937e <+424>:	mov    eax,DWORD PTR [ebp-0x60]
   0x08049381 <+427>:	add    eax,edx
   0x08049383 <+429>:	movzx  eax,BYTE PTR [eax]
   0x08049386 <+432>:	xor    ecx,eax
   0x08049388 <+434>:	lea    edx,[ebp-0x51]
   0x0804938b <+437>:	mov    eax,DWORD PTR [ebp-0x60]
   0x0804938e <+440>:	add    eax,edx
   0x08049390 <+442>:	mov    BYTE PTR [eax],cl
   0x08049392 <+444>:	add    DWORD PTR [ebp-0x60],0x1
   0x08049396 <+448>:	mov    eax,DWORD PTR [ebp-0x60]
   0x08049399 <+451>:	cmp    eax,DWORD PTR [ebp-0x58]
   0x0804939c <+454>:	jl     0x804936b <main+405>
   0x0804939e <+456>:	sub    esp,0x8
   0x080493a1 <+459>:	lea    eax,[ebp-0x20]
   0x080493a4 <+462>:	push   eax
   0x080493a5 <+463>:	lea    eax,[ebp-0x51]
   0x080493a8 <+466>:	push   eax
   0x080493a9 <+467>:	call   0x8049040 <strcmp@plt>
   0x080493ae <+472>:	add    esp,0x10
   0x080493b1 <+475>:	test   eax,eax
   0x080493b3 <+477>:	je     0x80493d2 <main+508>
   0x080493b5 <+479>:	sub    esp,0x8
   0x080493b8 <+482>:	lea    eax,[ebp-0x20]
   0x080493bb <+485>:	push   eax
   0x080493bc <+486>:	lea    eax,[ebx-0x1fd6]
   0x080493c2 <+492>:	push   eax
   0x080493c3 <+493>:	call   0x8049050 <printf@plt>
   0x080493c8 <+498>:	add    esp,0x10
   0x080493cb <+501>:	mov    eax,0x0
   0x080493d0 <+506>:	jmp    0x80493f1 <main+539>
   0x080493d2 <+508>:	sub    esp,0x4
   0x080493d5 <+511>:	lea    eax,[ebp-0x20]
   0x080493d8 <+514>:	push   eax
   0x080493d9 <+515>:	lea    eax,[ebp-0x34]
   0x080493dc <+518>:	push   eax
   0x080493dd <+519>:	lea    eax,[ebx-0x1fc4]
   0x080493e3 <+525>:	push   eax
   0x080493e4 <+526>:	call   0x8049050 <printf@plt>
   0x080493e9 <+531>:	add    esp,0x10
   0x080493ec <+534>:	mov    eax,0x0
   0x080493f1 <+539>:	mov    ecx,DWORD PTR [ebp-0xc]
   0x080493f4 <+542>:	xor    ecx,DWORD PTR gs:0x14
   0x080493fb <+549>:	je     0x8049402 <main+556>
   0x080493fd <+551>:	call   0x8049490 <__stack_chk_fail_local>
   0x08049402 <+556>:	lea    esp,[ebp-0x8]
   0x08049405 <+559>:	pop    ecx
   0x08049406 <+560>:	pop    ebx
   0x08049407 <+561>:	pop    ebp
   0x08049408 <+562>:	lea    esp,[ecx-0x4]
   0x0804940b <+565>:	ret    
End of assembler dump.
```

Hmmm assez long pour pas grand chose tout de même ... 
<br>
On voit un call à strcmp dans la plt à <main+334> et à <main+467>, essayons de placer un breakpoint sur ces instructions et regardons ce qu'il se passe.

```
pwndbg> b *main+334
Breakpoint 1 at 0x8049324
pwndbg> b *main+467
Breakpoint 2 at 0x80493a9
pwndbg> r
Starting program: /home/saymant/Bureau/Bureau/Info/CTF/HackademINT/Reverse/Easy Login/easylogin 
login ?
saymant 
password ?
bg

...

 ► 0x8049324 <main+334>    call   strcmp@plt <0x8049040>
        s1: 0xffffcf85 ◂— 'Administrateur'
        s2: 0xffffcf94 ◂— 'saymant
```
Puis le programme finit par s'arrêter sans passer par le deuxième call à strcmp, ce qui veut dire que celui-ci va d'abord vérifier le username puis si il est correct, le password.


Mais vu la tête de la stack lors du strcmp ne me dites pas que ...

```
pwndbg> r
Starting program: /home/saymant/Bureau/Bureau/Info/CTF/HackademINT/Reverse/Easy Login/easylogin 
login ?
Administrateur
password ?
bg

...

 ► 0x8049324 <main+334>    call   strcmp@plt <0x8049040>
        s1: 0xffffcf85 ◂— 'Administrateur'
        s2: 0xffffcf94 ◂— 'Administrateur'

...

 ► 0x80493a9 <main+467>    call   strcmp@plt <0x8049040>
        s1: 0xffffcf77 ◂— 'defaultpasswd'
        s2: 0xffffcfa8 ◂— 0x6762 /* 'bg' */
```

Bon, c'est bien ce que je pensais ... notre argument va juste être comparé avec la bonne valeur qui ici est placée sur la stack. Donc ici on peut voir que le bon username est `Administrateur` et le bon password est `defaultpasswd`.<br>
Bien ressayons tout ça avec les bonnes informations
```
pwndbg> r
Starting program: /home/saymant/Bureau/Bureau/Info/CTF/HackademINT/Reverse/Easy Login/easylogin 
login ?
Administrateur
password ?
defaultpasswd

...

 ► 0x8049324 <main+334>    call   strcmp@plt <0x8049040>
        s1: 0xffffcf85 ◂— 'Administrateur'
        s2: 0xffffcf94 ◂— 'Administrateur'

...

 ► 0x80493a9 <main+467>    call   strcmp@plt <0x8049040>
        s1: 0xffffcf77 ◂— 'defaultpasswd'
        s2: 0xffffcfa8 ◂— 'defaultpasswd'

...

Welcome back! HackademINT{Administrateur:defaultpasswd}
```
Ok noice !
