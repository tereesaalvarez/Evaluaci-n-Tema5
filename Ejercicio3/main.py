from gestor import *

if __name__ == "__main__":
    gestor = Gestor()
    gestor.agregarPersonaje('Caballero', 4, 2, 4, 2)
    gestor.agregarPersonaje('Guerrero', 2, 4, 2, 4)
    gestor.agregarPersonaje('Arquero', 2, 4, 1, 8)
    gestor.mostrarPersonajes()
    gestor.borrarPersonaje('Guerrero')
    gestor.mostrarPersonajes()
    gestor.guardarPersonajes()
    gestor.cargarPersonajes()


    
