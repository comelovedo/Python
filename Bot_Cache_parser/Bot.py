# import requests
#
# r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')  # делаем запрос на сервер попереданному адресу
#
#
# print(r.content)

# Как вы заметили, чтобы получить содержание ответа, надо обратится к полю content объекта response,
# который возвращается, когда приходит ответ от сервера через библиотеку Requests.
# У этого объекта на самом деле есть много полей, например, status_code, который говорит нам о том,
# какой вообще ответ пришёл. Давайте поменяем наш код и посмотрим, что программа выведет теперь.

# import requests
#
# r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')
# print(r.status_code)  # узнаем статус полученного ответа

# 200, 201, 202 и т. д. — ответы, которые говорят, что с запросом всё хорошо, и ответ приходит правильный,
# т. е. его можно обрабатывать и как-либо взаимодействовать с ним. На самом деле почти все сервера всегда
# в ответ шлют именно ответ 200, а не какой-либо другой из этой же категории.

# 300, 301 и т. д. — ответы, которые говорят, что вы будете перенаправлены на
# другой ресурс (не обязательно на этом же сервере).

# 400, 401 и т. д. — ответы, которые говорят, что что-то неправильно с запросом.
# Запрашивается либо несуществующая страница (всем известная 404 ошибка), либо же недостаточно
# прав для просмотра страницы (403) т. д.

# 501, 502 и т. д. — ответы, которые говорят, что с запросом всё хорошо, но вот на сервере что-то
# сломалось, и поэтому нормальный ответ прийти не может.

# import requests
# import json
#
#
# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')  # попробуем поймать json ответ
# texts = json.loads(r.content) # делаем из полученных байтов python объект для удобной работы
# print(type(texts)) # проверяем тип сконвертированных данных
#
# for text in texts: # выводим полученный текст. Но для того чтобы он влез в консоль оставим только первые 150 символов.
#     print(text[:150], '\n')

# Давайте посмотрим теперь на ещё один тип возвращаемых значений. Он тоже будет JSON,
# но в данном случае он, скорее, будет похож на словарь.
#

# import requests
# import json
#
# r = requests.get('https://api.github.com')
#
# d = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы
#
# print(type(d))
# print(d['following_url'])
# обращаемся к полученному объекту как к словарю и попробуем
# напечатать одно из его значений

# Таким образом мы можем удобно превращать данные, полученные из ответа JSON, в объекты структур
# данных Python с помощью библиотеки JSON, и удобно работать с ними.


# Как вы могли заметить, здесь мы использовали только get-запросы (применяли функцию .get()
# из библиотеки requests). Однако одним из наиболее распространённых запросов, помимо get ,
# является post-запрос. Если же get используется, как правило, для получения данных
# (например, JSON-ответ или HTML-код для браузера, как мы уже увидели), то при помощи post-запросов
# отправляются данные для обработки на сервер. Например, чаще всего вместе с post-запросом используются
# параметры (data) для записи каких-либо новых данных в базу данных.


# Напишите программу, которая отправляет запрос на генерацию случайных текстов (используйте этот сервис).
# Выведите первый из сгенерированных текстов.

# import requests
# import json
#
# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
# q = json.loads(r.content)
#
# # отправляем пост запрос, но только в этот раз тип передаваемых данных будет JSON
# print(q[0])
