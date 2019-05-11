import json
from flask_api import status


def successful_response(data):
    return data


def error_response(failure_message):
    response = {
        "error": failure_message
    }

    json_data = json.dumps(response, ensure_ascii=False)
    return json_data, status.HTTP_500_INTERNAL_SERVER_ERROR


def not_found_response(failure_message):
    response = {
        "error": failure_message
    }

    json_data = json.dumps(response, ensure_ascii=False)
    return json_data, status.HTTP_404_NOT_FOUND
