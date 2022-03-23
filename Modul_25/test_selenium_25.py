
import time
import pytest
from selenium import webdriver



@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('/users/bazucer/desktop/it/python/Modul_25/chromedriver')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends1.herokuapp.com/login')

    yield

    pytest.driver.quit()


def test_show_my_pets():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('Bazucer@gmail.com')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('qwerty555')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"


def test_internal():
    all_my_pets = pytest.driver.find_elements_by_css_selector('.all_my_pets.table.table-hover.marked-element')
    for i in range(len(all_my_pets)):
        assert all_my_pets.get_attribute('row') == 230
