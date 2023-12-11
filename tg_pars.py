from telethon.sync import TelegramClient
from tg_api import tg_hash, tg_id

def get_url(limit: int = 100):
        """
        Функция возвращает из указанного тг канала URL ссылки
        На вход указываем кол-во ссылок, которые будут спарсены.
        """
        api_id = tg_id
        api_hash = tg_hash
        with TelegramClient('session_name', api_id, api_hash) as client:
                # Замени 't.me/pars_link_news' на ссылку на нужный тебе канал
                channel_entity = client.get_entity('t.me/pars_link_news')
                # Получить последние сообщения, указанные по лимиту
                messages = client.get_messages(channel_entity, limit=limit)
                url_link = []
                for message in messages:
                        if message.text:
                                url_link.append(message.text)
        return url_link


if __name__=='__main__':
        get_url(2)