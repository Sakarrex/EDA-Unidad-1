from PilaEncadenada import PilaEncadenada
import math


class Conversor:

    Pila = None

    def __init__(self) -> None:
        self.Pila = PilaEncadenada()
    
    def ConvertirABinario(self,valor):
        num = valor
        while math.floor(num) != 0:
            self.Pila.Insertar(math.floor(num%2))
            num = math.floor(num/2)
            
        
        self.Pila.Mostrar()


    