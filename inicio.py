# -*- coding: utf-8 -*-
from analisisDatos import *

class Inicio:

    "INSTANCIAS"
    def __init__(self):
        self.datos = Datos()

    "CARGAR DATOS"
    def cargar_Datos(self):
        #Cargar datos
        datosArchivo = pd.read_csv('Datos.csv')
        #CaracterÍsticas del dataset
        nombres = ['Alcohol','Acido','Ceniza','Alcalinidad','Magnesio','Fenoles','Flavonoides','FenolesNo','Proan','Intensidad','Hue','Diluidos','Proline']
        #Variable que identa
        espacio =''
        #Resultado al archivo
        resultado =''
        #Llamado función ordenar
        return (self.datos.ordenar(datosArchivo, 0, espacio, nombres, resultado))

    """ AGREGAR EL RESULTADO AL ARCHIVO """
    def escribir_Archivo(self,salida):
        resultado = open("resultado.txt", "w")
        resultado.write(salida)
        resultado.close()
        
inicio = Inicio()
salida = inicio.cargar_Datos()
inicio.escribir_Archivo(salida)
