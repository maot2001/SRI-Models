import json
import os
import query_lsi
import utils
Corpus_Len=1400

def precision(relevants, recovered):
    if len(recovered) == 0:
        return 0
    return len(set(relevants).intersection(set(recovered))) / len(recovered)

def recall(relevants, recovered):
    if len(relevants) == 0:
        return 0
    return len(set(relevants).intersection(set(recovered))) / len(relevants)


def f_measure(prec, rec):
    if prec + rec == 0:
        return 0
    return (2 * prec * rec) / (prec + rec)

def r_precision(relevants, recovered):
    r = len(relevants)
    return len(set(recovered).intersection(relevants)) / r

def failure_ratio(relevants, recovered):
    docs_irrelevant_recovered = set(recovered) - set(relevants)
    docs_irrelevant_total = Corpus_Len - len(relevants)
    return len(docs_irrelevant_recovered) / docs_irrelevant_total

def metrics():
    """
    Automatic queries and metrics collection
    """
    data_words = utils.json_to_words()
    data_docs = utils.json_to_doc()

    route = os.getcwd()
    route = os.path.join(route, 'data')

    with open(os.path.join(route, 'queries.json'), "r") as file:
        queries=json.load(file)

    for i in range(1, len(queries) + 1):
        query = queries[f'{i}']
        result = query_lsi.query_lsi(query, data_words, data_docs)
        print(Evaluations(result, i))


def Evaluations(docs, index):
    """
    Evaluates the results with the expected results
    
    Args:
    list(Docs): Docs to compare
    str: query

    Return:
    dict(metrics): Values of metrics

    """
    docs_id=[tuple[1] for tuple in docs]

    route = os.getcwd()
    route = os.path.join(route, 'data')

    with open(os.path.join(route, 'relevant_doc.json'), "r") as file:
        data=json.load(file)

    query_id=f'{index}'

    if query_id in data:
        relevants=data[query_id]['relevants']
        precision_value = precision(relevants, docs_id)
        recall_value = recall(relevants, docs_id)
        f_value=f_measure(precision_value,recall_value)
        r_precision_value=r_precision(relevants,docs_id)
        failure_value=failure_ratio(relevants,docs_id)
        return {"precision": precision_value,"recall":recall_value,
                "r_precision":r_precision_value,"f_value":f_value,
                "failure_ratio":failure_value}
    return None
