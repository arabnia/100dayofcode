import requests
from dotenv import load_dotenv
import os
import datetime
STOCK = "ETH"
FULL_STOCK = "Ethereum"
URL = "https://www.alphavantage.co/query"

load_dotenv()
historical = {
    "symbol": STOCK,
    "function": "DIGITAL_CURRENCY_DAILY",
    "market": "USDT",
    "apikey": os.getenv("ALPHAVANTAGE_API_KEY"),
}

now = datetime.datetime.now(datetime.UTC)
yesterday = (now - datetime.timedelta(days=0)).isoformat().split("T")[0]
pre_yesterday = (now - datetime.timedelta(days=2)).isoformat().split("T")[0]

response = requests.get(URL, params=historical)
response.raise_for_status()
response_json = response.json()
yesterday_close = float(response_json["Time Series (Digital Currency Daily)"][yesterday]["4. close"])
pre_yesterday_close = float(response_json["Time Series (Digital Currency Daily)"][pre_yesterday]["4. close"])
up_down = None

def percent_change(old: float, new: float) -> float:
    global up_down
    if (new - old) < 0:
        up_down = "🔼"
    else:
        up_down = "🔽"
    return abs((new - old) / old * 100)

NEWS_URL = "https://newsapi.org/v2/everything"
NEWS_PARAMS = {
    "apikey": os.getenv("NEWS_API_KEY"),
    "language": 'en',
    "from": pre_yesterday,
    "to": yesterday,
    "sort_by": 'relevancy',
    "qInTitle": FULL_STOCK,
}

if percent_change(pre_yesterday_close, yesterday_close) > 5:
    response = requests.get(NEWS_URL, params=NEWS_PARAMS)
    response.raise_for_status()
    response_json = response.json()["articles"][:2]

messages = [f"Headline: {item["title"]} {STOCK}{up_down}\n{item["description"]}" for item in response_json]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number

