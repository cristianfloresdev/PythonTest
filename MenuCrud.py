from ListaObjetos import listar, eliminarEnemigo, buscar_enemigo, modificarEnemigo, mostrar_enemigo, agregar_enemigo
from Objeto import Objeto


def menuEnemigo():
    print("Menu de Enemigo CRUD")
    interruptor = True
    enemigos = listar()

    while interruptor:
        print("Menu")
        print("1. Agregar Enemigos")
        print("2. Buscar Enemigo")
        print("3. Eliminar Enemigo")
        print("4. Modificar Enemigo")
        print("5. Mostrar Enemigo")
        print("6. saliendo")

        seleccionar = int(input("selecciona un opción: "))

        match seleccionar:
            case 1:
                nombre = input("Ingrese su nombre: ")
                nivel = input("Ingrese su nivel: ")
                vida = input("Ingrese su vida: ")

                agregar_enemigo(nombre, nivel, vida, enemigos)
                print("Agregado correctamente")

            case 2:
                nombre = input("Ingrese enemigo a buscar: ")
                buscar_enemigo(nombre,enemigos)
                print("Enemigo encontrado: ", nombre)

            case 3:
                nombre = input("Ingrese enemigo a eliminar: ")
                eliminarEnemigo(nombre,enemigos)
                print("Enemigo eliminado correctamente: ", nombre)

            case 4:
                modificarEnemigo("Cthulu", "Dagon", 500, 1000, enemigos)
                print("Enemigo modificado correctamente")

            case 5:
                print("Enemigo mostrado correctamente")
                mostrar_enemigo(enemigos)

            case _:
                interruptor = False

if __name__ == '__main__':
    menuEnemigo()







