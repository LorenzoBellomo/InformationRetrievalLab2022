import requests
import json

ENDPOINT_RELATEDNESS = "https://tagme.d4science.org/tagme/rel"
LANG = "en"

with open("../../config.json", 'r') as json_file:
    config = json.load(json_file)
    KEY = config['d4science_KEY']

def query_relatedness(e1, e2):
    tt = e1.replace(" ", "_") + " " + e2.replace(" ", "_")
    payload = {"tt": tt, "gcube-token": KEY, "lang": LANG}

    r = requests.post(ENDPOINT_RELATEDNESS, payload)
    if r.status_code != 200:
        raise Exception("Error on relatedness computation: {}\n{}".format(tt, r.text))
    return r.json()

first = query_relatedness("Biology", "Biotechnology")
second = query_relatedness("Barack Obama", "Biotechnology")
print(first)
print(second)