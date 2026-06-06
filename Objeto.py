
class Objeto:
    def __init__(self, nombre, nivel, vida):
        self.nombre = nombre
        self.nivel = nivel
        self.vida = vida

if __name__ == '__main__':
    globin = Objeto("Globin", 5)

    #Acceder a los datos
    print("Nombre: ", globin.nombre)
    print("Nivel: ", globin.nivel)

    #modificar datos
    globin.nombre = "Dragon"
    print("Nombre: ", globin.nombre)