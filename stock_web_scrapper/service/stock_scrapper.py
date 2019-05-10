import stock_web_scrapper.util.data_grabber as grabber
import stock_web_scrapper.util.parser as parser
import stock_web_scrapper.util.response_formatter as response
import json


def stock_api_response(stock_symbol):
    nasdaq_html = grabber.grab_nasdaq_stock_html(stock_symbol)
    market_watch_html = grabber.grab_market_watch_stock_html(stock_symbol)

    if not parser.validate_symbol(nasdaq_html, market_watch_html):
        return "Invalid Stock Symbol was passed"

    key_stock_info = parser.parse_key_stock_info(nasdaq_html)
    basic_stock_info = parser.parse_basic_stock_info(market_watch_html)

    stock_data = aggregate_stock_info(key_stock_info, basic_stock_info)

    return response.successful_response(stock_data)


def aggregate_stock_info(key_stock_info, basic_stock_info):
    basic_stock_info["keyInfo"] = key_stock_info
    return json.dumps(basic_stock_info, ensure_ascii=False)