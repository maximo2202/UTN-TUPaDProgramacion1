#numero de 0 a 100
for i in range(101):
    print(i)
#___________________
#cantidad de digitos
n: int=int(input("ingrese cualquier numero entero "))
c = 0
x = abs(n)
if n==0:
    c=1
else:
    while x > 0:
        x = x//10
        c+=1
print(f"{n} tiene {c} digitos")
#___________________
#suma entre dos valores excluidos
n1: int=int(input("ingrese el primer numero "))
n2: int=int(input("ingrese el segundo numero "))
x=0
if n2<n1:
    n1,n2 = n2,n1
for i in range(n1+1,n2):
    x+=i
print("el rsultado de la suma es de: ",x)
#___________________
#suma de numeros en secuencia
c = 0
v = 0
while c == 0:
    n1: int=int(input("ingrese un numero entero (el programa finaliza cuando ingrese 0)"))
    if n1 != 0:
        v=n1+v
    else:
        v=n1+v
        print(f"el resultado es: {v}")
        c = 1
#___________________
#numero aleatorio
from random import randint
x = randint(0, 9)
n=100
c=0
while n != x:
    n: int=int(input("intente adivinar el numero de 0 al 9. "))
    if n != x:
        print("numero equivocado, intenta de nuevo ")
        c+=1
print(f"correcto! adivino el numero {x} en {c+1} intentos" )
#___________________
#de 0 a 100 de forma decreciente
for i in range(100, -1, -2):
    print(i)
#___________________
#suma desde 0 hasta numero ingresado
n: int=int(input("ingrese hasta que numero quiere que se sume "))
n = abs(n)
x=0
for i in range(0,n+1):
    x+=i
print(f"el resultado de la suma es: {x}")
#___________________
#clasificacion de 100 numeros
x=1
par=0
impar=0
pos=0
neg=0
cero=0
while x <= 100:
    n: int=int(input("ingrese un numero entero "))
    if n%2 == 0:
        par+=1
    if n%2 != 0:
        impar+=1
    if n>0:
        pos+=1
    if n<0:
        neg+=1
    if n==0:
        cero+=1
    x+=1
print(f"hay {pos} numeros positivos, {neg} negativos, {par} pares, {impar} impares y {cero} son cero")
#___________________
#media de 100 numeros
x=0
c=0
v=0
while x<100:
    n: int=int(input("ingrese un numero entero "))
    v+=n
    x+=1
print(f"la media de los numeros ingresados es {v/x}")
#___________________
#invertir los digitos
n1 = int(input("Ingresa un número para invertir: "))
n2 = abs(n1)
invertido = 0
while n2 > 0:
    ultimo = n2 % 10
    invertido = invertido * 10 + ultimo
    n2 = n2 // 10
if n1<0:
    invertido*=-1
print(f"El número invertido es: {invertido}")