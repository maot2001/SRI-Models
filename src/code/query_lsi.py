from token_docs import create_structure
from utils import *
import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
from math import log2

def query_lsi(query, data_words, data_docs):
    """Responsible for organizing the resulting data and returning it in the desired format

    Args:
        query (str): User query
        data_words (list(dict)): Database words
        data_docs (list(dict)): Database docs

    Returns:
        list((str, int)): Title and id of the document
    """

    # Resolve the query
    all = recive_query_lsi(query, data_words, len(data_docs))

    # Organize and return
    all = sorted(all, key=lambda x: x[1], reverse=True)
    return [(data_docs[doc[0]]['name'], data_docs[doc[0]]['id']) for doc in all]

def recive_query_lsi(query, data_words, docs):
    """Resolve the query

    Args:
        query (str): User query
        data_words (list(dict)): Database words
        docs (list(dict)): Count of database docs

    Returns:
        list((int, float)): Index of the document with its similarity value
    """

    # Initializing data
    max_vals, words = create_structure([query])
    query_vector, result, found_words = [], [], []

    # Finding word in the word database
    for word in words:
        aux = binary_search(word.word, data_words)
        if aux == -1: continue
        word.idf = aux['idf']
        tf_idf_calculate(word, max_vals, 1, 1, word.idf)
        query_vector.append(word.docs[0])
        found_words.append(aux)

    # Indexing tf-idf values
    matrix = np.zeros((docs, len(found_words)))
    for i in range(len(found_words)):
        for doc in found_words[i]['docs']:
            matrix[int(doc)][i] = found_words[i]['docs'][doc]

    # Create and train an initial TruncatedSVD model of dimension equal to the number of words
    lsa_model = TruncatedSVD(n_components=len(found_words))
    lsa_model.fit(matrix)

    # Obtain the singular values and calculate the explained variance
    singular_values = lsa_model.singular_values_
    explained_variance = (singular_values ** 2) / np.sum(singular_values**2)

    # Calculate the number of dimensions necessary to reach or exceed the explained variance threshold
    umbral_varianza = 0.95
    n_dimensiones = np.argmax(np.cumsum(explained_variance) >= umbral_varianza) + 1
    n_dimensiones = n_dimensiones if n_dimensiones <= len(found_words) else len(found_words)

    # Use the created model to re-size the data
    lsa_model = TruncatedSVD(n_components=n_dimensiones)
    lsa_topic_matrix = lsa_model.fit_transform(matrix)
    lsa_topic_query = lsa_model.transform([query_vector])

    # Calculate cosine similarity
    similarity = cosine_similarity(lsa_topic_query, lsa_topic_matrix)

    # Filter items based on threshold
    for i in range(len(similarity[0])):
        if similarity[0][i] < max(.2, 1/len(found_words) - .1): continue
        result.append((i, similarity[0][i]))

    return result