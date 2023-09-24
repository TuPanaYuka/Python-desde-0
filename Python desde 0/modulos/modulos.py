#importandoo un modulo y asignandole el nombre m_saludar
#import modulo_saludar as m_saludar

#Desde ese modulo importamos 2 funciones
from fun_piolas.saludar import saludar, saludar_raro as saludar_como_pana

#Creamos las variables con los saludos
saludo = saludar("Messi") 
saludo_raro = saludar_como_pana("Rodri")

#mostramos los resultadops
print(saludo)
print (saludo_raro)

#Para ve las propiedades del name_space
#print(dir(m_saludar))


