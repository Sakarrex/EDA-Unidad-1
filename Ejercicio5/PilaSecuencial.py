import numpy as np


class PilaSecuencial:
    arreglo = None
    tope = 0

    def __init__(self,tamanio) -> None:
        self.arreglo = np.empty(int(tamanio),dtype=int)
        for i in range(len(self.arreglo)):
            self.arreglo[i] = 0
        self.tope = 0
    
    def vacio(self):
        return (self.tope == 0)
    
    def Insertar(self,num):
        if self.tope == len(self.arreglo):
            print("Pila llena")
        else:
            self.arreglo[self.tope] = num
            self.tope += 1
    
    def Suprimir(self):
        elem_devolver = None
        if self.vacio() == True:
            print("No se puede suprimir, pila vacia")
        else:
            elem_devolver = self.arreglo[self.tope-1]
            self.arreglo[self.tope-1] = 0
            self.tope -= 1
        return elem_devolver
    
    def ComprobarUltimo(self):
        return(self.arreglo[self.tope-1])
    
    def recorrer(self):
        cadena = " "
        for i in range(len(self.arreglo)):
            if self.arreglo[i] != None:
                cadena = cadena + "," + str(self.arreglo[i])
        return cadena
                
    def llena(self):
        return (self.tope == len(self.arreglo))

    def Mostrar(self):
        while self.tope >0:
            print(self.Suprimir())
    





