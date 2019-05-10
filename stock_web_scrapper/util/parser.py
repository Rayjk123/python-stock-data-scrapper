from bs4 import BeautifulSoup as parser
import json


def parse_basic_stock_info(stock_html):
    parsed_soup = parser(stock_html, "html.parser")
    stock_name = parsed_soup.find(class_="company__name").string

    stock_price = '$' + parsed_soup.find(class_="intraday__price").find("bg-quote").string

    intraday_data = parsed_soup.find(class_="intraday__change")
    price_change = intraday_data.find(class_="change--point--q").find("bg-quote").string
    percent_change = intraday_data.find(class_="change--percent--q").find("bg-quote").string

    basic_info_dict = {"stockName": stock_name,
                       "stockPrice": stock_price,
                       "priceChange": '$' + price_change,
                       "percentChange": percent_change}
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
        # print(table_cells)

        for data in table_cells[0].contents:
            l = table_cells[1].string.strip()
            print(l)
            print("".join(l.split()))

            if data.string.strip():
                stock_data_dict[data.string] = table_cells[1].string.strip()

    return stock_data_dict


def aggregate_stock_info(key_stock_info, basic_stock_info):
    basic_stock_info["keyInfo"] = key_stock_info
    return json.dumps(basic_stock_info, ensure_ascii=False)


def validate_symbol(nasdaq_html, market_watch_html):
    nas_soup = parser(nasdaq_html, "html.parser")
    data = nas_soup.find(class_="row overview-results relativeP")

    market_soup = parser(market_watch_html, "html.parser")
    stock_name = market_soup.find(class_="company__name")

    if stock_name is None or data is None:
        return False

    return True

