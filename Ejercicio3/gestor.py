


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

