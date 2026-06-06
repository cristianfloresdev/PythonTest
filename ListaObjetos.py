from Objeto import Objeto

def listar():
    print("Lista de Objetos")
    #Creamos lista de enemigos
    globin = Objeto("Globin", 5, 50)
    orco = Objeto("Orco", 10, 100)
    dragon = Objeto("Dragon", 50, 5000)

    #Guardamos enemigos en una lista
    enemigos = [globin,orco,dragon]

    #Recorremos la lista con un for each
    for objeto in enemigos:
        print(objeto.nombre)
        print(objeto.nivel)
        print(objeto.vida)

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


if __name__ == '__main__':
    listar()

    diccionarios()