from token_docs import create_structure, Words
from utils import *
import numpy as np

def query_tf_idf(query, data_words, data_docs):
    all, threshold = recive_query_tf_idf(query, data_words, len(data_docs))

    all = sorted(all, key=lambda x: x[1], reverse=True)
    result = []
    for doc in all:
        if doc[1] < max(.2, 1/threshold - .1): break
        result.append(data_docs[doc[0]]['name'])

    return result

def recive_query_tf_idf(query, data_words, docs):
    max_vals, words = create_structure([query])
    query_vector, result, found_words = [], [], []

    for word in words:
        aux = binary_search(word.word, data_words)
        if aux == -1: continue
        word.idf = aux['idf']
        tf_idf_calculate(word, max_vals, 1, 1, word.idf)
        query_vector.append(word.docs[0])
        found_words.append(aux)

    matrix = np.zeros((docs, len(found_words)))
    docs = [False] * (docs)

    for i in range(len(found_words)):
        for doc in found_words[i]['docs']:
            matrix[int(doc)][i] = found_words[i]['docs'][doc]
            docs[int(doc)] = True

    for i in range(len(docs)):
        if docs[i]:
            doc_vector = [val for val in matrix[i]]
            compare = sum_mult_vector(query_vector, doc_vector)/ (sum_dist_vector(query_vector) * sum_dist_vector(doc_vector))
            result.append((i, compare))

    return result, len(found_words)
