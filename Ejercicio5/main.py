from turtle import Turtle
from ManejadorTorres import ManejadorTorres

if __name__ == "__main__":
    gano = False
    UnManejador = ManejadorTorres(int(input("Ingresar el tamanio de las torres: ")))
    while gano != True:
        try:
            torre_origen = int(input("Indicar numero de torre origen: "))
            torre_destino = int(input("Indicar numero de torre fin: "))
            gano = UnManejador.MoverPieza(torre_origen,torre_destino)
        except ValueError:
            print("Torres no validas Ingresadas")