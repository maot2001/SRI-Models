import json
import os
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
    documentos_irrelevantes_recuperados = set(recovered) - set(relevants)
    documentos_irrelevantes_totales = Corpus_Len - len(relevants)
    return len(documentos_irrelevantes_recuperados) / documentos_irrelevantes_totales



def Evaluations(docs, query):
    """
    Evaluates the results with the expected results
    
    Args:
    list(Docs): Docs to compare
    str: query

    Return:
    dict(metrics): Values of metrics

    """
    docs_id=[tupla[1] for tupla in docs]
    route = os.getcwd()
    route = os.path.join(route, 'data')

    with open(os.path.join(route, 'relevant_doc.json'), "r") as file:
        data=json.load(file)

    with open(os.path.join(route, 'queries.json'), "r") as file:
        queries=json.load(file)

    query_id=''

    for id,name in queries.items():
        if name==query : 
            query_id=id
            break
    
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
# Example of use
print(Evaluations([("name","5"),("name","7"),("name","9"),("name","91"),("name","19"),("name","144"),("name","181")],"what problems of heat conduction in composite slabs have been solved so\nfar ."))
