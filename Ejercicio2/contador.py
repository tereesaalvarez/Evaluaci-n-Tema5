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

