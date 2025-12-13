import requests
URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": "569dc0e8bc074c5798560ea81c36b89e",
}
parameters = {
    "symbol": "BTC",
    "convert": "USD",
}
response = requests.request("GET", URL, headers=headers, params=parameters)
response.raise_for_status()
print(response.json())