# Упражнение продолжает практическую работу из последнего видеоурока. Для усовершенствования приложения разберитесь, как можно реализовать получение common words с соседних страниц — тех, на которые есть ссылки.
# Возможен следующий алгоритм решения задачи:
# 1. Получить ссылки на соседние страницы. Для этого можно воспользоваться библиотекой BeautifulSoup. Не забудьте отобрать только правильные ссылки, которые указывают на другие страницы Википедии. (Вы можете распознать их по тексту \wiki).
# 2. Спарсить отдельно соседние страницы. Для этого вам необходимо перебрать в цикле все полученные ссылки.
# 3. Сложить все в один список.

# https://ru.wikipedia.org/wiki/

from requests import get

def get_link(topic):
    link = f'https://ru.wikipedia.org/wiki/{topic.capitalize()}'
    return link

def get_topic_page(topic):
    link = get_link(topic)
    html_content = get(link).text
    with open('new.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    return True




