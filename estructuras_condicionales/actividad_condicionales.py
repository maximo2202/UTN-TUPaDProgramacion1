#mayor_de_edad
edad = int(input("ingrese su edad por favor "))
if edad >= 18:
    print("usted es mayor de edad")
else:
    print("usted es menor de edad")
#_______________________
#aprobado_desaprobado
nota = float(input("ingrese su nota final "))
if nota >= 6 and nota <= 10:
    print("usted esta aprobado de forma directa")
elif nota < 6 and nota >= 0:
    print("usted esta desaprobado")
else:
    print("entrada invalida")
#_______________________
#numero_par
n = int(input("ingrese un numero par "))
if n % 2 == 0:
    print("usted ingreso un numero par")
else:
    print("por favor, ingrese un numero par")
#_______________________
#categoria_edad
edad = int(input("ingrese su edad "))
if edad < 12 and edad > 0:
    print("usted es un niño")
elif edad >= 12 and edad < 18:
    print("usted es un adolecente")
elif edad >= 18 and edad < 30:
    print("usted es un adulto/a joven")
elif edad >= 30:
    print("usted es un adulto/a")
else:
    print("entrada invalida")
#_______________________
#contraseña
password = input("ingrese una contraseña con minimo 8 y maximo 14 caracteres ")
x = len(password)
if x <= 14 and x >= 8:
    print("ha ingresado una contraseña correcta")
elif x < 8:
    print("contraseña demasiado corta")
else:
    print("contraseña demasiado larga")
#_______________________
#statistics
from statistics import mode, median, mean
import random
lista = [random.randint(1, 100) for i in range(50)]
media = mean(lista)
mediana = median(lista)
moda = mode(lista)
print(f"media {media}, mediana {mediana}, moda {moda}")
if media > mediana:
    print(f"hay sesgo positivo")
elif media < mediana:
    print(f"hay sesgo negativo")
else:
    print(f"no hay sesgo")
#_______________________
#ultima_vocal
palabra = input("ingrese su palabra o frase ")
x = len(palabra)
subp = palabra[x-1:]
if subp == "a" or subp == "A" or subp == "e" or subp == "E" or subp == "i" or subp == "I" or subp == "o" or subp == "O" or subp == "u" or subp == "U":
    print(f"{palabra}!!")
else:
    print(palabra)
#_______________________
#nombre_posicion
nom = input("ingrese su nombre ")
print("si desea transformar su nombre a mayusculas ingrese 1")
print("si desea transformar su nombre a minusculas ingrese 2")
print("si desea transformar la primer letra a mayuscula ingrese 3")
pos = int(input("ingrese que posicion desea "))
if pos == 1:
    print(f"{nom.upper()}")
elif pos == 2:
    print(f"{nom.lower()}")
elif pos == 3:
    print(f"{nom.title()}")
else:
    print("opcion invalida")
#_______________________
#terremoto
mag = float(input("ingrese magnitud del terremoto "))
if mag < 3 and mag > 0:
    print(f"muy leve")
elif mag >= 3 and mag < 4:
    print(f"leve")
elif mag >= 4 and mag < 5:
    print(f"moderado")
elif mag >= 5 and mag < 6:
    print(f"fuerte")
elif mag >= 6 and mag < 7:
    print(f"muy fuerte")
elif mag >= 7:
    print(f"extremo")
else:
    print("entrada invalida")
#_______________________
#estacion_del_año
H = input("ingrese en que hemisferio se encuentra usted ")
dia = int(input("ingrese el numero de dia actual "))
mes = int(input("ingrese numero de mes actual "))
h = H.lower()
if h == "sur" or h == "hemisferio sur":
    if mes==12 and dia>=21 and dia<=31 or mes==3 and dia<=20 and dia>=1 or mes>=1 and mes<=2:
        print(f"en su ubicacion es verano")
    elif mes==3 and dia>=21 and dia<=31 or mes==6 and dia>=1 and dia<=20 or mes>=4 and mes<=5:
        print(f"en su ubicacion es otoño")
    elif mes==6 and dia>=21 and dia<=30 or mes==9 and dia>=1 and dia<=20 or mes>=7 and mes<=8:
        print(f"en su ubicacion es invierno")
    elif mes==9 and dia>=21 and dia<=30 or mes==12 and dia>=1 and dia<=20 or mes>=10 and mes<=11:
        print(f"en su ubicacion es primavera")
    pass
elif h == "norte" or h == "hemisferio norte":
    if mes==12 and dia>=21 and dia<=31 or mes==3 and dia<=20 and dia>=1 or mes>=1 and mes<=2:
        print(f"en su ubicacion es invierno")
    elif mes==3 and dia>=21 and dia<=31 or mes==6 and dia>=1 and dia<=20 or mes>=4 and mes<=5:
        print(f"en su ubicacion es primavera")
    elif mes==6 and dia>=21 and dia<=30 or mes==9 and dia>=1 and dia<=20 or mes>=7 and mes<=8:
        print(f"en su ubicacion es verano")
    elif mes==9 and dia>=21 and dia<=30 or mes==12 and dia>=1 and dia<=20 or mes>=10 and mes<=11:
        print(f"en su ubicacion es otoño")
    pass