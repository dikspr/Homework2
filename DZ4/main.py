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

def get_topic_text(topic):
    html_content = get_topic_page(topic)
    words = re.findall('[а-яА-Я]+', html_content)
    return words

print(get_topic_text('Россия'))
