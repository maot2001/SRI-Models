import ir_datasets
from operator import attrgetter
import json
from token_docs import create_structure
from utils import tf_idf_calculate
from elements import Docs
import os

def Charge_database():
  dataset = ir_datasets.load("cranfield")
  documents = [doc.text for doc in dataset.docs_iter()]
  max_vals, words = create_structure(documents)

  words = sorted(words, key=attrgetter('word'))

  for word in words:
    tf_idf_calculate(word, max_vals, len(word.docs), len(documents))

  route = os.getcwd()
  route = os.path.join(route, 'data')

  words_json = json.dumps([word.to_dict() for word in words], indent=4, ensure_ascii=False)
  with open(os.path.join(route, 'words.json'), 'w', encoding='utf-8') as archivo_json:
    archivo_json.write(words_json)

  docs = [Docs(doc.title, doc.text, doc.doc_id) for doc in dataset.docs_iter()]
  docs_json = json.dumps([doc.to_dict() for doc in docs], indent=4, ensure_ascii=False)
  with open(os.path.join(route, 'docs.json'), 'w', encoding='utf-8') as archivo_json:
    archivo_json.write(docs_json)

def Charge_queries():
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


Charge_database()
Charge_queries()
