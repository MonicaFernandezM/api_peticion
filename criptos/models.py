import requests
from criptos import URL_TASA_ESPECIFICA #el punto sustituye la palabra criptos porque esta en el mismo fichero 
from criptos.errors import APIError
from criptos.config import API_KEY

class CriptoValorModel:
    def __init__(self, origen = "", destino = ""):
        self.origen = origen 
        self.destino = destino 

        self.tasa = 0.0

    def obtener_tasa(self):
        respuesta = requests.get(URL_TASA_ESPECIFICA.format(self.origen, self.destino, API_KEY))

        if respuesta.status_code != 200:
            #raise APIError(respuesta.status_code, respuesta.json()["error"]) #nos devuelve el error que lanza el json 
            raise APIError(respuesta.status_code)

        self.tasa = round(respuesta.json()["rate"], 2)

