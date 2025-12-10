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

NEWS_URL = "https://newsapi.org/v2/everything"
NEWS_PARAMS = {
    "apikey": os.getenv("NEWS_API_KEY"),
    "q": FULL_STOCK,
    "language": 'en',
    "from": pre_yesterday,
    "to": yesterday,
    "sort_by": 'relevancy',
    "qInTitle": FULL_STOCK,
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


if percent_change(pre_yesterday_close, yesterday_close) > 5:
    response = requests.get(NEWS_URL, params=NEWS_PARAMS)
    response.raise_for_status()
    response_json = response.json()["articles"][:2]

messages = [for response_json in response_json]




## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
