#creando un conjunto con set()

conjunto =  set(["Datos", "Bicho"])

#metiendo un conjunto dentro de otro conjuntos
conjunto1 = frozenset(["Dato1", "Dato2", "Dato3"])
conjunto2 = {conjunto1, "Dato3"}
print(conjunto2)

#Teoría de conjuntos

conjunto1 = {1, 3, 5, 7}
conjunto2 = {1, 3, 7}

#subset = subconjunto; superset = superconjunto

#verificando si es un subconjunto
resultado_sub = conjunto2.issubset(conjunto1)
resultado_sub = conjunto2 >= conjunto1
print(resultado_sub)

#verificando si es un superconjunto
resultado_super = conjunto1.issuperset(conjunto2)
resultado_super = conjunto1 > conjunto2
print(resultado_super)

#verificar si hay algún número en común
resultado_en_comun= conjunto2.isdisjoint(conjunto1)
print(resultado_en_comun)