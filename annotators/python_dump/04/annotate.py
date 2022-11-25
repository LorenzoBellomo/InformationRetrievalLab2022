import requests
import json

REL_ENDPOINT = "https://rel-entity-linker.d4science.org/"
LANG = "en"

with open("../../config.json", 'r') as json_file:
    config = json.load(json_file)
    KEY = config['d4science_KEY']

with open("../../Leonardo.txt", 'r') as long_file:
    text = long_file.read()

def query_rel(text):
    document = json.dumps({"text": text, "spans": []})
    headers={'gcube-token': KEY, 'Content-Type': 'application/json'}
    r = requests.post(REL_ENDPOINT, data=document, headers=headers)
    if r.status_code != 200:
        raise Exception("Error on text: {}\n{}".format(text, r.text))
    return r.json()

print(query_rel(text))