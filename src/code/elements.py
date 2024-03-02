class Docs:
    def __init__(self, name, text):
        self.name = name
        self.text = text

    def to_dict(self):
        return {
            'name': self.name,
            'text': self.text
        }

class Words:
    def __init__(self, word, docs):
        self.word = word
        self.docs = docs
        self.idf = 0

    def to_dict(self):
        return {
            'word': self.word,
            'idf' : self.idf,
            'docs': self.docs
        }