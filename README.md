Программа парсит кол-во просмотров с указанного сайта, из предоставленных URL в телеграм канале. Далле обновляет, полученные просмотры с каждого URL, в гугл таблицах.

sl_url.py - Делает запрос при помощи selenium(предназначен для Dzen т.к. сайт детектит бота), далее возвращает страницу и парсит ее с помощью bf4. Использован header мобильный устройств. А также надстройки над драйвером, для маскировки, что запрос выоплняет программа.


bf_url.py - Делает запрос при помощи request, парсит полученную страницу с помощью bf 4.


tg_pars.py - Парсим группу с помощью библиотеки telethon, возвращаем список url с указанным кол-во последних постов.


main.py - Главный файл, вызывает методы для получения url и кол-во просмотров на странице, устанавливает соеденение с гугл таблице и записывает в нужные поля инфу. Настройки main:


api_id,api_hash - подставить свои, можно узнать на "https://my.telegram.org/auth?to=apps"


json ключ вашего проекта из сервисного аккаунат, подробнее "https://cloud.google.com/iam/docs/keys-create-delete"
