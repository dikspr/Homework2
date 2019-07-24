# 1. Создайте новые классы Noun (существительное) и Verb (глагол).
# 2. Настройте наследование новых классов от класса Word.
# 3. Добавьте в новые классы свойство grammar («Грамматические характеристики»).
# Для класса Noun укажите значение по умолчанию «сущ» (сокращение от существительное),
# а для Verb — «гл» (сокращение от глагол).
# Вспомните про инкапсуляцию и сделайте свойство grammar защищённым.
# 4. Исправьте класс Word, чтобы указанный ниже код не вызывал ошибки.
# Подсказка: теперь в нём не нужно хранить части речи.
# words = []
# words.append(Noun("собака"))
# words.append(Verb("ела"))
# words.append(Noun("колбасу"))
# words.append(Noun("кот"))
# По желанию добавьте ещё несколько глаголов и существительных.
# 5. Протестируйте работу старого метода show класса Sentence. Если предложения не формируются, исправьте ошибки.
# 6. Допишите в классы Noun и Verb метод part. Данный метод должен возвращать строку с полным названием части речи.
# 7. Протестируйте работу метода show_part класса Sentence. Исправьте ошибки, чтобы метод работал.
# Подсказка: ранее part был свойством класса Word, а теперь это метод классов Noun и Verb.

# перенес класс и пятого Д/з
class Word:
    def __init__(self, text):
        self.text = text

# Создал два новых класса
class Noun(Word):
    __grammar = 'сущ'

    def part(self):
        if self.__grammar == 'сущ':
            return 'существительное'


class Verb(Word):
    __grammar = 'гл'

    def part(self):
        if self.__grammar == 'гл':
            return 'глагол'

# перенес класс и пятого Д/з и немного поправил метод show_parts
# (добавил скобки после words[i].part, т.к. это теперь метод)
class Sentence:
    def __init__(self, content):
        self.content = content

    def show(self):
        sent = ''
        for i in self.content:
            sent = sent + words[i].text + ' '
        return sent

    def show_parts(self):
        parts = [words[i].part() for i in self.content]
        parts = set(parts)
        parts = list(parts)
        return parts


words = []
words.append(Noun("собака"))
words.append(Verb("ела"))
words.append(Noun("колбасу"))
words.append(Noun("кот"))

prime = Sentence([1, 3])
print(prime.show())
print(prime.show_parts())

