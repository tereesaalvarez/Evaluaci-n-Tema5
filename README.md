# Evaluaci-n-Tema5

Este es el link de este [repositorio](https://github.com/tereesaalvarez/Evaluaci-n-Tema5.git)


## Ejercicio 1

**Código:**
```

def suma(a,b):
    if type(a) != int or type(b) != int:
        raise TypeError("Error: Tipo de dato no válido")
    else:
        return a+b

def resta(a,b):
    if type(a) != int or type(b) != int:
        raise TypeError("Error: Tipo de dato no válido")
    else:
        return a-b

def producto(a,b):
    if type(a) != int or type(b) != int:
        raise TypeError("Error: Tipo de dato no válido")
    else:
        return a*b

def division(a,b):
    if type(a) != int or type(b) != int:
        raise TypeError("Error: Tipo de dato no válido")
    elif b == 0:
        raise ZeroDivisionError("Error: No es posible dividir entre cero")
    else:
        return a/b

```

## Ejercicio 2:

**Código:**
```

import sys

def contador():
        try:
            fichero = open("contador.txt", "r")
            contador = int(fichero.read())
            fichero.close()
        except:
            contador = 0
        if len(sys.argv) == 2:
            if sys.argv[1] == "inc":
                contador += 1
            elif sys.argv[1] == "dec":
                contador -= 1
        print(contador)    
        fichero = open("contador.txt", "w")
        fichero.write(str(contador))
        fichero.close()


```

## Ejercicio 3:

**Código:**
```
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


```

## Ejercicio 4:

**Código:**
```

import datetime

def reloj():
    hora = datetime.datetime.now()
    print(hora.strftime("%H:%M:%S"))



import time
import os
from reloj import reloj
import reloj

def main():
    while True:
        reloj.reloj()
        time.sleep(1)
        os.system('cls')
        os.system('clear')

```