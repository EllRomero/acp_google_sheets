import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


def sl_get_view(url: str) -> int:
    """
    Функция возвращает с сайта значение просмотров,
    используя Selenium.
    На вход получает url.
    """
    # Инициализация настроек и веб-драйвера
    service = Service()
    options = webdriver.ChromeOptions()
    # Добавление настроечных парамеров
    options.add_experimental_option("excludeSwitches", ["enable-automation"])  
    options.add_experimental_option("useAutomationExtension", False)    
    options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1")      
    options.add_argument("--disable-blink-features=AutomationControlled") 
    options.add_argument("log-level=3")
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    # Открытие урл
    driver.get(url=url)
    # Установка максимального времени ожидания в 10 секунд
    wait = WebDriverWait(driver, 10)
    # Ожидание, пока элемент на странице не будет видимым
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))
    time.sleep(0.5)
    # Копируем страницу
    html_page = driver.page_source
    # Закрытие браузера
    driver.quit()
    soup = BeautifulSoup(html_page, 'html.parser')
    # Парсим кол-во просмотров
    views = soup.find('span', class_='article-stats-view__stats-item-count').text
    # Меняем обозначение К в int значение на выход
    views_str = replace_k(views)
    views = ''
    for i in views_str:
        if i in '0123456789':
            views += i
        else:
            break
    return int(views)


def replace_k(text: str) -> str:
    """
    Функция заменят текст, используя регулярные выражения,
    на правильный для преобразования в int.
    """
    if ',' in text:
        text_out = re.sub(r',([0-9])K', r'\g<1>00', text)
    else:
        text_out = re.sub(r'([0-9])K', r'\g<1>000', text)
    return text_out
