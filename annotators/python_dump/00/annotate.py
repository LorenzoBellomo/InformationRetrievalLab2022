import requests
import json

TAGME_ENDPOINT = "https://tagme.d4science.org/tagme/tag"

LANG = "en"

with open("../../config.json", 'r') as json_file:
    config = json.load(json_file)
    KEY = config['d4science_KEY']

def query_tagme(text):
    payload = {"text": text, "gcube-token": KEY, "lang": LANG}
    r = requests.post(TAGME_ENDPOINT, payload)
    if r.status_code != 200:
        raise Exception("Error on text: {}\n{}".format(text, r.text))
    return r.json()


resp = query_tagme("Italy will not be competing in the 2022 world cup")
print(resp)
