import requests
from criptos import API_KEY, URL_TASA_ESPECIFICA #el punto sustituye la palabra criptos porque esta en el mismo fichero 
from criptos.errors import APIError

class CriptoValorModel:
    def __init__(self, origen: str, destino: str):
        self.origen = origen 
        self.destino = destino 

        self.tasa = 0.0

    def obtener_tasa(self):
        self.respuesta = requests.get(URL_TASA_ESPECIFICA.format(self.origen, self.destino, API_KEY))

        if self.respuesta.status_code != 200:
            raise APIError(self.respuesta.json()["error"]) #nos devuelve el error que lanza el json 
            

        self.tasa = round(self.respuesta.json()["rate"], 2)

