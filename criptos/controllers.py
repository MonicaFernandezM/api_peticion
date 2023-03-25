from criptos.models import CriptoValorModel, APIError
from criptos.view import CriptoValorView

class CriptoValorController():
    def __init__(self):
        self.vista = CriptoValorView()
        self.modelo = CriptoValorModel()

    def ejecutar(self):
        self.vista.pedir()
        self.modelo.origen = self.vista.origen
        self.modelo.destino = self.vista.destino
        try:
            self.modelo.obtener_tasa()
            self.vista.mostrar(self.modelo.tasa)
        except APIError as e:
            self.vista.mostrar_error(e.args[0]) #porque esta en forma de tupla en models
