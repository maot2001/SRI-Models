import json
import os
from query_tf_idf import query_tf_idf

def charge():
    route = os.path.join(os.getcwd(), "data", "words.json")
    with open(route) as file:
        data_words = json.load(file)

    route = os.path.join(os.getcwd(), "data", "docs.json")
    with open(route) as file:
        data_docs = json.load(file)

    return data_words, data_docs