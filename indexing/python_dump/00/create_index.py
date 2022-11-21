from elasticsearch import Elasticsearch
import json

with open("../../config.json", 'r') as config_file:
    config = json.load(config_file)
    INDEX_PORT = config['port']
    INDEX_HOST = config['host']
    INDEX_USER = config['username']
    INDEX_PASS = config['psw']
    INDEX_NAME = config['surname']
INDEX_URL = 'http://{}:{}/'.format(INDEX_HOST, INDEX_PORT)

def index_create():
    es = Elasticsearch(INDEX_URL, http_auth=(INDEX_USER, INDEX_PASS))
    if es.indices.exists(index=INDEX_NAME):
        es.indices.delete(index=INDEX_NAME)
    es.indices.create(index=INDEX_NAME)
    return es

es = index_create()
for i in range(0, 3):
    line = input('Write some text: ')
    document = {'line_content': line.strip()}
    es.index(index=INDEX_NAME, body=document)
