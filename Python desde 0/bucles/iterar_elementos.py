animales = ["perro", "gato", "monkey", "horse"]
numeros = [10, 11, 12 , 14, 15]

#recorriendo el conjunto animales
print("------------------------------")
for animal in animales:
    print(f"Ahora la varialble animal es igual a: {animal}")

#recorriendo el conjunto numeros
print("------------------------------")
for numero in numeros:
    print(numero*2)
    
#iterando 2 o mas elementos de un conjunto con la función zip()
print("------------------------------")
for animal,numero in zip(animales,numeros):
    print(f"Recorriendo conjunto1: {animal}")
    print(f"Recorriendo conjunto2: {numero}")
    
#forma optima de recorrer un conjunto
print("------------------------------")
for num in enumerate(numeros):
    indice = num[0]
    valor = num [1]
    print(f"El indice es: {indice} y el valor es: {valor}")
print("------------------------------")
    
#listas, conjuntos y tuplas se iteran de igual forma