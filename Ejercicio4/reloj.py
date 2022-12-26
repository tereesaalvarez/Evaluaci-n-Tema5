import datetime

def reloj():
    hora = datetime.datetime.now()
    print(hora.strftime("%H:%M:%S"))



