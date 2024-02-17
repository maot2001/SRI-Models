from math import log10

def idf(appear, docs):
  n = appear if appear != 0 else 0.1
  return log10(docs/n)

def tf(word, doc):
  index = doc.words.index(word.word)
  return doc.count[index] / doc.max if index != -1 else 0

def tf_idf_calculate(word, docs):
  idf_val = idf(len(word.docs), len(docs))
  for doc in word.docs:
    tf_val = tf(word, docs[doc[0]])
    doc[1] = idf_val * tf_val