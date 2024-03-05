from token_docs import create_structure, Words
from utils import *
import numpy as np
import re
import spacy
import nltk
import itertools
from sympy import sympify,simplify,  to_dnf, Not, And, Or, logic

data_words = json_to_words()
data_docs = json_to_doc()
nlp = spacy.load("en_core_web_sm")

def process_query(query):
  processed_query = ""
    for i in query:
        if i == "and":
            processed_query=processed_query + " & "
        elif i == "or":
            processed_query =processed_query + " | "
        elif i=="not":
            processed_query =processed_query + " ~ "
        else:
            processed_query = processed_query + " " + i
    return processed_query

def query_to_dnf(query):
    """Replace each boolean operator in natural language for a boolean operator in matematician language and then converts that to sympify expression 

    Args:
        query (str): Natural language query

    Returns:
        sympify: DNF query
    """
    query = [token.lemma_.lower() for token in nlp(query) if token.is_alpha or token.text=='(' or token.text ==')']
    try:
        processed_query = process_query(query)
        query_expr = sympify(processed_query, evaluate=False)
    except:
        new_query = add_and_between_words(query)
        processed_query = process_query(new_query)
        query_expr = simplify(processed_query, evaluate=False)
    query_dnf = to_dnf(query_expr, simplify=True, force=True)

    return query_dnf


def get_clean_query(query_dnf):
    """Process the dnf query

    Args:
        query_dnf (sympify): DNF query :)

    Returns:
        list<list<str>>: list with all conjuntive clauses
    """
    #return a tuple, if tup[0]=='' then is a single word else is an expression between parenthesis
    tup_query = re.findall(r'\((.*?)\)|(\w+)', str(query_dnf))
    conjuntive_query = [re.split(r'\s*&\s*', clause[0]) if clause[0] else [clause[1]] for clause in tup_query]
    return conjuntive_query

def get_matching_docs(query, data_words):
    """Returns the ids of matching documents

    Args:
        query (str): query
        data_words (list<words>): list of all words
    """
    matching_docs = []
    conjuntive_query = get_clean_query(query_to_dnf(query))
    all_docs = []
    for clause in conjuntive_query:
        for item in clause:
            word = next(w for w in data_words if w.word == item)
            doc_keys = word.docs.keys()
            matching_docs.append(list(map(int, doc_keys)))
            if item.startswith('~'):
                word = next(w for w in data_words if w.word == item)
                doc_keys = word.docs.keys()
                set_docs = set(range(1, 1401))
                docs = list(map(int, doc_keys))
                difference_set = set_docs.difference(docs)
                matching_docs.append(list(difference_set))

        intersection_docs = set.intersection(*map(set, matching_docs))
        all_docs.append(list(intersection_docs))
    union_docs = set().union(*all_docs)
    return (list(union_docs))
    
def get_docs_from_ids(query, data_words, data_docs):
    """Return the documents from id(id)

    Args:
        ids (list<int>): Each document id
        data_docs (_type_): All documents

    Returns:
        list<str>: documents that match with the given ids
    """
    ids = get_matching_docs(query, data_words)
    names = []
    true_ids = []
    for id in ids:
        names.append(data_docs[id].name)
        true_ids.append(data_docs[id].id)
    return (names, true_ids)



