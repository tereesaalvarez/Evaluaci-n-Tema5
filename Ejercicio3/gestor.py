import pickle
from io import open

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance

    def __str__(self):
        return "Nombre: {} Vida: {} Ataque: {} Defensa: {} Alcance: {}".format(self.nombre, self.vida, self.ataque, self.defensa, self.alcance)

class Gestor:
    def __init__(self):
        self.listaPersonajes = []

    def agregarPersonaje(self, personaje,vida, ataque, defensa, alcance):
        self.listaPersonajes.append(personaje)


    def mostrarPersonajes(self):
        for personaje in self.listaPersonajes:
            print(personaje)

    def borrarPersonaje(self, nombre):
        for personaje in self.listaPersonajes:
            if Personaje.self.nombre == nombre:
                self.listaPersonajes.remove(personaje)

    def guardarPersonajes(self):
        fichero = open("personajes.pckl", "wb")
        pickle.dump(self.listaPersonajes, fichero)
        fichero.close()

    def cargarPersonajes(self):
        fichero = open("personajes.pckl", "rb")
        self.listaPersonajes = pickle.load(fichero)
        fichero.close()