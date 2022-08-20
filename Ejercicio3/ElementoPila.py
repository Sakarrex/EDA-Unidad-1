class ElementoPila:
    valor = 0
    siguiente = None

    def __init__(self,valor) -> None:
        self.valor = valor
        suguiente = None
    
    def setSiguiente(self,siguiente):
        self.siguiente = siguiente
    
    def getSiguiente(self):
        return(self.siguiente)
    
    def getValor(self):
        return self.valor
        