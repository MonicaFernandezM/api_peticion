from criptos.models import CriptoValorModel
from criptos.view import CriptoValorView

class CriptoValorController():
    def __init__(self):
        self.vista = CriptoValorView()
        self.modelo = CriptoValorModel()

    def ejecutar(self):
        self.vista.pedir()
        self.modelo.origen = self.vista.origen
        self.modelo.destino = self.vista.destino
        #try, except para que utilice la vista de que se ponte un error en la APIKe
        self.modelo.obtener_tasa()
        self.vista.mostrar(self.modelo.tasa)