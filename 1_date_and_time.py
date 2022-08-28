"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta

def print_days():
    now = datetime.now()
    onedayago = now - timedelta(days = 1)
    thirtydaysago = now - timedelta(days = 30)
    print(f"Сегодня\t\t\t{now.strftime('%d.%m.%Y')}")
    print(f"Вчера было\t\t{onedayago.strftime('%d.%m.%Y')}")
    print(f"30 дней назад было\t{thirtydaysago.strftime('%d.%m.%Y')}")

def str_2_datetime(date_string):
    return datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))