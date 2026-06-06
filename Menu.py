from main import es_par,busqueda,separacion
from sumas import suma,consumidor
from Objeto import Objeto

def menu():
    interruptor = True

    while interruptor:
        print("Menu")
        print("1. Programa de pares e impares")
        print("2. Programa de sumas")
        print("3. Programa donde muestra el objeto")
        print("4. Saliendo")

        seleccionar = int(input("Selecciona un opcion: "))


        match seleccionar:
            case 1:
                pares, impares = busqueda(1, 99)

                mayores, menores = separacion(pares)

                print(pares)
                print(impares)
                print(mayores)
                print(menores)

            case 2:
                num1, num2 = consumidor()
                resultado = suma(num1, num2)
                print(resultado)

            case 3:
                globin = Objeto("Cristian",10, 100)
                print("Nombre:", globin.nombre)
                print("Nivel:", globin.nivel)
                print("Vida:", globin.vida)

            case 4:
                print("Saliendo")
                interruptor = False
            case _:
                print("Opcion invalida")


if __name__ == '__main__':
    menu()