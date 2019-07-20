from requests import get


# Функция возвращает начальную ссылку
def get_start_link(topic):
    link = f'https://ru.wikipedia.org/wiki/{topic.capitalize()}'
    return link


# Функция возвращает ссылку на сопутствующую страницу
def get_link(wiki_link):
    link = f'https://ru.wikipedia.org{wiki_link}'
    return link


# Функция, которая возвращает текст страницы по ссылке
def get_topic_page(link):
    # link = get_link(topic)
    html_content = get(link).text
    return html_content
