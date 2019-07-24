class Word:
    def __init__(self, text, part):
        self.text = text
        self.part = part

class Sentence:
    def __init__(self, content):
        self.content = content


    def show(self):
        sent = ''
        for i in self.content:
            sent = sent + list_words[i].text + ' '
        return sent

 
    def show_parts(self):
        parts = [list_words[i].part for i in self.content]
        parts = set(parts)
        parts = list(parts)
        return parts

