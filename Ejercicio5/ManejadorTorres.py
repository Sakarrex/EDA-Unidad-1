


from PilaSecuencial import PilaSecuencial

class ManejadorTorres:
    cant_movimientos = 0
    tamanio = 0
    Torres = []


    def __init__(self,tamanio) -> None:

        self.tamanio = int(tamanio)
        self.Torres = []
        cant_movimientos = 0
        for i in range(3):
            self.Torres.append(PilaSecuencial(tamanio))
        
        for i in range(tamanio):
            self.Torres[0].Insertar(tamanio-i)
            
        
        for i in range(len(self.Torres)):
            print("Torre {}: {}".format(i+1,self.Torres[i].recorrer()))

        
        
    
       
    def MoverPieza(self,PilaOrigen,PilaDestino):
        gano = False

        if int(PilaDestino == PilaOrigen) or PilaOrigen < 1 or PilaDestino > 3 or self.Torres[int(PilaOrigen)-1].vacio() == True:
            raise ValueError
        
        pieza_a_mover = self.Torres[int(PilaOrigen)-1].ComprobarUltimo()
       
        if self.Torres[int(PilaDestino)-1].vacio() == False: 
            pieza_destino = self.Torres[int(PilaDestino)-1].ComprobarUltimo()
        else:
            pieza_destino = self.tamanio+1
        
       



        if pieza_a_mover < pieza_destino:
            pieza_a_mover = self.Torres[int(PilaOrigen)-1].Suprimir()
            self.Torres[PilaDestino-1].Insertar(pieza_a_mover)
            self.cant_movimientos +=1 
            self.MostrarTorres()

            
            if self.Torres[2].llena() == True:
                gano = True
                print("Felicidades, usted a ganado!")
                print("Numero de movimientos: " + str(self.cant_movimientos))
                print("Cantidad de movimeintos minimos: " + str((2**self.tamanio)-1))
        


        else:
            print("Print no se puede mover esa pieza")
        
        return(gano)
        
    
    def MostrarTorres(self):
        for i in range(len(self.Torres)):
            print("Torre {}: {}".format(i+1,self.Torres[i].recorrer()))


     
        
        