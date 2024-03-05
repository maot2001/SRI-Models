from math import log, sqrt
import json
import os
from elements import Words, Docs

def idf(appear, docs):
  n = appear if appear != 0 else 0.1
  return log(docs/n)

def tf_idf_calculate(word, text_freq, appear, docs_len, idf_val = -1):
  if idf_val == -1:
    idf_val = idf(appear, docs_len)
    word.idf = idf_val
  for doc in word.docs:
    tf_val = word.docs[doc] / text_freq[doc]
    word.docs[doc] = idf_val * tf_val

def sum_mult_vector(query, doc):
  return sum(query[i] * doc[i] for i in range(len(query)))

def sum_dist_vector(vector):
  return sqrt(sum(vector[i]**2 for i in range(len(vector))))

def binary_search(word, data):
  left, right = 0, len(data) - 1

  while left <= right:
    mid = left + (right - left) // 2

    if data[mid].word == word:
      return data[mid]
    elif data[mid].word < word:
      left = mid + 1
    else:
      right = mid - 1

  return -1

def json_to_words():
    
    route = os.getcwd()
    route = os.path.join(route, 'data')
    route = os.path.join(route, 'words.json')

    with open(route, 'r', encoding='utf-8') as json_file:
        content = json_file.read()

    content = json.loads(content)

    words = []

    for word in content:
        aux_word = Words(word['word'], word['docs'])
        aux_word.idf = word.get('idf', 0)
        words.append(aux_word)

    return words

def json_to_doc(): 
    route = os.getcwd()
    route = os.path.join(route, 'data')
    route = os.path.join(route, 'docs.json')

    with open(route, 'r', encoding='utf-8') as json_file:
        content = json_file.read()

    content = json.loads(content)

    docs = []

    for doc in content:
        aux_doc = Docs(doc['name'], doc['text'], doc['id'])
        docs.append(aux_doc)

    return docs  

#this may not use it
def add_and_between_words(phrase):
    words = phrase.split()
    new_phrase = []
    for i in range(len(words) - 1):
        new_phrase.append(words[i])
        if words[i] != "and" and words[i] != "or" and words[i]!="not" and words[i + 1] != "and" and words[i + 1] != "or":
            new_phrase.append("and")
    new_phrase.append(words[-1])
    return " ".join(new_phrase)

