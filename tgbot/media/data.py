import json  # подключили библиотеку для работы с json
from pprint import pprint  # подключили Pprint для красоты выдачи текста

with open('funds.json', 'r', encoding='utf-8') as f:  # открыли файл с данными
    text = json.load(f)  # загнали все, что получилось в переменную


print(text.get('first_fund_type').get('photo'))