import numpy as np


class PilaSecuencial:
    arreglo = None
    tope = 0

    def __init__(self,tamanio) -> None:
        self.arreglo = np.empty(int(tamanio),dtype=int)
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
            self.tope -= 1
        return elem_devolver
    
    def Mostrar(self):
        while self.tope >0:
            print(self.Suprimir())
    





