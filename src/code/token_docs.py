import spacy
from elements import Words
nlp = spacy.load("en_core_web_sm")

def tokenization_spacy(texts):
    """Give de lemmatization of all the words in the texts

    Args:
        texts (list(str)): Docs to process 

    Returns:
        (list(list(str))): For each token in each text, return its lemma
    """
    return [[token.lemma_.lower() for token in nlp(doc) if token.is_alpha and not token.is_stop] 
            for doc in texts]

def create_structure(docs):
  """Generates the word base of the documents to be processed and the maximum frequency of each document  

  Args:
      docs (list(str)): Docs to process

  Returns:
      (list(int)): For each document, the maximum frequency of a word
      (list(Words)): For each word, the documents in which it appears and how often 
  """
  max_vals, words, vocabulary = [], [], []
  tokenized_docs = tokenization_spacy(docs)

  for i in range(len(tokenized_docs)):
    max_val = 0
    for word in tokenized_docs[i]:
      if not word in vocabulary:
        vocabulary.append(word)
        words.append(Words(word, {i: 1}))
        max_val = max(max_val, 1)

      else:
        index = vocabulary.index(word)
        if not i in words[index].docs:
          words[index].docs[i] = 0
        words[index].docs[i] += 1
        max_val = max(max_val, words[index].docs[i])

    max_vals.append(max_val)
    
  return max_vals, words