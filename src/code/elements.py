class Docs:
    def __init__(self, name, text):
        self.name = name
        self.words = []
        self.count = []
        self.max = 0
        self.text = text

    def add(self, word):
        if not word in self.words:
            self.words.append(word)
            self.count.append(0)
        index = self.words.index(word)
        self.count[index] += 1
        self.max = max(self.max, self.count[index])

    def to_dict(self):
        return {
            'name': self.name,
            'text': self.text
        }

class Words:
    def __init__(self, word, docs):
        self.word = word
        self.docs = docs

    def to_dict(self):
        return {
            'word': self.word,
            'docs': [ {
                'id': doc[0],
                'tf-idf': doc[1]
            } for doc in self.docs]
        }