import json
import requests
# import pprint

def api_get_request(url):
    data = requests.get(url).text
    data = json.loads(data)
    return data['topartists']['artist'][0]['name']
