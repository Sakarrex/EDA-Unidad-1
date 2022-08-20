from Calculador import Calculador

if __name__ == "__main__":
    UnCalculador = Calculador()
    try:
        print(UnCalculador.ObtenerFactorial(int(input("Ingresar numero a obtener factorial: "))))
    except(ValueError):
        print("No se puede obtener factorail de un numero negativo")
