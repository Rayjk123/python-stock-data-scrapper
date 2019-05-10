import json

def successful_response(data):
    response = {
        "status": "success",
        "data": data
    }

    return json.dumps(response, ensure_ascii=False)