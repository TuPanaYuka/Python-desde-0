
ingreso_mensual = 92000
gasto_mensual = 90000

#if anidado y else if (elif)
if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estamos en numeros rojos")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Bien pa")
    else: 
        print ("Gastas mucho rey, ahorra más")
        
elif ingreso_mensual > 5000:
    print("Estás bien en Latam")
    
elif ingreso_mensual > 200:
    print("okis, pero tasmedio pelando")
    
else:
    print("jaja que pobre que sos")  