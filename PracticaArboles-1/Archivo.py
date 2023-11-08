import os
import zipfile

class Archivo:
    def __init__(self, nombre, contenido):
        self.path = nombre
        self.informacion = contenido
        self.tipo = "archivo"
        self.tamaño = os.path.getsize(nombre)
        self.fecha_creación = os.path.getctime(nombre)