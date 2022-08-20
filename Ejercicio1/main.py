from PilaSecuencial import PilaSecuencial
from PilaEncadenada import PilaEncadenada

if __name__ == "__main__":

    nuevapila = PilaSecuencial(3)
    nuevapila.Suprimir()
    nuevapila.Insertar(1)
    nuevapila.Insertar(5)
    nuevapila.Insertar(9)
    nuevapila.Insertar(15)
    nuevapila.Mostrar()

