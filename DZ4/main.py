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
def get_common_words(words_list):
    rate = {}
    for word in words_list:
        if word in rate:
            rate[word] += 1
        else:
            rate[word] = 1
    rate_list = list(rate.items())
    rate_list.sort(key=lambda x: -x[1])
    return rate_list


# Функция выводит на экран наиболее часто повторяющихся слов в списке
def visualize_common_words(words_list):
    words = get_common_words(words_list)
    for w in words[20:30]:
        print(w[0])


# Запрашиваем название топика.
topic = input('Topic: ')
# Создаем пустой список ссылок и добавляем в него ссылку на страницу основного топика
links = []
links.append(get_start_link(topic))
# Заполняем список ссылками на дочерние страницы
for wiki_link in get_wiki_links(get_start_link(topic)):
    links.append(get_link(wiki_link))
# Создаем список слов из текстов страниц и заполняем его
# (что бы не было скучно ждать, выводится число слов в списке после добавления новой страницы)
pages_words = []
i = 1
for wiki_link in links:
    pages_words.extend(get_topic_words(wiki_link))
    len_list = len(pages_words)
    print(f'Найдено {len_list} слов на {i} страницах из {len(links)}')
    i += 1
# Отображаем результат
visualize_common_words(pages_words)