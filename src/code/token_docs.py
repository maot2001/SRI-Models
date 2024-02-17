import ir_datasets
import spacy
from elements import *
from utils import *
from operator import attrgetter
import json

docs = []
words = []

def tokenization_spacy(texts):
  global docs, words
  vocabulary = []
  for i in range(len(texts)):
    now_doc = Docs(i, texts[i])

    for token in nlp(texts[i]):
      if token.is_alpha and not token.is_stop:

        if not token.lemma_ in vocabulary:
          vocabulary.append(token.lemma_)
          words.append(Words(token.lemma_, [[i, 0]]))

        else:
          index = vocabulary.index(token.lemma_)
          if not [i, 0] in words[index].docs:
            words[index].docs.append([i, 0])
        
        now_doc.add(token.lemma_)
    
    docs.append(now_doc)

nlp = spacy.load("en_core_web_sm")
dataset = ir_datasets.load("cranfield")
documents = [doc.text for doc in dataset.docs_iter()]
tokenization_spacy(documents)
words = sorted(words, key=attrgetter('word'))

for word in words:
  tf_idf_calculate(word, docs)

words_json = json.dumps([word.to_dict() for word in words], indent=4, ensure_ascii=False)
with open('words.json', 'w', encoding='utf-8') as archivo_json:
    archivo_json.write(words_json)

docs_json = json.dumps([doc.to_dict() for doc in docs], indent=4, ensure_ascii=False)
with open('docs.json', 'w', encoding='utf-8') as archivo_json:
    archivo_json.write(docs_json)
