import requests
import urllib
import json
from requests_html import HTMLSession
from get_data import *

def get_source(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        return response
    except requests.exceptions.RequestException as e:
        print(e)


def get_knowledge_graph(api_key, query):
    endpoint = 'https://kgsearch.googleapis.com/v1/entities:search'
    params = {
        'query': query,
        'limit': 10,
        'indent': True,
        'key': api_key,
    }
    url = endpoint + '?' + urllib.parse.urlencode(params)
    response = get_source(url)
    return json.loads(response.text)


api_key = "AIzaSyAPiTnrakCG5uCTYf1lb-9euDHChPlEVW8"
summaries = get_data('summaries_0')
print(summaries[:10])
knowledge_graph_json = get_knowledge_graph(api_key, "tesla")

for element in knowledge_graph_json['itemListElement']:
    # print(element['result']['name'] + ' (' + str(element['resultScore']) + ')')
    print(element['result'])
