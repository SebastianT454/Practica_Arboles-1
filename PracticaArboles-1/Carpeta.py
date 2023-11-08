import os
import zipfile

class Carpeta:
    def __init__(self, nombre, path):
        self.nombre = nombre
        self.path = path
        self.tipo = "carpeta"
        self.hijos = []