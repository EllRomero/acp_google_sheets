import requests
from bs4 import BeautifulSoup


def get_views(url):
    """
    Функция возвращает с сайта значение просмотров
    На вход получает url
    """
    # Отправляем GET-запрос к веб-сайту
    response = requests.get(url=url)
    # Создаем объект BeautifulSoup на основе содержимого страницы
    soup = BeautifulSoup(response.text, 'html.parser')
    # Парсим кол-во просмотров
    views = soup.find('div', class_='viewed').text
    return views
