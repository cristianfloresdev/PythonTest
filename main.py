
def es_par(numero):
    return numero % 2 == 0

def busqueda(inicio, fin):
    pares = []
    impares = []

    for numero in range(inicio, fin + 1):
        if es_par(numero):
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

def separacion(numeros):
    print("separacion")
    mayores = []
    menores = []

    for numero in numeros:
        if numero > 50:
            mayores.append(numero)
        else:
            menores.append(numero)
    return mayores, menores

#Main
if __name__ == '__main__':
    pares, impares = busqueda(inicio=1, fin=100)
    mayores, menores = separacion(pares)

    print("Pares: ", pares)
    print("Impares: ", impares)

    print("Separacion")
    print("Mayores: ", mayores)
    print("Menores: ", menores)



