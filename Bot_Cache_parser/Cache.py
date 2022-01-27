import redis
import json

red = redis.Redis(host='localhost',
                  port=6379,
                  password="")

# dict1 = {'key1': 'value1', 'key2': 'value2'}  # Созаем словарь для записи
# red.set('dict1', json.dumps(dict1))# С помощью dumps() из модуля json превратим наш словарь в строку
# print(type(dict1))
# converted_dict = json.loads(red.get('dict1'))  # с помощью знакомой нам функции превращаем данные
# # полученные из кэша обратно в словарь
# print(type(converted_dict))  # убеждаемся, что получили действительно словарь
# print(converted_dict)

red.delete('dict1')  # удаляются ключи с помощью метода .delete()
print(red.get('dict1'))
