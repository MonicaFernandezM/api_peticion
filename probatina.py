import requests

respuesta = requests.get("https://rest.coinapi.io/v1/exchangerate/BTC?apikey=F3827B24-7901-4FBE-93B5-6C8587D461DA")


print(respuesta.status_code)

data = respuesta.json()
print(data["rates"][3])

