#lista de 0 a 100 de multiplos de 4
lista = list(range(0,101,4))
print(lista)
#______________________
#mostrar penultimo elemnto
lista = ["marti","anto","fede","agus","cande"]
print(lista[-2])
#______________________
#crear lista vacia y usar append
lista = []
lista.append("naza")
lista.append("coti")
lista.append("cami")
print(f"{lista}") 
#______________________
#reemplazar el segundo y ultimo valor
animales = ["perro", "gato", "conejo", "pez"]
animales[-3] = "loro"
animales[-1] = "oso"
print(f"{animales}")
#______________________
#analizar el programa
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(f"{numeros}")
#Este programa elimina el valor más alto (sea entero o decimal) de la lista.
#______________________
#lista del 10 al 30
lista = list(range(10,31,5))
print(f"lista entera {lista}")
print(f"primeros 2 valores {lista[0:2]}")
#______________________
#reemplazar los indices centrales
lista = ["sedan", "polo", "suran", "gol"]
lista[1] = "golf"
lista[2] = "sirocco"
print(f"{lista} ")
#______________________
#dobles
dobles = []
dobles.append(2*5)
dobles.append(2*10)
dobles.append(2*15)
print(dobles)
#______________________
#lista compras
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)
#______________________
#lista anidada
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(f"{lista_anidada}")