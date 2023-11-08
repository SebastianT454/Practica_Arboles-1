# Importando modulos.
from Archivo import *
from Carpeta import *

# Arbol:

import os
import zipfile

class Arbol:
    def __init__(self, nombre_archivo_zip):
        with zipfile.ZipFile(nombre_archivo_zip, "r") as zip_file:
            nombre_carpeta_madre = zip_file.namelist()[0]

            self.raiz = Carpeta(nombre_carpeta_madre, nombre_archivo_zip)

            for nombre_archivo_hijo in zip_file.namelist():
                self.agregar(nombre_archivo_hijo, zip_file.read(nombre_archivo_hijo))

    def agregar(self, nombre_archivo, contenido):
        if os.path.isfile(nombre_archivo):
            self.raiz.hijos.append(Archivo(nombre_archivo, contenido))
            print("Archivo agregado!")
        else:
            nueva_carpeta = Carpeta(nombre_archivo)
            self.raiz.hijos.append(nueva_carpeta)

            # Recorremos el contenido de la nueva carpeta
            for nombre_archivo_hijo in zip_file.namelist():
                # Agregamos el archivo o carpeta hijo a la nueva carpeta
                nueva_carpeta.agregar(nombre_archivo_hijo, zip_file.read(nombre_archivo_hijo))

    def buscar(self, ruta):
        nodo = self.raiz
        for nombre_archivo in ruta.split("/")[1:]:
            nodo = nodo.hijos.get(nombre_archivo)
            if nodo is None:
                return None
        return nodo

    def crear(self, ruta, tipo):
        nodo = self.buscar(ruta)
        if nodo is None:
            raise ValueError("La ruta no existe")
        if tipo == "archivo":
            return Archivo(ruta, "")
        return Carpeta(ruta)

    def eliminar(self, ruta):
        nodo = self.buscar(ruta)
        if nodo is None:
            raise ValueError("La ruta no existe")
        if isinstance(nodo, Archivo):
            os.remove(nodo.path)
        else:
            for hijo in nodo.hijos.values():
                self.eliminar(hijo.path)
            os.rmdir(nodo.path)

    def recorrer(self, ruta=""):
        nodo = self.buscar(ruta)
        if nodo is None:
            raise ValueError("La ruta no existe")
        if isinstance(nodo, Archivo):
            print(nodo.nombre)
        else:
            for hijo in nodo.hijos.values():
                self.recorrer(hijo.path)