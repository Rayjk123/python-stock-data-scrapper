from flask_api import FlaskAPI
from flask_api import status
from stock_web_scrapper.util.data_grabber import grab_and_validate_symbol
from stock_web_scrapper.service.stock_scrapper import stock_api_response

app = FlaskAPI(__name__)


@app.route('/')
def root():
    return "Hello~ Welcome to Panda Projects :D"


@app.route('/stock_symbol/<string:stock_symbol>')
def stock_api(stock_symbol):
    return stock_api_response(stock_symbol)


@app.route('/health')
def health_check():
    if not grab_and_validate_symbol("AAPL"):
        return status.HTTP_404_NOT_FOUND

    return "Healthy"

stock_api_response('AAPL')