import requests

endpoint = "https://rest.coinapi.io/v1/exchangerate/{}/{}?apikey=F3827B24-7901-4FBE-93B5-6C8587D461DA"

moneda_from = input("Moneda de origen: ")

moneda_to = input("Moneda a conseguir: ")

r = requests.get (endpoint.format(moneda_from, moneda_to)) #estos datos van a entrar en {}{}

print(r.json())
print(r.status_code)
print(round(r.json()["rate"], 2))