from operator import truediv

from Objeto import Objeto

def listar():
    print("Lista de Objetos")
    #Creamos lista de enemigos
    globin = Objeto("Globin", 5, 50)
    orco = Objeto("Orco", 10, 100)
    dragon = Objeto("Dragon", 50, 5000)
    oso = Objeto("Oso", 10, 100)

    #Guardamos enemigos en una lista
    enemigos = [globin,orco,dragon,oso]

    #Recorremos la lista con un for each
    for objeto in enemigos:
        print(objeto.nombre)
        print(objeto.nivel)
        print(objeto.vida)

    return enemigos

def diccionarios():
    print("")
    print("Diccionarios")

    enemigo = {
        "nombre": "Globin",
        "nivel": 5,
        "vida": 50
    }
    print(enemigo["nombre"])

    #Modificar
    enemigo["vida"] = 30
    print(enemigo["vida"])
    print(enemigo["nivel"])

    #Agregar
    enemigo["Arma"] = "Hacha"
    print(enemigo["Arma"])

#Agregar enemigo
def agregar_enemigo(nombre, nivel, vida, enemigos):

    enemigos.append(Objeto(nombre, nivel, vida))

    return enemigos

#Mostrar enemigo
def mostrar_enemigo(enemigos):
    print("Enemigos")
    for enemigo in enemigos:
        print(f" Nombre: {enemigo.nombre} ")
        print(f" Nivel: {enemigo.nivel} ")
        print(f" Vida: {enemigo.vida} ")


#Eliminar enemigos
def eliminarEnemigo(nombre, enemigos):

    for enemigo in enemigos:
        if enemigo.nombre == nombre:
            enemigos.remove(enemigo)
            return
#Modificar enemigos
def modificarEnemigo(nombre, nuevo_nombre, nuevo_nivel, nuevo_vida, enemigos):
    for enemigo in enemigos:
        if enemigo.nombre == nombre:
            enemigo.nombre = nuevo_nombre
            enemigo.nivel = nuevo_nivel
            enemigo.vida = nuevo_vida
            return True
    return False

#Buscar enemigos
def buscar_enemigo(nombre, enemigos):
        for enemigo in enemigos:
            if enemigo.nombre == nombre:
                return enemigo

        return None

if __name__ == '__main__':

    enemigos = listar()

    #Mostrar enemigo o listar
    mostrar_enemigo(enemigos)

    #Agregar enemigo
    agregar_enemigo(nombre="Daron", nivel=20, vida=500,enemigos=[Objeto("Orco", 10, 100)])

    #listar()

    #diccionarios()



    resultado = buscar_enemigo("Oso", enemigos)
    #Si aparece el objeto es porque existe
    print("Resultado" , resultado)
    print(type(resultado))

    if resultado is not None:
        print("Resultado" , resultado.nombre)

