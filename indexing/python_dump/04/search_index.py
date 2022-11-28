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
            "should": [
                {"match": {"maintext": terms}}, 
                {"match": {"source" : source}}
            ]
        }      
    }        
}
query_boosted = {
    "query": {
        "bool": {
            "should": [
                {
                    "match": {
                        "source": {
                            "query": source,
                            "boost": 3
                        }
                    }
                },
                {
                    "match": {
                        "maintext": {
                            "query": terms,
                        }
                    }
                },
            ]
        }
    }
}


for body in [query_body, query_boosted]:
    res = es.search(index=INDEX_NAME, body=body)
    print ("Found {} results.".format(res['hits']['total']['value']))
    for hit in res['hits']['hits']:
        print("=====================================================================")
        print ("score: {} source: {}".format(hit["_score"], hit["_source"]["source"]))
        print ("body: {}".format(hit["_source"]["maintext"])[:100])
    print("\n")