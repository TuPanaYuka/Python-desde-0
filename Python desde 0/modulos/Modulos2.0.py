#si el módulo estuviera dentro de una carpeta de una misma ruta, se importa así:
#import fun_piolas.saludar as m_saluidn

import sys
sys.path.append("c:\\Users\\Argelia\\Desktop\\Python desde 0\\fun_piolas")

import saludar as m_saludar
print(m_saludar.saludar("Messi"))

