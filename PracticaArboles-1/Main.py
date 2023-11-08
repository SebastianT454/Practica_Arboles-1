# Importando modulos.
from Arbol import *
from Archivo import *
from Carpeta import *

# Programa:

archivo_zip = "C:/Users/Sebastian/Desktop/Estructuras_dinamicas_misc/PracticaArboles.zip"

# Creamos un árbol de archivos y carpetas a partir de un archivo zip
arbol = Arbol(archivo_zip)

# Almacenamos la información de los archivos txt
#arbol.obtener_informacion()

'''
# Encontramos todas las carpetas
carpetas = list(arbol.encontrar_carpetas())

# Imprimimos la información de los archivos txt
for archivo in arbol.raiz.informacion.values():
    print(archivo)

# Imprimimos el nombre de todas las carpetas
for carpeta in carpetas:
    print(carpeta.nombre)
'''