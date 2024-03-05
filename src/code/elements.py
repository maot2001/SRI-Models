class Docs:
    def __init__(self, name, text, id):
        self.name = name.replace(' .', '.').replace('\n', ' ')
        self.text = text.replace(' .\n', '.').replace('.\n', '.').replace('\n', ' ')
        self.id = id

    def to_dict(self):
        return {
            'id': self.id,
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