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

source = input("Insert a news source: ").strip()
terms = input("Insert text terms: ").strip()
query_body = {
    "query": {
        "bool": {
            "should": [{"match": {"maintext": terms}}, {"match": {"source": source}}],
            "minimum_should_match": 1,
            "must": [{"range": {"pub-date": {"gt":"2022-01-01"}}}]
        }      
    }        
}

res = es.search(index=INDEX_NAME, body=query_body)
print ("Found {} results.".format(res['hits']['total']['value']))
for hit in res['hits']['hits']:
    print ("score: {} source: {}".format(hit["_score"], hit["_source"]["source"]))
    print ("body: {}".format(hit["_source"]["maintext"])[:100])
