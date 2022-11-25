
import requests
import json

SWAT_ENDPOINT = "https://swat.d4science.org/salience"
LANG = "en"

with open("../../config.json", 'r') as json_file:
    config = json.load(json_file)
    KEY = config['d4science_KEY']

with open("../../Leonardo.txt", 'r') as long_file:
    text = long_file.read()

def query_swat(title, content):
    document = json.dumps({"title": title, "content": content})
    r = requests.post(SWAT_ENDPOINT, data = document, params={'gcube-token': KEY})
    if r.status_code != 200:
        raise Exception("Error on article titled: {}\n{}".format(title, r.text))
    return r.json()["annotations"]

print(query_swat("Leonardo da Vinci", text))