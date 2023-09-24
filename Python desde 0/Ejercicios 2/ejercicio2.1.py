#Falto el profesor y los alumnos hiciero su propia clase, uno hace de profesor y otro de su asistente

#Pedir el nombre y la edad de los compañeros que vinieron a clases

#función para poder obtener al asistente y al profesor segun la edad
def obtener_compañeros (cantidad_de_compañeros):
    
    #creando la lista de los compañeros
    compañeros = []
    
    #ejecutndo un for para pedir la información de cada compañero 
    for i in range (cantidad_de_compañeros):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = int(input("Ingrese la edad del compañero: ")) 
        compañero = (nombre, edad)
        
        #Agregand la información a la lista
        compañeros.append(compañero)
    
    #ordenando demayor a menor segun su edad
    compañeros.sort(key=lambda x: x[1])
    
    #compañeros [x] devuelve una tupla con (nombre, edad)y despues accedemos al nombre 
    #para definir al asistente y a al profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    #Return una tupla
    return asistente, profesor
#desempaquetamos lo que nos retorna la función 
asistente,profesor = obtener_compañeros(5)

#mostrando el resultado
print(f"El profesor es: {profesor} y su asistente es: {asistente}")