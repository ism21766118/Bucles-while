#coding: utf-8
#coding: utf8
x=input("Introduzca un numero:")
cont = 0
suma = 0
while (cont < x):
    aux = input("indique otro numero:")
    if (aux > 0):
            cont += 1
            suma = suma + aux
if suma > 12:
    print "Has superado el limite"
else:
    print "Correcto"

