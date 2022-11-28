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

es = Elasticsearch(INDEX_URL, http_auth=(INDEX_USER, INDEX_PASS))

source = input("Insert a news source: ").strip()
terms = input("Insert text terms: ").strip()
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

article_id = "E9S3voQBPTSChHKmQy_2" #TODO change this with the ID of the article you want to test
res = es.explain(id=article_id, index=INDEX_NAME, body=query_boosted)
print(res['explaination'])