import json  # подключили библиотеку для работы с json
from pprint import pprint  # подключили Pprint для красоты выдачи текста

with open('C:/Users/ART/PycharmProjects/TG_BOT/tgbot_template/tgbot/media/funds.json', 'r', encoding='utf-8') as f:  # открыли файл с данными
    funsd = json.load(f)  # загнали все, что получилось в переменную


print(funsd )