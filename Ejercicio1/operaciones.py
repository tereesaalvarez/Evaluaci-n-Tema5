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





