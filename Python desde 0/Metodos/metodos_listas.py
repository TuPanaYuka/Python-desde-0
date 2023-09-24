
#creando una lista con list
lista = list([7, 10, 30, True, False])

#cuenta la cantidad de elementos de una lista
cantidad_de_elementos = len(lista)

#agregando elementos a una lista
lista.append(100)

#agregando un elemento a la lista con un ídice específico
lista.insert(2, 44)

#agregando varios elementos a la lista
lista.extend([2023])

#eliminando un elemento de una lista por su índice
lista.pop(0) #usamos -1 para eliminar el ultimo elemento

#removiendo un elemento de la lista por su valor
lista.remove(True)

#ordena la lista de forma ascendente a descendente, si usamos reverse=true lo ordena al revés
lista.sort()

#invirtiendo los elementos de una lista
lista.reverse()

#verificando si un elemento se encuentra en una lista
elemento_encontrado=lista.index(44)

#eliminando todos los elementos de una lista
#lista.clear()

print(elemento_encontrado)


