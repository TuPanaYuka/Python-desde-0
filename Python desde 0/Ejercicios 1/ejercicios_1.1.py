
#promedio de duradion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio= 4
dalto_curso = 1.5

#Duración de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#Diferencias de duracion 

diferencia_con_otros_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_otros_max = round( 100 - (dalto_curso  / otros_cursos_max *100), 2) 
diferencia_con_otros_promedio = 100 -dalto_curso / otros_cursos_promedio * 100 

#10 horas de dalto
diez_horas_comparado_a_otros_curos = round((otros_cursos_promedio / dalto_curso *10), 2)
diez_horas_comparado_a_dalto = round((dalto_curso / otros_cursos_promedio* 10), 2)

#mostrando las diferencias de duracion (ejercicio A)
print("-----------------------------------")
print("El curso de dalto dura:")
print(f" - {diferencia_con_otros_min}% menos que el curso más rápido")
print(f" - {diferencia_con_otros_max}% menos que el curso más lento")
print(f" - {diferencia_con_otros_promedio}% menos que el curso promedio")
print("-----------------------------------")

#Calculando el porcentaje de tiempo vacio
tiempo_vacio_promedio = round((100 - otros_cursos_promedio / crudo_promedio * 100), 2)
tiempo_vacio_dalto = round((100 - dalto_curso / crudo_dalto * 100), 2)

#calculando el tiempo vacio (ejercicio B)
print("Cantidad de crudo:")
print(f" -El curso promedio elimina un {tiempo_vacio_promedio}% de crudo" )
print(f" -El curso que estoy viendo elimina un {tiempo_vacio_dalto}% de crudo" )
print("-----------------------------------")

#calculando cuanto equivalen 10 horas de este curso en otros cursos
print("ver 10 horas de dalto equivale a:")
print(f"-{diez_horas_comparado_a_otros_curos} horas de otros curos")
print(f"-Ver 10 horas de otros curos equivale a ver {diez_horas_comparado_a_dalto} horas del curso de Dalto")
print("-----------------------------------")
