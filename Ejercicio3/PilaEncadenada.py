
from ElementoPila import ElementoPila

class PilaEncadenada:
    tope = None
    cant = 0

    def __init__(self) -> None:
        self.cant = 0
        self.tope = None
    
    def vacio(self):
        return (self.tope == None)
    
    def Insertar(self,valor):
        nuevoElemento = ElementoPila(valor)
        nuevoElemento.setSiguiente(self.tope)
        self.tope = nuevoElemento
        self.cant += 1
    
    def Suprimir(self):
        elem_devolver = None
        if self.vacio() == True:
            return 1
        else:
            elem_devolver = self.tope.getValor()
            self.tope = self.tope.getSiguiente()
            self.cant -= 1
        return elem_devolver
    
    def Mostrar(self):
        while self.cant > 0:
            print(self.Suprimir())


