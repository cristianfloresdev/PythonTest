import json
from Objeto import Objeto
from ListaObjetos import listar

datos = [
    {
        "nombre": "Artemisa",
        "nivel": 99
    },
    {
        "nombre": "Cristian",
        "nivel": 100
    }
]

def conversionEnemigo(enemigos):
    enemigos_json = []

    # Obtenemos los objetos dentro de la lista
    for enemigo in enemigos:
        diccionarioEnemigo = {
            "nombre": enemigo.nombre,
            "nivel": enemigo.nivel,
            "vida": enemigo.vida
        }
        enemigos_json.append(diccionarioEnemigo)

    return enemigos_json

if __name__ == '__main__':

    #Si existe el documento lo sobreescribe, en dado que no, lo crea, lo manipulo con el diccionario
    #Guardar
    json.dump(datos, open("jugador.json", "w"))

    #Leerla
    json.load(open("jugador.json"))

    datos = json.load(open("jugador.json"))

    #Imprime el tipo de dato
    print(type(datos))

    print(datos)

    #
    enemigos = listar()

    enemigos_json = conversionEnemigo(enemigos)

    print(enemigos_json)
    print(type(enemigos_json))

    json.dump(enemigos_json, open("jugador.json", "w"))

    for enemigo in datos:
        Objeto(
            enemigo["nombre"],
            enemigo["nivel"],
            enemigo["vida"]
        )
