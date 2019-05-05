from bs4 import BeautifulSoup as parser
from urllib.request import urlopen as request
import json
from flask_api import FlaskAPI
from flask_api import status

app = FlaskAPI(__name__)


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


def parse_basic_stock_info(stock_html):
    parsed_soup = parser(stock_html, "html.parser")
    stock_name = parsed_soup.find(class_="company__name").string

    stock_price = '$' + parsed_soup.find(class_="intraday__price").find("bg-quote").string

    intraday_data = parsed_soup.find(class_="intraday__change")
    price_change = intraday_data.find(class_="change--point--q").find("bg-quote").string
    percent_change = intraday_data.find(class_="change--percent--q").find("bg-quote").string

    basic_info_dict = {"stock-name": stock_name,
                       "stock-price": stock_price,
                       "price-change": price_change,
                       "percent-change": percent_change}
    return basic_info_dict


def parse_key_stock_info(stock_html):
    parsed_soup = parser(stock_html, "html.parser")
    key_stock_data = parsed_soup.find(class_="row overview-results relativeP")
    key_stock_rows = key_stock_data.find_all(class_="table-row")

    return handle_each_stock_row(key_stock_rows)


def handle_each_stock_row(key_stock_rows):
    stock_data_dict = {}

    for row in key_stock_rows:
        table_cells = row.find_all(class_="table-cell")

        for data in table_cells[0].contents:
            if data.string.strip():
                stock_data_dict[data.string] = table_cells[1].string.strip()

    return stock_data_dict


def aggregate_stock_info(key_stock_info, basic_stock_info):
    basic_stock_info["key-info"] = key_stock_info
    return json.dumps(basic_stock_info, ensure_ascii=False)


def validate_symbol(nasdaq_html, market_watch_html):
    nas_soup = parser(nasdaq_html, "html.parser")
    data = nas_soup.find(class_="row overview-results relativeP")

    market_soup = parser(market_watch_html, "html.parser")
    stock_name = market_soup.find(class_="company__name")

    if stock_name is None or data is None:
        return False

    return True


@app.route('/stocksymbol/<string:stocksymbol>/basic')
def stock_api(stocksymbol):
    nasdaq_html = grab_nasdaq_stock_html(stocksymbol)
    market_watch_html = grab_market_watch_stock_html(stocksymbol)

    if not validate_symbol(nasdaq_html, market_watch_html):
        return "Invalid Stock Symbol was passed"

    key_stock_info = parse_key_stock_info(nasdaq_html)
    basic_stock_info = parse_basic_stock_info(market_watch_html)

    return aggregate_stock_info(key_stock_info, basic_stock_info)


@app.route('/health')
def healthcheck():
    nasdaq_html = grab_nasdaq_stock_html('AAPL')
    market_watch_html = grab_market_watch_stock_html('AAPL')

    if not validate_symbol(nasdaq_html, market_watch_html):
        return status.HTTP_404_NOT_FOUND

    return "Healthy"
