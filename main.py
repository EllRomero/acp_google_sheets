import gspread
from oauth2client.service_account import ServiceAccountCredentials
from tg_pars import get_url
from bf_url import get_views


# Перечисляем подключаемые API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
# Указываем ключ формата "mypython-407516ssafsf.json"
credentials = ServiceAccountCredentials.from_json_keyfile_name('mypython-407516-485da67b8a7c.json', scope)
# Создание клиента
client = gspread.authorize(credentials)
# Открытие Google Таблицы по ее имени
spreadsheet = client.open('Гонорар таблиц сайта')
# Выбор листа
worksheet = spreadsheet.sheet1
url = get_url(int(input('Введи кол-во постов: ')))
# Начальная позиция для ячеек таблиц
n = 2
for i in url:
    views = get_views(i)
    # Выбор ячейки C
    cell = worksheet.cell(f'{n}', '3')
    # Установить значение в ячейку
    cell.value = int(views)
    # Сохранение изменений
    worksheet.update_cell(cell.row, cell.col, cell.value)
    # Запись значения в ячейку
    cell = worksheet.cell(f'{n}', '4')
    cell.value = i
    n += 1
    # Сохранение изменений
    worksheet.update_cell(cell.row, cell.col, cell.value)
input('Таблица обновлена, для продолжения нажмите кнопку ')
