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
#     test_view_event = ItemViewEvent(timestamp=1549461608000,
#     session_id="0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct", number_of_views=6)
#     test_view_event.show_description()
#     print(test_view_event.type)

# class ParentException(Exception):
#     # допишем к нашему пустому классу конструктор, который будет
#     # печатать дополнительно в консоль информацию об ошибке.
#     def __init__(self, message, error):
#         super().__init__(message)  # помним про вызов конструктора родительского класса
#         print(f"Error:{error}")  # печатаем ошибку
#
#
# class ChildException(ParentException):
#     # создаём пустой класс – исключение наследника, наследуемся от ParentException
#     def __init__(self, message, error):
#         super().__init__(message, error)
#
#
# try:
#     raise ChildException("massage", "error")  # поднимаем исключение-наследник, передаём дополнительный аргумент
# except ParentException as e:
#     print(e)  # выводи информацию об исключении


# рекурсия до 5
# def func(n):
#     if n == 0:
#         return
#     else:
#         func(n - 1)
#         print(n)
#
#
# func(5)

# N_max = int(input("Определите размер очереди:"))
#
# queue = [0 for _ in range(N_max)]  # инициализируем список с нулевыми элементами
# order = 0  # будем хранить сквозной номер задачи
# head = 0  # указатель на начало очереди
# tail = 0  # указатель на элемент следующий за концом очереди
#
#
# def is_empty():  # очередь пуста?
#     # да, если указатели совпадают и в них содержится ноль
#     return head == tail and queue[head] == 0
#
#
# def size():  # получаем размер очереди
#     if is_empty():  # если она пуста
#         return 0  # возвращаем ноль
#     elif head == tail:  # иначе, если очередь не пуста, но указатели совпадают
#         return N_max  # значит очередь заполнена
#     elif head > tail:  # если хвост очереди сместился в начало списка
#         return N_max - head + tail
#     else:  # или если хвост стоит правее начала
#         return tail - head
#
#
# def add():  # добавляем задачу в очередь
#     global tail, order
#     order += 1  # увеличиваем порядковый номер задачи
#     queue[tail] = order  # добавляем его в очередь
#     print("Задача №%d добавлена" % (queue[tail]))
#
#     # увеличиваем указатель на 1 по модулю максимального числа элементов
#     # для зацикливания очереди в списке
#     tail = (tail + 1) % N_max
#
#
# def show():  # выводим приоритетную задачу
#     print("Задача №%d в приоритете" % (queue[head]))
#
#
# def do():  # выполняем приоритетную задачу
#     global head
#     print("Задача №%d выполнена" % (queue[head]))
#     queue[head] = 0  # после выполнения зануляем элемент по указателю
#     head = (head + 1) % N_max  # и циклично перемещаем указатель
#
#
# while True:
#     cmd = input("Введите команду")
#     if cmd == "empty":
#         if is_empty():
#             print("Очередь пуста")
#         else:
#             print("В очереди есть задача")
#     elif cmd == "size":
#         print("кол-во задач в очереди:", size())
#     elif cmd == "add":
#         if size() != N_max:
#             add()
#         else:
#             print("Очередь переполнена")
#     elif cmd == "show":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             show()
#     elif cmd == "do":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             do()
#     elif cmd == "exit":
#         for _ in range(size()):
#             do()
#         print("Очередь пустая. Завершить задачу")
#         break
#     else:
#         print("Введена неверная команда")
#
#
# #  Алгоритм Дейкстры
# G = {"Адмиралтейская":
#          {"Садовая": 4},
#      "Садовая":
#          {"Сенная площадь": 3,
#           "Спасская": 3,
#           "Адмиралтейская": 4,
#           "Звенигородская": 5},
#      "Сенная площадь":
#          {"Садовая": 3,
#           "Спасская": 3},
#      "Спасская":
#          {"Садовая": 3,
#           "Сенная площадь": 3,
#           "Достоевская": 4},
#      "Звенигородская":
#          {"Пушкинская": 3,
#           "Садовая": 5},
#      "Пушкинская":
#          {"Звенигородская": 3,
#           "Владимирская": 4},
#      "Владимирская":
#          {"Достоевская": 3,
#           "Пушкинская": 4},
#      "Достоевская":
#          {"Владимирская": 3,
#           "Спасская": 4}}
#
# D = {k: 100 for k in G.keys()}  # расстояния
# start_k = 'Адмиралтейская'  # стартовая вершина
# D[start_k] = 0  # расстояние от нее до самой себя равно нулю
# U = {k: False for k in G.keys()}  # флаги просмотра вершин
# P = {k: None for k in G.keys()}  # предки
#
# for _ in range(len(D)):
#     # выбираем среди непросмотренных наименьшее по расстоянию
#     min_k = min([k for k in U.keys() if not U[k]], key=lambda x: D[x])
#
#     for v in G[min_k].keys():  # проходимся по всем смежным вершинам
#         if D[v] > D[min_k] + G[min_k][v]:  # если расстояние от текущей вершины меньше
#             D[v] = D[min_k] + G[min_k][v]  # то фиксируем его
#             P[v] = min_k  # и записываем как предок
#     U[min_k] = True  # просмотренную вершину помечаем
#
#     pointer = 'Владимирская'  # куда должны прийти
#     while pointer is not None:  # перемещаемся, пока не придём в стартовую точку
#         print(pointer)
#         pointer = P[pointer]

# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left_child = None
#         self.right_child = None
#     def insert_left(self, next_value):
#         if self.left_child is None:
#             self.left_child = BinaryTree(next_value)
#         else:
#             new_child = BinaryTree(next_value)
#             new_child.left_child = self.left_child
#             self.left_child = new_child
#         return self
#
#     def insert_right(self, next_value):
#         if self.right_child is None:
#             self.right_child = BinaryTree(next_value)
#         else:
#             new_child = BinaryTree(next_value)
#             new_child.right_child = self.right_child
#             self.right_child = new_child
#         return self
#
#     def post_order(self):
#         if self.left_child is not None:  # если левый потомок существует
#             self.left_child.post_order()  # рекурсивно вызываем функцию
#
#         if self.right_child is not None:  # если правый потомок существует
#             self.right_child.post_order()  # рекурсивно вызываем функцию
#
#         print(self.value)  # процедура обработки
#
#
# A_node = BinaryTree('A').insert_left('B').insert_right('C')
# # создаём корень и его потомков /7|2|5\
# node_root = BinaryTree(2).insert_left(7).insert_right(5)
# # левое поддерево корня /2|7|6\
# node_7 = node_root.left_child.insert_left(2).insert_right(6)
# # правое поддерево предыдущего узла /5|6|11\
# node_6 = node_7.right_child.insert_left(5).insert_right(11)
# # правое поддерево корня /|5|9\
# node_5 = node_root.right_child.insert_right(9)
# # левое поддерево предыдущего узла корня /4|9|\
# node_9 = node_5.right_child.insert_left(4)
#
#
# def post_order(self):
#     if self.left_child is not None: # если левый потомок существует
#         self.left_child.post_order() # рекурсивно вызываем функцию
#
#     if self.right_child is not None: # если правый потомок существует
#         self.right_child.post_order() # рекурсивно вызываем функцию
#
#     print(self.value) # процедура обработки
#


# #
# # node_root.post_order()
#
#
# class Node:  # класс элемента
#     def __init__(self, value=None, next_=None):  # инициализируем
#         self.value = value  # значением
#         self.next = next_  # и ссылкой на следующий элемент
#
#     def __str__(self):
#         return "Node value = " + str(self.value)
#
#
# class LinkedList:  # класс списка
#     def __init__(self):  # инициализируем пустым
#         self.first = None
#         self.last = None
#
#     def clear(self):  # очищаем список
#         self.__init__()
#
#     def __str__(self):  # функция печати
#         R = ''
#
#         pointer = self.first  # берем первый указатель
#         while pointer is not None:  # пока указатель не станет None
#             R += str(pointer.value)  # добавляем значение в строку
#             pointer = pointer.next  # идем дальше по указателю
#             if pointer is not None:  # если он существует добавляем пробел
#                 R += ' '
#         return R
#
#     def pushleft(self, value):
#         if self.first is None:
#             self.first = Node(value)
#             self.last = self.first
#         else:
#             new_node = Node(value, self.first)
#             self.first = new_node
#
#     def pushright(self, value):
#         if self.first is None:
#             self.first = Node(value)
#             self.last = self.first
#         else:
#             new_node = Node(value)
#             self.last.next = new_node
#             self.last = new_node
#
#     def popleft(self):
#         if self.first is None:  # если список пустой, возвращаем None
#             return None
#         elif self.first == self.last:  # если список содержит только один элемент
#             node = self.first  # сохраняем его
#             self.__init__()  # очищаем
#             return node  # и возвращаем сохраненный элемент
#         else:
#             node = self.first  # сохраняем первый элемент
#             self.first = self.first.next  # меняем указатель на первый элемент
#             return node  # возвращаем сохраненный
#
#     def popright(self):
#         if self.first is None:  # если список пустой, возвращаем None
#             return None
#         elif self.first == self.last:  # если список содержит только один элемент
#             node = self.first  # сохраняем его
#             self.__init__()  # очищаем
#             return node  # и возвращаем сохраненный элемент
#         else:
#             node = self.last  # сохраняем последний
#             pointer = self.first  # создаем указатель
#             while pointer.next is not node:  # пока не найдем предпоследний
#                 pointer = pointer.next
#             pointer.next = None  # обнуляем указатели, чтобы
#             self.last = pointer  # предпоследний стал последним
#             return node   # возвращаем сохраненный
#
#     def __iter__(self):  # объявляем класс как итератор
#         self.current = self.first  # в текущий элемент помещаем первый
#         return self  # возвращаем итератор
#
#     def __next__(self):  # метод перехода
#         if self.current is None:  # если текущий стал последним
#             raise StopIteration  # вызываем исключение
#         else:
#             node = self.current  # сохраняем текущий элемент
#             self.current = self.current.next  # совершаем переход
#             return node  # и возвращаем сохраненный
#
#     def __len__(self):
#         count = 0
#         pointer = self.first
#         while pointer is not None:
#             count += 1
#             pointer = pointer.next
#         return count
#
#
# LL = LinkedList()
#
# LL.pushright(1)
# LL.pushleft(2)
# LL.pushright(3)
# LL.popright()
# LL.pushleft(4)
# LL.pushright(5)
# LL.popleft()
#
# print(len(LL))


# Алгоритмы поиска:

# Линейный поиск:
# Пусть на вход программы поступает массив из произвольного количества целых чисел
# и ещё одно целое число, которое будем проверять на вхождение в этот массив
# Задача состоит в том, чтобы вернуть индекс первого вхождения элемента,
# если он входит в него, и False если не входит.

# def find(array, element):
#     for i, a in enumerate(array):
#         if a == element:
#             return i
#     return False


# Функция count, которая возвращает количество вхождений элемента в массив
# def count(array, element):
#     count = 0
#     for a in array:
#         if a == element:
#             count += 1
#
#
# array = list(map(int, input().split()))
# element = int(input())
#
# print(find(array, element))

# Линейный алгоритм поиска может применяться для следующих целей:
#
# Нахождение минимального / максимального элемента.
# Поиск элемента с определённым значением.
# Количество вхождений элемента в массив.
# Количество элементов больше заданного.

# В случае нахождения минимального (максимального) элемента линейный поиск
# имеет смысл применять только при небольшом количестве элементов и если
# структура не отсортирована. Для больших структур, а, тем более, если они
# уже сортированы, имеет смысл применять более эффективные алгоритмы.

# Двоичный поиск:
# Алгоритм двоичного поиска является более совершенным, чем линейный поиск,
# однако он накладывает на структуру сильное ограничение — она должна быть отсортирована.

# В связи с тем, что алгоритм может искать только в отсортированном массиве,
# используем генератор последовательных чисел range. Суть двоичного поиска
# сводится к тому, что на каждой итерации размер исследуемого массива уменьшается в два раза.

# def binary_search(array, element, left, right):
#     if left > right:  # если левая граница превысила правую,
#         return False  # значит элемент отсутствует
#
#     middle = (right + left) // 2  # находимо середину
#     if array[middle] == element:  # если элемент в середине,
#         return middle  # возвращаем этот индекс
#     elif element < array[middle]:  # если элемент меньше элемента в середине
#         # рекурсивно ищем в левой половине
#         return binary_search(array, element, left, middle - 1)
#     else:  # иначе в правой
#         return binary_search(array, element, middle + 1, right)
#
#
# element = int(input())
# array = [i for i in range(1, 100)]  # 1,2,3,4,...
#
# # запускаем алгоритм на левой и правой границе
# print(binary_search(array, element, 0, 99))

# Алгоритмы сортировки:

# Данные, которые приходят в программу из внешней среды, чаще всего являются
# несортированными — их порядок ничем не определяется. Согласитесь, что это
# далеко не всегда удобно. А если мы говорим про алгоритмы, то это ещё и сильно
# снижает эффективность.


# Наивная сортировка:( Как делать не стоит)
# import random  # модуль, с помощью которого перемешиваем массив
#
# # пусть имеем массив всего лишь из 9 элементов
# array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# is_sort = False  # станет True, если отсортирован
# count = 0  # счетчик количества перестановок
#
# while not is_sort:  # пока не отсортирован
#     count += 1  # прибавляем 1 к счётчику
#
#     random.shuffle(array)  # перемешиваем массив
#
#     # проверяем, отсортирован ли
#     is_sort = True
#     for i in range(len(array) - 1):
#         if array[i] > array[i + 1]:
#             is_sort = False
#             break
#
# print(array)
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(count)
# # 290698
#
# Сортировка выбором:
# Следующее решение «в лоб» —
# каждый раз искать минимальный элемент и ставить его в начало.
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# count = 0
# for i in range(len(array)):  # проходим по всему массиву
#     idx_min = i  # сохраняем индекс предположительно минимального элемента
#     for j in range(i, len(array)):
#         count += 1 # Посчитайте количество сравнений, которые производятся в алгоритме выбором из примера.
#         if array[j] < array[idx_min]:
#             idx_min = j
#     if i != idx_min:  # если индекс не совпадает с минимальным, меняем
#         array[i], array[idx_min] = array[idx_min], array[i]
#
# print(count) # количество сравнений

# Сортировка пузырьком:
# Его суть сводится к тому, что максимальные элементы шаг за шагом «всплывают»
# вправо — в отсортированную часть массива. И по ходу совершаются ещё перестановки,
# если это необходимо, ведь каждый раз мы сравниваем только соседние элементы!

# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
#
# for i in range(len(array)):
#     for j in range(len(array) - i - 1):
#         if array[j] > array[j + 1]:
#             array[j], array[j + 1] = array[j + 1], array[j]
#
# print(array)

# Сортировка вставками:
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# count = 0
# for i in range(1, len(array)):
#     x = array[i]
#     idx = i
#     while idx > 0 and array[idx-1] > x:
#         count += 1
#         array[idx] = array[idx-1]
#         idx -= 1
#     array[idx] = x
#
# print(count)
#
# Сравните результаты. Алгоритм сортировки вставками хоть и является также
# квадратичным по времени (в среднем), но имеет меньшие множители (в силу умень-
# шенного количества тяжелых операций). И к тому же очень хорошо работает на
# почти отсортированных массивах.


# Быстрая сортировка:
# def qsort(array, left, right):
#     middle = (left+right) // 2
#
#     p = array[middle]
#     i,j = left, right
#     while i <= j:
#         while array[i] < p:
#             i += 1
#         while array[j] > p:
#             j -= 1
#         if i <= j:
#             array[i], array[j] = array[j], array[i]
#             i += 1
#             j -= 1
#
#     if j > left:
#         qsort(array, left, j)
#     if right > i:
#         qsort(array, i, right)