from urllib.request import urlopen as request
import stock_web_scrapper.util.parser as parser


def grab_nasdaq_stock_html(stock_symbol):
    url = 'https://www.nasdaq.com/symbol/' + stock_symbol
    request_result = request(url)
    html = request_result.read()
    request_result.close()

    return html


def grab_market_watch_stock_html(stock_symbol):
    url = 'https://www.marketwatch.com/investing/stock/' + stock_symbol
    request_result = request(url)
    html = request_result.read()
    request_result.close()

    return html


def grab_and_validate_symbol(stock_symbol):
    nasdaq_html = grab_nasdaq_stock_html(stock_symbol)
    market_watch_html = grab_market_watch_stock_html(stock_symbol)

    if not parser.validate_symbol(nasdaq_html, market_watch_html):
        return False

    return True
