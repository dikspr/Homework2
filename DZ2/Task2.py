# Используя навыки работы с текстом, получите количество студентов GeekBrains со стартовой страницы сайта geekbrains.ru.
# b) используя библиотеку BeautifulSoup.
# Примечание: Чтобы увидеть количество учеников, вам надо зайти на главную страницу сайта без залогинивания
# (нажмите 3 точки в правом верхнем углу экрана рядом с вашей фотографией и выберите пункт меню «Выход»).
# Вы окажетесь на главной странице, где вверху увидите логотип, количество человек (то, что нам нужно) и кнопку «Войти».

from bs4 import BeautifulSoup as BS

with open('index.html', 'r', encoding='utf-8') as f:
    page = f.read()

ind = BS(page, 'html.parser')
students = ind.find_all(class_='total-users')[0].get_text()
print(students)