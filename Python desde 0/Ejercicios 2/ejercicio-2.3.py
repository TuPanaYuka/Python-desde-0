#creando una función que me muestre la serie finonacci entre 0 y el numero dado
def fibonacci (num):
    a,b = 0,1
    fibonacci_lista = [2]
    for i in range(num):
        if b > num: return fibonacci_lista
        else:
            fibonacci_lista.append(b) 
            a,b = b,a+b 
resultado = fibonacci(20)


#Forma optimizada
def fibonacci(num):
    a, b = 0, 1
    fibonacci_lista = []
    while b > num:
        fibonacci_lista.append(b)
        a, b = b, a + b
    return fibonacci_lista

resultado = fibonacci(-1)
print(resultado)
