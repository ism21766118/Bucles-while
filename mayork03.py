#coding: utf-8
num1=input("escriba un numero:")
num2=input("escriba un numero mayor que"+" "+str(num1)+":")
while (num1<num2):
 num1=num2
 num2=input("escriba un numero mayor que"+" "+str(num1)+":")
print "el numero"+" "+str(num2),"no es mayor que"+" "+str(num1), ",programa terminado."
