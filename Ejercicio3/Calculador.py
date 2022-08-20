from PilaEncadenada import PilaEncadenada

class Calculador:
    Pila = None

    def __init__(self) -> None:
        self.Pila = PilaEncadenada()
    
    def ObtenerFactorial(self,valor):
        if valor < 0:
            raise ValueError

        if valor == 0 or valor == 1:
            return(1)
        else:
            actual = 1
            factorial = 1
            
            while actual <= valor:
                self.Pila.Insertar(actual)
                actual += 1
            
            while actual > 1:
                factorial = factorial*(self.Pila.Suprimir())
                actual -= 1
                
            
            return factorial