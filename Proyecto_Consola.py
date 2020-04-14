# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 00:13:28 2020

@author: Alejandra
"""

print('****CALCULADORA***')
menu='''
===========MENU===========
1. Suma (+)
2. Resta (-)
3. Multiplicación (*)
4. División (/)
5. Salir
'''
a=int(input('Ingrese el 1er número: '))
b=int(input('Ingrese el 2do número: '))
sw=True
while sw:
    print(menu)
    op=int(input('--->Elija una opción: '))
    if op is 1:
        print ('Suma: ',a+b)
    elif op is 2:
        print ('Resta: ',a-b)
    elif op is 3:
        print ('Multiplicación: ',a*b)
    elif op is 4:
        print ('División: ',a/b)
    elif op is 5:
        sw=False
    else:
        print('Opción no disponible :(')
        break;