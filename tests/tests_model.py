import unittest
from criptos.models import CriptoValorModel, APIError, API_KEY


class TestModel(unittest.TestCase):
    def test_la_moneda_debe_existir(self):
        global API_KEY
        API_KEY = "0"
        cv = CriptoValorModel("BTC", "Lolailos")

        with self.assertRaisesRegex(APIError, "550"):
            cv.obtener_tasa()

    def test_debes_informar_la_api(self):
        cv = CriptoValorModel("BTC", "Lolailos")

        with self.assertRaisesRegex(APIError, "550"):
            cv.obtener_tasa()    