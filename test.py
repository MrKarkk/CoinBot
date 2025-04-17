import requests 

response = requests.get(
    "https://min-api.cryptocompare.com/data/price",
    params={"fsym":"USD","tsyms":"RUB,JPY,EUR"},
    headers={"Content-type":"application/json; charset=UTF-8"}
)

json_response = response.json()

print(json_response['RUB'])