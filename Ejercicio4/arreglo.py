import numpy as np

class Arreglo2Pilas:
    __tope1 = 0
    __tope2 = 0
    __arreglo = None

    def __init__(self,tamanio) -> None:
        self.__tope1 = 0
        self.__tope2 = int(tamanio)-1
        self.__arreglo = np.empty(int(tamanio),dtype=int)
    
    def IncrementarPila1(self,valor):
        if self.__tope1 <= self.__tope2 and self.__tope1 <= len(self.__arreglo):
            self.__arreglo[self.__tope1] = valor
            self.__tope1+=1
            print("Se incremento la pila 1")
        else:
            print("La pila 1 no puede crecer mas")
    
    def IncrementarPila2(self,valor):
        if self.__tope1 <= self.__tope2 and self.__tope1 >= 0:
            self.__arreglo[self.__tope2] = valor
            self.__tope2-=1
            print("Se incremento la pila 2")

        else:
            print("La pila 2 no puede crecer mas")
    
    def vacia1(self):
        return (self.__tope1 == 0)
    
    def vacia2(self):
        return (self.__tope2 == len(self.__arreglo)-1)
    
    def SuprimirPila1(self):
        valor_devolver = None
        if self.vacia1() == True:
            print("No se puede suprimir, pila 1 vacia")
        else:
            valor_devolver = self.__arreglo[self.__tope1-1]
            self.__tope1 -= 1
        return valor_devolver
    
    
    def SuprimirPila2(self):
        valor_devolver = None
        if self.vacia2() == True:
            print("No se puede suprimir, pila 2 vacia")
        else:
            valor_devolver = self.__arreglo[self.__tope2+1]
            self.__tope2 += 1
        return valor_devolver
    
    def Mostrar1(self):
        if self.vacia1() == True:
            print("Pila 1 Vacia")
        
        else: 
            print("Pila 1: ")
        
            while self.__tope1 > 0:
                print(self.SuprimirPila1())
        
        
    def Mostrar2(self):
        if self.vacia2() == True:
            print("Pila 2 vacia")
        else:
            print("Pila 2: ")
            while self.__tope2 < len(self.__arreglo)-1:
                print(self.SuprimirPila2())
    
    def llena(self):
        return self.__tope1 <= self.__tope2
            
    

    
            

                

    
