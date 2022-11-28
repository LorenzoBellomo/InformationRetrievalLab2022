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
mapping = {
    "properties":{
        "maintext": {
            "type": "text",
            "analyzer": "english"
        },
        "source": {
            "type": "text",
            "analyzer": "whitespace"
        },
        "pub-date": {
            "type": "date",
             "format": "yyyy-MM-dd"
        }
    }        
}
es.indices.put_mapping(index=INDEX_NAME, body=mapping)

import os

dir = "../../texts"
for filename in os.listdir(dir):
    f = os.path.join(dir, filename)
    with open(f, 'r') as article_file:
        text = json.load(article_file)
        document = {"maintext": text["maintext"], "source": text["source"], "pub-date": text["date"]}
        es.index(index=INDEX_NAME, body=document)
