import json
from elasticsearch import Elasticsearch

with open("../../config.json", 'r') as config_file:
    config = json.load(config_file)
    INDEX_PORT = config['port']
    INDEX_HOST = config['host']
    INDEX_USER = config['username']
    INDEX_PASS = config['psw']
    INDEX_NAME = config['surname']
INDEX_URL = 'http://{}:{}/'.format(INDEX_HOST, INDEX_PORT)

es = Elasticsearch(INDEX_URL, http_auth=(INDEX_USER, INDEX_PASS))

input_query = input('Insert a query: ').strip()
query_body = {'query': {'match': {'line_content': input_query}}}

res = es.search(index=INDEX_NAME, body=query_body)
for hit in res['hits']['hits']:
    print('score: {} - line: {}'.format(hit['_score'], hit['_source']['line_content']))
