from os import uname
from arreglo import Arreglo2Pilas

if __name__ == "__main__":
    unArreglo = Arreglo2Pilas(4)
    unArreglo.IncrementarPila1(1)
    unArreglo.IncrementarPila2(5)
    unArreglo.IncrementarPila2(9)
    unArreglo.IncrementarPila1(7)
    unArreglo.IncrementarPila2(2)
    unArreglo.Mostrar1()
    unArreglo.Mostrar2()

    