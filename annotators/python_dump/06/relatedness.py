import json
from wikipedia2vec import Wikipedia2Vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

ENDPOINT_RELATEDNESS = "https://tagme.d4science.org/tagme/rel"
LANG = "en"

with open("../../config.json", 'r') as json_file:
    config = json.load(json_file)
    KEY = config['d4science_KEY']
    MODEL_FILE = config["path_to_wiki2vec_model"]

wiki2vec = Wikipedia2Vec.load(MODEL_FILE)

def get_entity_vector(e):
    try:
        emb = wiki2vec.get_entity_vector(e)
    except:
        raise Exception("Entity vector {} not found\n".format(e))
    return emb

def similarity(v1, v2):
    x = np.array(v1).reshape(1,-1)
    y = np.array(v2).reshape(1,-1)
    return cosine_similarity(x, y)[0][0]

v1 = ("Barack Obama", get_entity_vector("Barack Obama"))
v2 = ("Biology", get_entity_vector("Biology"))
v3 = ("Biotechnology", get_entity_vector("Biotechnology"))

print(v1)
print("======================================================================")
from itertools import combinations
for x, y in combinations([v1, v2, v3], 2):
    print("Cosine similarity between {} and {} is {:.2f}".format(x[0], y[0], similarity(x[1], y[1])))