from . import MONEDAS


class CriptoValorView():
    def __init__(self):
        self.origen = ""
        self.destino = ""


    def pedir(self):
        origen = input("Moneda de origen: ")
        while origen not in MONEDAS:
            print('La moneda debe ser de las siguientes: ')
            print(",".join(MONEDAS))
            origen = input("Moneda de origen: ")   

        self.origen = origen
                 
        destino = input("Moneda a convertir: ")
        while destino not in MONEDAS:
            print('La moneda debe ser de las siguientes: ')
            print(",".join(MONEDAS))
            destino = input("Moneda a convertir: ") 

        self.destino = destino
