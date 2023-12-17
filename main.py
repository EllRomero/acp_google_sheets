import gspread
from oauth2client.service_account import ServiceAccountCredentials
from tg_pars import get_url
from bf_url import bf_get_view
from sl_url import sl_get_view


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
    # Проверка какой сайт парсить, дзен блочит request, поэтому эмулируем юзера
    if i[8] == 's':  # stav.aif.ru
        views = bf_get_view(i)
    if i[8] == 'd':  # dzen.ru
        views = sl_get_view(i)
    # Выбор ячейки C
    cell = worksheet.cell(f'{n}', '3')
    # Установить значение в ячейку C
    cell.value = views
    # Сохранение изменений
    worksheet.update_cell(cell.row, cell.col, cell.value)
    # То же самое для ячейки D
    cell = worksheet.cell(f'{n}', '4')
    cell.value = i
    # Меняем строку в таблице
    n += 1
    # Сохранение изменений
    worksheet.update_cell(cell.row, cell.col, cell.value)
input('Таблица обновлена, для продолжения нажмите кнопку ')
