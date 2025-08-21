#imprimir hola mundo
print("hola mundo")
#__________________
#imprimir nombre de usuario
nombre=input("como te llamas ")
print(f"hola {nombre}")
#__________________
#imprimir presentacion
nombre=input("nombre:")
apellido=input("apellido:")
edad=input("edad:")
residencia=input("reside en:")
print(f"soy {nombre} {apellido} tengo {edad} y vivo en {residencia}")
#__________________
#area y perimetro
radio=int(input("inrgese el valor del radio "))
import math
perimetro=2*radio*math.pi
area=radio*radio*math.pi
print(f"el perimetro es: {perimetro}")
print(f"el area es: {area}")
#__________________
#segundos a horas
seg=int(input("ingrese cantidad de segundos "))
hora=seg/3600
print(f"{seg} equivale a {hora} horas")
#__________________
#tabla de multiplicar
num=int(input("ingrese el numero que desea multipicar "))
for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}") 
    #__________________
#calculadora basica
num1=int(input("ingrese un numero distinto a 0 "))
num2=int(input("ingrese otro numero distinto a 0 "))
print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} - {num2} = {num1-num2}")
print(f"{num1} * {num2} = {num1*num2}")
print(f"{num1} / {num2} = {num1/num2}")
#__________________
#IMC
peso=int(input("ingrese su peso en kg "))
altura=float(input("ingrese su altura en m "))
x= altura ** 2
print(f"su IMC es de {peso/x}")
#__________________
#celsius a fahrenheit
C=int(input("ingrese temperatura es grados celsius "))
F= C*9/5
print(f"{C} grados celsius en fahrenheit serian {F + 32} grados fahrenheit")
#__________________
#promedio 
n1 = int(input("ingrese el primer numero "))
n2 = int(input("ingrese el segundo numero "))
n3 = int(input("ingrese el tercer numero "))
x= n1 + n2+ n3
print(f"el promedio de {n1},{n2} y {n3} es {x/3}")