from criptos.models import CriptoValorModel
from criptos.view import CriptoValorView
from criptos.errors import APIError

vista = CriptoValorView() #porque en criptoValorView validamos el origen y el destino, temos que llamarla 
vista.pedir()

cmv = CriptoValorModel(vista.origen, vista.destino)
try: 
    cmv.obtener_tasa()
    print(cmv.tasa)
except APIError:
    print("No se puede calcular la tasa")