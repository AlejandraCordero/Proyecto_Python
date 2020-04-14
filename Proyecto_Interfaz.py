# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 23:33:36 2020

@author: Alejandra
"""

import tkinter as tk
root=tk.Tk()
mensaje1 =tk.StringVar()
mensaje2 =tk.StringVar()
mensaje3 =tk.StringVar()
mensaje4 =tk.StringVar()
#variables
a=tk.StringVar()
b=tk.StringVar()


#funciones
def suma():
    a1=int(a.get())
    b1=int(b.get())
    r=a1+b1
    mensaje1.set(str(r))
def resta():
    a1=int(a.get())
    b1=int(b.get())
    r2=a1-b1
    mensaje2.set(str(r2))
def mult():
    a1=int(a.get())
    b1=int(b.get())
    r3=a1*b1
    mensaje3.set(str(r3))
def divi():
    a1=int(a.get())
    b1=int(b.get())
    r4=a1/b1
    mensaje4.set(str(r4))

def borrar():
    a.set('')
    b.set('')
    mensaje1.set('')
    mensaje2.set('')
    mensaje3.set('')
    mensaje4.set('')


root.geometry('500x600')
root.title('Calculadora')
root.configure(bg='#FCFE6E')
#titulo
tk.Label(root, text='PROYECTO - CALCULADORA',bg='#F7C31F',fg='black',font=('',20)).place(x=55,y=20)
         

#1er número
tk.Label(root, text='Ingrese el 1er número:', bg='#F5C358', fg='black', font=('', 15)).place(x=30, y=100)
tk.Entry(root, justify='center', textvariable=a).place(x=300, y=105)
#tk.Button(root, text='Buscar', bd=0, command=a).place(x=250, y=600)

#2do número
tk.Label(root, text='Ingrese el 2do número:', bg='#F5C358', fg='black', font=('', 15)).place(x=30, y=150)
tk.Entry(root, justify='center', textvariable=b).place(x=300, y=155)

#funciones
tk.Button(root, text='SUMA:', bd=0, command=suma).place(x=180, y=220)
tk.Label(root, textvariable=mensaje1, bg='#F5C358', fg='black', font=('', 15)).place(x=240, y=220)

tk.Button(root, text='RESTA:', bd=0, command=resta).place(x=180, y=260)
tk.Label(root, textvariable=mensaje2, bg='#F5C358', fg='black', font=('', 15)).place(x=240, y=260)

tk.Button(root, text='MULTIPLICACIÓN:', bd=0, command=mult).place(x=120, y=300)
tk.Label(root, textvariable=mensaje3, bg='#F5C358', fg='black', font=('', 15)).place(x=240, y=300)

tk.Button(root, text='DIVISIÓN:', bd=0, command=divi).place(x=170, y=340)
tk.Label(root, textvariable=mensaje4, bg='#F5C358', fg='black', font=('', 15)).place(x=240, y=340)

#borrar
tk.Button(root, text='BORRAR', bd=0, command=borrar).place(x=230, y=450)

#salir
tk.Button(root,text="SALIR", bd=0,command=root.destroy).place(x=240,y=500)
root.mainloop()

