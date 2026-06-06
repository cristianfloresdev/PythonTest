def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def consumidor():
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))

    return num1, num2

if __name__ == '__main__':
    num1, num2 = consumidor()
    resultado = suma(num1, num2)
    print("Resultado final: ", resultado)
