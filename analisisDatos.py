#Librerias
import pandas as pd

class Datos:
    resultado = ''
    "FUNCION ORDENAR"
    def ordenar(self,datos, posicion, espacio, nombres, resultado):
        #Hay solo un dato??
        if datos.shape[0]!=1:
            #Identación del Árbol KD
            espacio +='| '
            #Longitud y mitad
            longitud = datos.shape[0]
            mitad = (datos.shape[0])/2
            #Ordenar datos de una columna
            datosAux = datos.sort_values(by=[nombres[posicion]],ascending=[False])
            #Reiniciar indices
            datosAux.reset_index(drop=True, inplace=True)
            #Registros del dato de la mitad y mitad+1
            aux1 = datosAux.loc[int(mitad)-1]
            aux2 = datosAux.loc[int(mitad)]
            #Promedio ((útimo elemento)+(primer elemento))/2
            self.resultado += espacio+'~'+nombres[posicion]+' '+str(datosAux.shape[0])+' '+str(round((aux1[posicion+1]+aux2[posicion+1])/2,4))+'\n'
            
            if datosAux.shape[0] != 0: 
                #Ordenar Árbol por derecha e izquierda
                if self.clasificar (datos):
                    self.resultado += espacio+'   '+str(datos.iloc[0][0])+'\n'
                else:
                    self.ordenar(datosAux[0:int(mitad)],posicion+1,espacio,nombres,resultado)
                    self.ordenar(datosAux[int(mitad):longitud],posicion+1,espacio,nombres,resultado)
                    return (self.resultado)
        else:
            #Cuando queda un solo elemento
            if datos.shape[0]==1:
                espacio+='| '
                self.resultado += espacio+'   '+str(datos.iloc[0][0])+'\n'
                return ("Hola")
            else:
                self.resultado += espacio+'   '+str(datos.iloc[0][0])+'\n'
                return ("Hi")

    "FUNCION PARA CLASIFICAR LOS DATOS"
    #Elementos ya clasificados??
    def clasificar (self, datos):
        tam = datos.shape[0]
        tipo = datos.iloc[0][0]
        for i in range (0,tam):
            tipo2 = datos.iloc[i][0]
            #Si no son de la misma clase=false
            if tipo != tipo2:
                return False
        #Si ya estan clasificados=true
        return True






