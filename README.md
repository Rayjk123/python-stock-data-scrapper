# Python Stock Data Scrapper
This python app scrapes the Nasdaq and MarketWatch websites to retrieve Stock Data. The app grabs data with urlopen, 
parses with Beautiful Soup, and creates an endpoint with Flask-API. The app is hosted on Google App Engine, so feel free
to hit the endpoint and use it personally. Use responsibly please!

There is one endpoint to get general stock data currently.

`GET https://panda-life-projects.appspot.com/stock_symbol/{stock_symbol}`

Examples Response
```
{
  "stockName": "Apple Inc.",
  "stockPrice": "$197.10",
  "priceChange": "$-0.08",
  "percentChange": "-0.04%",
  "keyInfo": {
    "bestBid": "N/A",
    "bestAsk": "N/A",
    "oneYearTarget": "222.5",
    "todaysHigh": "$198.85",
    "todaysLow": "$198.85",
    "shareVolume": "41,183,192",
    "fiftyDayAverageDailyVolume": "28,726,267",
    "previousClose": "$199.95",
    "fiftyTwoWeekHigh": "$233.47",
    "marketCap": "907,239,968,500",
    "PERatio": "16.58",
    "forwardPEOneYear": "17.48",
    "earningsPerShare": "$11.89",
    "annualizedDividend": "$3.08",
    "exDividendDate": "5/10/2019",
    "dividendPaymentDate": "5/16/2019",
    "currentYield": "1.44%",
    "beta": "1.02"
  }
}
```

No license or anything. Use it as you will.
