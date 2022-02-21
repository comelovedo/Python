from decorators import debug


# Функция декоратор
# def my_decorator(func):
#     def wrapper():
#         print("Начало выполнения функции.")
#         func()
#         print("Конец выполнения функции.")
#
#     return wrapper
#
#
# # Эту функцию мы будем декорировать
# def my_first_decorator():
#     print("Это мой первый декоратор!")
#
#
# my_first_decorator = my_decorator(my_first_decorator)


# Давайте рассмотрим пример функции, которая выполняется
# только в рабочие часы (допустим, во время ремонта, чтобы
# не беспокоить соседа). Если текущее время соответствует
# промежутку с 9 до 18, то мы выполняем функцию, в противном
# случае мы пропускаем этот шаг


# def working_hours(func):
#     def wrapper():
#         if 9 <= datetime.now().hour < 18:
#             func()
#         else:
#             pass  # Нерабочее время, выходим
#
#     return wrapper
#
#
# def writing_tests():
#     print("Я пишу тесты на python!")


# writing_tests = working_hours(writing_tests)
# print(writing_tests())


# @do_twice
# def test_twice():
#     print("Это вызов функции test_twice!")


# Чтобы сделать нашу функцию-декоратор универсальной,
# существует достаточно простое решение: нужно использовать
# *args и **kwargs внутри функции-обёртки. В этом случае наша
# функция будет принимать любое количество аргументов (включая 0).

# @do_twice
# def test_twice_without_params():
#     print("Этот вызов без параметров")
#
#
# @do_twice
# def test_twice_2_params(str1, str2):
#     print("В этой функции 2 параметра - {0} и {1}".format(str1, str2))
#
#
# @do_twice
# def test_twice(str):
#     print("Этот вызов возвращает строку {0}".format(str))
#

# test_twice_without_params()
# test_twice_2_params("1", "2")
# test_twice("single")

# Итак, давайте разберемся, что происходит в этом примере:
#
# Мы вызываем функцию test_twice, которая декорирована, то есть
# по факту мы вызываем функцию-декоратор wrapper.
# Функция-обёртка выполняется, и мы отчетливо видим это в выводе консоли
# (две одинаковых строки). При этом каждый раз наша основная функция печатает
# эти строки и возвращает строку Done в функцию-обёртку.
# После этого функция-обёртка завершает свою работу и возвращает None (помните, мы
# говорили о побочных эффектах и отсутствии возвращаемого значения в функциях?).
# Это значение и передаётся в нашу переменную decorated_value.

# @do_twice
# def test_twice(str):
#     print("Этот вызов возвращает строку {0}".format(str))
#     return "Done"
#
# # мы можем получить информацию о любом объекте. Для нашего
# # примера будет достаточно возвращать имя функции:
#
#
# print(test_twice.__name__)

# decorated_value = test_twice("single")
# print(decorated_value)

@debug
def age_passed(name, age=None):
    if age is None:
        return "Необходимо передать значение age"
    else:
        return "Аргументы по умолчанию заданы!"


age_passed("Роман")
age_passed("Роман", age=21)
