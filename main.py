import os

from dotenv import load_dotenv
from weather_sdk import get_new_event, SMSServer

load_dotenv()

forecast_token = os.getenv('FORECAST_TOKEN')
town_title = 'Курск'
sms_token = os.getenv('SMS_TOKEN')
server = SMSServer(sms_token)

new_event = get_new_event(forecast_token, town_title)

event_date = new_event.get_date()
event_time = new_event.get_time()
event_area = new_event.get_area()
phenomenon_description = new_event.get_phenomenon()

sms_template = '''{town_title}: {event_time} {event_date} {event_area} ожидается {phenomenon_description}. Будьте внимательны и осторожны.'''

sms_message = sms_template.format(
    phenomenon_description = phenomenon_description,
    town_title = town_title,
    event_time = event_time,
    event_date = event_date,
    event_area = event_area,
)

server.send(sms_message)


# Гипотеза 1: В переменной нет прогноза погоды для Курска
# Способ проверки: Выведу переменную new_event
# Код для проверки: print(new_event)
# Установленный факт: функция print возвращает значение переменной: "Регион:  Погода:"
# Вывод: Гипотеза подтвердилась


# Гипотеза 2.1: town_title на самом деле пуста
# Способ проверки: Выведу переменную town_title
# Код для проверки: print(town_title)
# Установленный факт: В переменной town_title находится строка.
# Вывод: Гипотеза не подтвердилась.


# Гипотеза 2.2: В town_title не название города
# Способ проверки: Выведу переменную town_title
# Код для проверки: print(town_title)
# Установленный факт: В переменной town_title находится строка с названием города.
# Вывод: Гипотеза не подтвердилась,в переменной именно название города.


# Гипотеза 3: Переменная token на самом деле пуста
# Способ проверки: Выведу переменную token
# Код для проверки: print(token, "token")
# Установленный факт: Функция print возвращает значение None token.
# Вывод: Гипотеза подтвердилась. Переменная token пуста.


# Гипотеза 4.1: Может, `token` всё ещё пуст?
# Способ проверки: Выведу переменную token
# Код для проверки:
# token = os.getenv('FORECAST_TOKEN')
# town_title = 'Курск'
# print(token)
# token = os.getenv('SMS_TOKEN')
# server = SMSServer(token)
# print(token)
# Установленный факт: Оба токена выводятся
# 85b98d96709fd49a69ba8165676e4592
# aGVsbG8gY3J5cHRvIGVudHVzaWFzdCA7KQ==
# Вывод: Гипотеза не подтвердилась. Обе переменные token имеют заданное значение.


# Гипотеза 4.2: Может, в токене не то значение, не `85b98d96709fd49a69ba8165676e4592`?
# Способ проверки: Выведу переменную token
# Код для проверки:
# token = os.getenv('FORECAST_TOKEN')
# town_title = 'Курск'
# token = os.getenv('SMS_TOKEN')
# server = SMSServer(token)
# print(token)
# Установленный факт: В токене хранится неверное значение.
# Вывод: Гипотеза подтвердилась.


# Гипотеза 4.3: Может, значение `85b98d96709fd49a69ba8165676e4592` успевает измениться до строчки `new_event = ...`?
# Способ проверки: Выведу переменную token
# Код для проверки:
# token = os.getenv('FORECAST_TOKEN')
# town_title = 'Курск'
# print("Первоначальное значение переменной token =", token)
# token = os.getenv('SMS_TOKEN')
# server = SMSServer(token)
# print("Итоговое значение переменной token =", token)
# Установленный факт: Значение переменной меняется по ходу выполнения программы.
# Вывод: Гипотеза подтвердилась. Значение токена меняется, что влияет на значение переменной new_event.


# Гипотеза 5: Переменные event_time, event_date, event_area и phenomenon_description пусты и/или имеют неподходящие значения
# Способ проверки: Выведу все эти 4 переменные функцией print.
# Код для проверки:
# event_date = new_event.get_date()
# print(event_date)
# event_time = new_event.get_time()
# print(event_time)
# event_area = new_event.get_area()
# print(event_area)
# phenomenon_description = new_event.get_phenomenon()
# print(phenomenon_description)
# Установленный факт: Все 4 переменные несут корректные значения.
# Вывод: Гипотеза не подтвердилась.


# Гипотеза 6: Возможно, в шаблоне используются какие-то переменные, которые не передаются в .format()?
# Способ проверки: Поочерёдно выделю мышью переменные 'phenomenon_description', 'town_title', 
# 'event_time', 'event_date' и 'event_area'. При выделении переменной проверю "подсвечивается" ли она во всех
# остальных местах в теле кода.
# Код для проверки: ...
# Установленный факт: Все перечисленные переменные "подсвечиваются" при выделении мышью.
# Вывод: Гипотеза не подтвердилась.


# Гипотеза 7: Возможно есть несоответствие в значениях переменных sms_template и sms_message. 
# В их очерёдности в тексте.
# Способ проверки: Укажу в коде, под какие именно переменные подставить нужные данные.
# Код для проверки: 
# sms_message = sms_template.format(
#     phenomenon_description = phenomenon_description,
#     town_title = town_title,
#     event_time = event_time,
#     event_date = event_date,
#     event_area = event_area,
# )
# Установленный факт: Значения переменнных находятся не на своём месте.
#  Вывод: Гипотеза подтвердилась. После правок код начал корректно работать.