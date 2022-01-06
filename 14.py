# def char_frequency(text):
#    text = text.lower()
#    text = text.replace(" ", "")
#    text = text.replace("\n", "")
#
#    count = {}  # для подсчета символов и их количества
#    for char in text:
#        if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
#            count[char] += 1
#        else:
#            count[char] = 1
#
#    for char, cnt in count.items():
#        print(f"Символ {char} встречается {cnt} раз")

# def pow_func(base):
#     print(base**2)
# pow_func(34)

# def pow_func(base, n=2):
#    print(base ** n)
#
# pow_func(3)  # 9
# pow_func(5, 3)  # 125
# pow_func(24, 4)

# def check_num(a, n):
#     if a % n == 0:
#         print(f"Число{n} является делителем числа {a}")
#     else:
#         print(f"Число{n} не является делителем числа {a}")
# check_num(4, 2)
# check_num(7, 4)

# Напишите функцию, которая печатает «обратную лесенку»
# def retern_step(n):
#     for i in range(n,0,-1):
#         print("*" * i)
# retern_step(80)

# def pow_func(base, n=2):
#    inside_result = base ** n
#    return inside_result
# outside_result = pow_func(3)
# print(outside_result)

# Напишите функцию, которая будет возвращать количество делителей числа а
# def get_multipliers(a):
#     count = 0
#     for n in range(1, a + 1):
#         if a % n == 0:
#             count += 1
#     return count
#
#
# get_multipliers(6)

# def check_palindrome(str_):
#     str_ = str_.lower()
#     str_ = str_.replace(" ", "")
#     if str_ == str_[::-1]:
#         return print("True")
#     else:
#         return print("False")
#
# check_palindrome("test")
# check_palindrome("Кит на море не романтик")

# def my_func(*args, **kwargs):
#   print(type(args))
#   print(type(kwargs))
#
#
# my_func()
# будет перемножать любые значения переданные в функцию
# def adder(*nums):
#   p =  1
#   for n in nums:
#     p *= n
#
#   return p
#
#
# print(adder())  # 0
# print(adder(1))  # 1
# print(adder(1, 2))  # 3
# print(adder(1, 2, 3))
# print(adder(1, 2, 3, 4))

# Числа фибоначи
# def rec_fibb(n):
#    if n == 1:
#     return 1
#    if n == 2:
#     return 1
#    return rec_fibb(n - 1) + rec_fibb(n - 2)
#
#
# rec_fibb(10)

# Найдет сумму всех чисел от 1 до N
# def sum_num(n):
#   if n == 1:
#     return 1
#   return n + sum_num(n-1)
#
#
# sum_num(5)


# Возвращает перевернутую строку
# def reverse_str(string):
#   if len(string) == 0:
#     return ''
#   else:
#     return string[-1] + reverse_str(string[:-1])
#
# print(reverse_str('test'))

# Вычисляет сумму чисел натурального числа n
# def sum_digit(n):
#     if n < 10:
#         return n
#     else:
#         return n % 10 + sum_digit(n // 10)
#
#
# print(sum_digit(123))


# Создайте функцию-генератор, возвращающую бесконечную последовательность натуральных чисел
# def count(start=1, step=1):
#     counter = start
#     while True:
#           yield counter
#           counter += step


# Генирирует бесконечную 123 123 123 123
# def repeat_list(list_):
#   list_values = list_.copy()
#   while True:
#     value = list_values.pop(0)
#     list_values.append(value)
#     yield value
# for i in repeat_list([1,2,3]):
#    print(i)
# repeat_list()

# декораторы
# def my_decorator(a_function_decorate):
#     def wrapper():
#         print("Я буду выполнен до основного вызова")
#         result = a_function_decorate()
#         print("Я буду выполнен после основного вызова")
#         return result
#
#     return wrapper
#
#
# def my_function():
#     print("Я - оборачиваемая функция!")
#     return 0
#
#     print(my_function())
#
#
# # Я - оборачиваемая функция!
# # 0
#
# decorated_function = my_decorator(my_function)  # декорирование функции
# print(decorated_function())

# Вычисляем количество временя сколько понадобиться программе чтоб ее выполнить( зная текущее время и время сразу
# после выполнения можно найти время за которое программа была выполнена import time
#
#
# def decorator_time(fn):
#     def wrapper():
#         print(f"Запустилась функция {fn}")
#         t0 = time.time()
#         result = fn()
#         dt = time.time() - t0
#         print(f"Функция выполнилась. Время: {dt:.10f}")
#         return dt  # задекорированная функция будет возвращать время работы
#
#     return wrapper
#
#
# def pow_2():
#     return 10000000 ** 2
#
#
# def in_build_pow():
#     return pow(10000000, 2)
#
#
# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)

# pow_2()
# Запустилась функция <function pow_2 at 0x7f938401b158>
# Функция выполнилась. Время: 0.0000011921

# in_build_pow()
# Запустилась функция <function in_build_pow at 0x7f938401b620>
# Функция выполнилась. Время: 0.0000021458

# Возьмите из предыдущего примера декорированные функции,
# которые возвращают время работы основной функции и найдите среднее время выполнения для 100 выполнений каждой функции
# import time
#
# N = 100
#
#
# def decorator_time(fn):
#     def wrapper():
#         t0 = time.time()
#         result = fn()
#         dt = time.time() - t0
#         return dt
#
#     return wrapper
#
#
# def pow_2():
#     return 10000000 ** 2
#
#
# def in_build_pow():
#     return pow(10000000, 2)
#
#
# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)
#
# mean_pow_2 = 0
# mean_in_build_pow = 0
# for _ in range(N):
#     mean_pow_2 += pow_2()
#     mean_in_build_pow += in_build_pow()
#
# print(f"Функция {pow_2} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.10f}")
# print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время: {mean_in_build_pow / 100:.10f}")

# Универсальный шаблон для декоратора
# def my_decorator(fn):
#   print("Этот код будет выведен один раз в момент декорирования функции")
#
#   def wrapper(*args, **kwargs):
#     print('Этот код будет выполняться перед каждым вызовом функции')
#     result = fn(*args, **kwargs)
#     print('Этот код будет выполняться после каждого вызова функции')
#     return result
#
#   return wrapper


# Напишите декоратор, который будет подсчитывать количество вызовов декорируемой функции. Для хранения переменной,
# содержащей количество вызовов, используйте nonlocal область декоратора.


# Напишите декоратор, который будет подсчитывать количество вызовов декорируемой функции. Для хранения переменной
# содержащей количество вызовов, используйте nonlocal область декоратора.
# def counter(func):
#     count = 0
#
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         func(*args, **kwargs)
#         count += 1
#         print(f"Функция{func} была вызвана{count} раз")
#
#     return wrapper
#
#
# @counter
# def say_ward(ward):
#     print(ward)
#
#
# say_ward("Oo!!!")
#
# say_ward("Oo!!!")

# Напишите декоратор, который будет сохранять результаты выполнения декорируемой функции в словаре.
# Словарь должен находиться в nonlocal области в следующем формате: по ключу располагается аргумент функции,
# по значению результат работы функции, например, {n: f(n)}.
#
# И при повторном вызове функции будет брать значение из словаря, а не вычислять заново.
# То есть словарь можно считать промежуточной памятью на время работы программы,
# где будут храниться ранее вычисленные значения. Исходная функция, которую нужно
# задекорировать имеет следующий вид и выполняет простое умножение на число 123456789:

# def cache(func):
#     cache_dict = {}
#
#     def wrapper(num):
#         nonlocal cache_dict
#         if num not in cache_dict:
#             cache_dict[num] = func(num)
#             print(f"Добавление результата в кэш:{cache_dict[num]}")
#         else:
#             print(f"Возвращение результата из кэша :{cache_dict[num]}")
#         print(f"Кэш{cache_dict}")
#         return cache_dict[num]
#
#     return wrapper
#
#
# @cache
# def here(n):
#     return n * 123456789
#
#
# here(10)
#
#
# here(10)
#
#
# here(11)
#
#
# here(25)


# def liner_solve(a, b):
#     if a:
#         return b / a
#     elif not a and not b:
#         return "Бесконечное кол-во корней"
#     else:
#         return "Нет корней"
#
#
# print(liner_solve(0, 1))

# Квадратное уравнение


# Напишите рекурсивную функцию, находящую минимальный элемент списка
# без использование циклов и встроенной функции min().

# def min_list(L):
#     if len(L) == 1:
#         return L[0]
#     return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])


# Напишите рекурсивную функцию, которая зеркально разворачивает число.
# Предполагается, что число не содержит нули.

# def mirror(a, res=0):
#     if a == 0:
#         return res
#     else:
#         return mirror(a // 10, res * 10 + a % 10)
#
#
# print(mirror(24))
# Поработаем над более сложной рекурсивной функцией. Сейчас попробуем реализовать функцию equal(N, S),
# проверяющую, совпадает ли сумма цифр числа N с числом S.
# При написании программы следует обратить внимание на то, что,
# если S стала отрицательной, то необходимо сразу вернуть False.

# def equal(N, S):
#     if S < 0:
#         return False
#     if N < 10:
#         return N == S
#     else:
#         return equal(N // 10, S - N % 10)

# ЛЯМДА
# Чтобы отсортировать словать по ключам, нужно сделать так:
# d = {2 : "c", 1 : "d", 4 : "a", 3 : "b"}
#
# # Чтобы отсортировать его по ключам, нужно сделать так:
# print(dict(sorted(d.items())))
# # {1: 'd', 2: 'c', 3: 'b', 4: 'a'}

# sorted(d.items(), key=lambda x: x[1])  # сортировка по значению словаряop
# Даны две строки (словать со всеми большими буквами и словарь с маленькими
# в данном примереб нужно указать число на которое будет совершено смещение символов путем кодировки текстаю
# Далее идет функция по кодированию текста.
# И далее идет открытие заранее подготовленного файла где введен текс который нужно закодировать
# И далее идет файлик куда будет записанана закодированная фраза из переменной "Summary"

# alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# alphaUp = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# number = int(input('Введите число, на которое нужно сдвинуть текст: '))
#
# summary = ''
#
#
# def changeChar(char):
#   if char in alpha:
#     return alpha[(alpha.index(char) + number) % len(alpha)]
#   elif char in alphaUp:
#     return alphaUp[(alphaUp.index(char) + number) % len(alphaUp)]
#   else:
#     return char
#
#
# with open("filename2.txt", encoding="utf8") as myFile:
#   for line in myFile:
#     for char in line:
#       summary += changeChar(char)
#
# with open("output.txt", 'w', encoding="utf8") as myFile:
# myFile.write(summary)

# def changeText(text):
#     # Функция принимает строку, Убирает все знаки припинания
#     # И возвращает список, состоящий из слов текста
#     for i in '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~':
#         text = text.replace(i, '')
#
#     return text.split()
#
#
# def mostCommon(text, lenght=0):
#     # Функция принимает список и ограничения по длине.
#     # Возвращает самый часто встречающийся элемент.
#     # Если есть элемент с одинаковой самой большой частотой,
#     # то вернет их все.
#
#     most_common = []
#     qty_most_common = 0
#
#     for item in text:
#         if len(item) > lenght:
#             qty = text.count(item)
#             if qty > qty_most_common and qty > 2:
#                 qty_most_common = qty
#                 most_common = [item]
#             elif qty == qty_most_common:
#                 most_common.append(item)
#
#     return list(set(most_common))
#
#
# def mostLenght(text):
#     # Функция принимает список.
#     # Возвращает самый длинный элемент.
#     # Если есть несколько элементов с одинаковой самой большой длиной, то вернёт их все.
#
#     most_lenght = []
#     qty_most_lenght = 0
#     alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     for item in text:
#         for char in item:
#             if char not in alphabet:
#                 charEn = False
#             else:
#                 charEn = True
#         if charEn:
#             qty = len(item)
#             if qty > qty_most_lenght:
#                 qty_most_lenght = qty
#                 most_lenght = [item]
#             elif qty == qty_most_lenght:
#                 most_lenght.append(item)
#
#     return list(set(most_lenght))
#
#
# nameFile = input('Назваие файла:')
#
# with open(nameFile, encoding='utf8') as f:
#     fileText = f.read()
#
# fileText = changeText(fileText)
# print(f'Список самых чвстых слов длинной больше трех символов:{mostCommon(fileText, 3)}')
# print(f'Список самых длинных английских слов: {mostLenght(fileText)}')

# import json
#
# import items as items
#
# with open('papa.json', encoding='utf8') as file:
#     templates = json.load(file)
#
#
# def CheckInt(item):
#     return isinstance(item, int)
#
#
# def ChekStr(item):
#     return isinstance(item, str)
#
#
# def ChekBool(item):
#     return isinstance(item, bool)
#
#
# def ChekUrl(item):
#     if isinstance(item, str):
#         return item.startswith('http://') or item.startswith('https://')
#     else:
#         return False
#
#
# def ChekStrValue(item, val):
#     if isinstance(item, str):
#         return item in val
#     else:
#         return False
#
#
# def ErrorLog(item, value, string):
#     Error.append({item: f'{value}, {string}'})
#
#
# listOfItem = {'timestamp': 'int',
#               'referer': 'url',
#               'location': 'url',
#               'remoteHost': 'str',
#               'partyId': 'str',
#               'sessionId': 'str',
#               'pageViewId': 'str',
#               'eventType': 'val',
#               'item_id': 'str',
#               'item_price': 'int',
#               'item_url': 'url',
#               'basket_price': 'str',
#               'detectedDuplicate': 'bool',
#               'detectedCorruption': 'bool',
#               'firstInSession': 'bool',
#               'userAgentName': 'str'}
#
#
# Error = []
# for item in templates:
#     for item in items:
#         if listOfItem[item] == 'int':
#             if not CheckInt(items[item]):
#                 ErrorLog(item, items[item], f'ожидали тип {listOfItem[item]}')
#         elif listOfItem[item] == 'str':
#             if not ChekStr(items[item]):
#                 ErrorLog(item, items[item], f'ожидали тип {listOfItem[item]}')
#         elif listOfItem[item] == 'bool':
#             if not ChekBool(items[item]):
#                 ErrorLog(item, items[item], f'ожидали тип {listOfItem[item]}')
#         elif listOfItem[item] == 'url':
#             if not ChekUrl(items[item]):
#                 ErrorLog(item, items[item], f'ожидали тип {listOfItem[item]}')
#         elif listOfItem[item] == 'val':
#             if not ChekStrValue(items[item], ['itemBuyEvent', 'itemViewEvent']):
#                 ErrorLog(item, items[item], f'ожидали тип itemBuyEvent или itemViewEvent')
#         elif:
#             ErrorLog(item, items[item], 'неожиданное значение')
#     else:
#         ErrorLog(item, items[item], 'неизвестная переменная')
#
# if Error == []:
#     print('pass')
# else:
#     print('Fail')
#     print('Error')


# class User:
#     pass
#
#
# peter = User()
# peter.name = "Peter Robertson"
#
# julia = User()
# julia.name = "Julia Donaldson"
#
# print(peter.name)
# print(julia.name)

# class User:
#     number_of_figures = 5
#     number_of_eyes = 2
#
#
# lancelot = User()
# print(lancelot.number_of_eyes)

# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
#
# peter = User(name="Peter Robertson", email="peterrobertson@mail.com")
# julia = User(name="Julia Donaldson", email="juliadonaldson@mail.com")
#
#
# print(peter.name)
# print(julia.email)


# class Product:
#     def __init__(self, name, category, quantity_in_stock):
#         self.name = name
#         self.category = category
#         self.quantity_in_stock = quantity_in_stock
#
#     def is_available(self):
#         return True if self.quantity_in_stock > 0 else False
#
#
# eggs = Product("eggs", "food", 5)
# print(eggs.is_available())


# class Event:
#     def __init__(self, timestamp=0, event_type="", session_id=""):
#         self.timestamp = timestamp
#         self.type = event_type
#         self.session_id = session_id
#
#     def init_from_dict(self, event_dict):
#         self.timestamp = event_dict.get("timestamp")
#         self.type = event_dict.get("type")
#         self.session_id = event_dict.get("session_id")
#
#
# events = [
#     {
#         "timestamp": 1554583508000,
#         "type": "itemViewEvent",
#         "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
#     {
#         "timestamp": 1555296337000,
#         "type": "itemViewEvent",
#         "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
#     {
#         "timestamp": 1549461608000,
#         "type": "itemBuyEvent",
#         "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
# ]
#
# for event in events:
#     event_obj = Event()
#     event_obj.init_from_dict(event)
#     print(event_obj.timestamp)


# import datetime
#
#
# class Product:
#     max_quantity = 1000000
#
#     def __init__(self, name, category, quantity_in_stock):
#         self.name = name
#         self.category = category
#         self.quantity_in_stock = quantity_in_stock
#
#     def is_available(self):
#         return True if self.quantity_in_stock > 0 else False
#
#
# class Food(Product):
#     is_critical = True
#     needs_to_be_refreshed = True
#     refresh_frequency = datetime.timedelta(days=1)
#
#
# eggs = Food(name="eggs", category="food", quantity_in_stock=5)
# print(eggs.is_available())


# class Event:
#     def __init__(self, timestamp=0, event_type="", session_id=""):
#         self.timestamp = timestamp
#         self.event_type = event_type
#         self.session_id = session_id
#
#     def init_from_dict(self, event_dict):
#         self.timestamp = event_dict.get("timestamp")
#         self.type = event_dict.get("type")
#         self.session_id = event_dict.get("session_id")
#
#     def show_description(self):
#         print("This is generic event.")
#
#
# class ItemViewEvent(Event):
#     type = "itemViewEvent"
#
#     def __init__(self, timestamp=0, session_id="", number_of_views=0):
#         self.timestamp = timestamp
#         self.session_id = session_id
#         self.number_of_view = number_of_views
#
#     def show_description(self):
#         print("This event means someone has browsed an item.")
#
#
# if __name__ == "__main__":
#     test_view_event = ItemViewEvent(timestamp=1549461608000, session_id="0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct", number_of_views=6)
#     test_view_event.show_description()
#     print(test_view_event.type)


