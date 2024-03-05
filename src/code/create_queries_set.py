import ir_datasets
import json
import os
dataset = ir_datasets.load("cranfield")

consultas_info = {}
consultas_ids_nombres = {}

for qrel in dataset.qrels_iter():
    query_id = qrel.query_id
    doc_id = qrel.doc_id
    relevance = qrel.relevance

    if query_id not in consultas_info:
        consultas_info[query_id] = {"name": None, "relevants": []}
    if relevance > 0:
        consultas_info[query_id]["relevants"].append(doc_id)

count=0
for query in dataset.queries_iter():
    count+=1
    query_nombre = query.text

    consultas_info[str(count)]["name"] = query_nombre
    consultas_ids_nombres[str(count)] = query_nombre

route = os.getcwd()
route = os.path.join(route, 'data')

with open(os.path.join(route, 'relevant_doc.json'), "w") as f:
    json.dump(consultas_info, f, indent=4)

with open(os.path.join(route, 'queries.json'), "w") as f:
    json.dump(consultas_ids_nombres, f, indent=4)

