import pytest
from fixture_and_parametrize_22Modul_PyTest_API.api import PetFriends
from fixture_and_parametrize_22Modul_PyTest_API.settings import valid_password, valid_email, invalid_email, invalid_age, invalid_name
import os

pf = PetFriends()


"""Напишем вспомогательную функцию, которая будет генерировать нам строку длиной в n символов в файле теста:"""


def generate_string(n):
    return "x" * n


def russian_chars():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


# Здесь мы взяли 20 популярных китайских иероглифов
def chinese_chars():
    return '的一是不了人我在有他这为之大来以个中上们'


def special_chars():
    return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'


@pytest.mark.parametrize("filter",
                         [''
                             , 'my_pets'
                             , generate_string(255)
                             , generate_string(1001)
                             , russian_chars()
                             , russian_chars().upper()
                             , chinese_chars()
                             , special_chars()
                             , 123
                          ]
    , ids=['empty string'
        , 'only my pets'
        , '255 symbols'
        , 'more than 1000 symbols'
        , 'russian'
        , 'RUSSIAN'
        , 'chinese'
        , 'specials'
        , 'digit'])
@pytest.fixture(autouse=True)
def get_key():
    status, pytest.key = pf.get_api_key(valid_email, valid_password)
    assert status == 200
    assert 'key' in pytest.key
    return pytest.key


# def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
#     status, result = pf.get_api_key(email, password)
#     assert status == 200
#     assert 'key' in result

def test_get_all_pets_with_negative_filter(filter):
    pytest.status, result = pf.get_list_of_pets(pytest.key, filter)

    # Проверяем статус ответа
    assert pytest.status == 400


@pytest.mark.parametrize("filter",
                         ['', 'my_pets'],
                         ids=['empty string', 'only my pets'])
def test_get_all_pets_with_valid_key(filter):
    pytest.status, result = pf.get_list_of_pets(pytest.key, filter)

    # Проверяем статус ответа
    assert pytest.status == 200
    assert len(result['pets']) > 0


# def test_get_all_pets_with_valid_key(filter):
#     """ Проверяем, что запрос всех питомцев возвращает не пустой список.
#    Для этого сначала получаем api-ключ и сохраняем в переменную auth_key. Далее, используя этот ключ,
#    запрашиваем список всех питомцев и проверяем, что список не пустой.
#    Доступное значение параметра filter - 'my_pets' либо '' """
#
#     pytest.status, result = pf.get_list_of_pets(pytest.key, filter)
#
#     assert len(result['pets']) > 0





def test_get_api_key_for_invalid_user(email=invalid_email, password=valid_password):
    """" Проверяем, что запрос ключа для несуществующего пользователя не возвращает
    статус 200"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
    status = pf.get_api_key(email, password)
    # Проверяем:
    assert status != 403


def test_get_all_pets_with_valid_key(get_key, filter=''):
    auth_key = get_key
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(get_key, name='Барбоскин', animal_type='двортерьер',
                                     age='4', pet_photo='images/cat_1.jpeg'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    auth_key = get_key

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_invalid_name(name=invalid_name, animal_type='двортерьер',
                                       age='4', pet_photo='images/cat_1.jpeg'):
    """Проверяем что можно добавить питомца с  не валидным именем"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_invalid_age(name=invalid_name, animal_type='двортерьер',
                                      age=invalid_age, pet_photo='images/cat_1.jpeg'):
    """Проверяем что можно добавить питомца с  не валидным именем"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_information_about_pet_without_photo(name='Пингвинятина', animal_type='Млекосос', age='54'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_information_about_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200


def test_add_photo_for_pet(pet_photo='images/1877085.jpeg'):
    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Добавляем фото
    pet_id = my_pets['pets'][1]['id']
    status, result = pf.add_photo_of_pet(auth_key, pet_id, pet_photo)
    # Сверяем полученный ответ с ожидаемым результатом

    assert status == 200


def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев не пустой, Берём id первого питомца
    # из списка и отправляем запрос на удаление и опять запрашиваем список своих питомцев
    assert len(my_pets['pets']) > 0
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Берём id первого питомца из списка и отправляем запрос на удаление

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_pet_info_negative_age(name='Мурзик', animal_type='Котэ', age=-5):
    """Проверяем возможность обновления информации о питомце c отрицательным значением возраста"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    assert len(my_pets['pets']) > 0
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
    assert status == 200
    assert result['name'] == name


def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    assert len(my_pets['pets']) > 0, "There is no my pets"
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
    assert status == 200
    assert result['name'] == name
