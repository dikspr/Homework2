# Упражнение продолжает практическую работу из последнего видеоурока.
# Для усовершенствования приложения разберитесь, как можно реализовать получение common words с соседних страниц — тех, на которые есть ссылки.
# Возможен следующий алгоритм решения задачи:
# 1. Получить ссылки на соседние страницы. Для этого можно воспользоваться библиотекой BeautifulSoup.
# Не забудьте отобрать только правильные ссылки, которые указывают на другие страницы Википедии. (Вы можете распознать их по тексту \wiki).
# 2. Спарсить отдельно соседние страницы. Для этого вам необходимо перебрать в цикле все полученные ссылки.
# 3. Сложить все в один список.


import re
from bs4 import BeautifulSoup as BS
from wiki_requests import get_topic_page, get_start_link, get_link


# Функция, которая получает список ссылок на соседние страницы
def get_wiki_links(link):
    html_content = get_topic_page(link)
    soup = BS(html_content, 'html.parser')
    links = soup.find_all("a")
    links = [link.get('href', '') for link in links]
    links = [link for link in links if re.search('/wiki/', link) and not re.search('./wiki/', link)]
    return links


# Функция, которая получает список из текста страицы
def get_topic_words(link):
    html_content = get_topic_page(link)
    words = re.findall("[а-яА-Я\-']{3,}", html_content)
    return words


# Функция, которая сортирует список слов из текста на странице по количеству повторений
def get_common_words(link):
    words_list = get_topic_words(link)
    rate = {}
    for word in words_list:
        if word in rate:
            rate[word] += 1
        else:
            rate[word] = 1
    rate_list = list(rate.items())
    rate_list.sort(key=lambda x: -x[1])
    return rate_list


def visualize_common_words(link):
    words = get_common_words(link)
    for w in words[1:10]:
        print(w[0])


topic = input('Topic: ')
links = []
links.append(get_start_link(topic))
for wiki_link in get_wiki_links(get_start_link(topic)):
    links.append(get_link(wiki_link))
print(links)
