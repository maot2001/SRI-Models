import ir_datasets
from operator import attrgetter
import json
from token_docs import create_structure
from utils import tf_idf_calculate
from elements import Docs
import os

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

docs = [Docs(doc.title, doc.text) for doc in dataset.docs_iter()]
docs_json = json.dumps([doc.to_dict() for doc in docs], indent=4, ensure_ascii=False)
with open(os.path.join(route, 'docs.json'), 'w', encoding='utf-8') as archivo_json:
    archivo_json.write(docs_json)