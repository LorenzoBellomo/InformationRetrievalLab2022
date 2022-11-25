import requests
import json

TAGME_ENDPOINT = "https://tagme.d4science.org/tagme/tag"
LANG = "en"

with open("../../config.json", 'r') as json_file:
    config = json.load(json_file)
    KEY = config['d4science_KEY']

with open("../../Leonardo.txt", 'r') as long_file:
    text = long_file.read()

def query_tagme(text, long_text=False):
    payload = {"text": text, "gcube-token": KEY, "lang": LANG}
    if long_text:
        payload["long_text"] = 5
    r = requests.post(TAGME_ENDPOINT, payload)
    if r.status_code != 200:
        raise Exception("Error on text: {}\n{}".format(text, r.text))
    return r.json()

def get_tagme_entities(tagme_response, min_rho=0.3):
    ann = tagme_response["annotations"]
    ann = [a for a in ann if a["rho"] > min_rho]
    return [a["title"] for a in ann if "title" in a]

resp = query_tagme(text, long_text=True)
print(get_tagme_entities(resp))