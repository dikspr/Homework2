# Упражнение продолжает практическую работу из последнего видеоурока.
# Для усовершенствования приложения разберитесь, как можно реализовать получение common words с соседних страниц — тех, на которые есть ссылки.
# Возможен следующий алгоритм решения задачи:
# 1. Получить ссылки на соседние страницы. Для этого можно воспользоваться библиотекой BeautifulSoup.
# Не забудьте отобрать только правильные ссылки, которые указывают на другие страницы Википедии. (Вы можете распознать их по тексту \wiki).
# 2. Спарсить отдельно соседние страницы. Для этого вам необходимо перебрать в цикле все полученные ссылки.
# 3. Сложить все в один список.


import re
import bs4
from wiki_requests import get_topic_page


def get_topic_words(topic):
    html_content = get_topic_page(topic)
    words = re.findall("[а-яА-Я\-']{3,}", html_content)
    return words


def get_common_words(topic):
    words_list = get_topic_words(topic)
    rate = {}
    for word in words_list:
        if word in rate:
            rate[word] += 1
        else:
            rate[word] = 1
    rate_list = list(rate.items())
    rate_list.sort(key=lambda x: -x[1])
    return rate_list


def visualize_common_words(topic):
    words = get_common_words(topic)
    for w in words[1:100]:
        print(w[0])
topic = input('Topic: ')
print(visualize_common_words(topic))