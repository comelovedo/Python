

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Settings import valid_email, valid_password

driver = webdriver.Chrome


@pytest.fixture(autouse=True)
def testing():
    # Specify the path to the webdriver
    pytest.driver = webdriver.Chrome('/Users/bazucer/Desktop/IT/chromedriver')
    # Go to the login page
    pytest.driver.get('http://petfriends1.herokuapp.com/login')
    # Input email
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
    # Input pass
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
    # Click on the login button
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Check that we are on the main page of the user
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    yield

    pytest.driver.close()


# Checking for the presence of all my pets:
def test_show_all_my_pets():
    # Press the "Мои питомцы" button to open the page with the table of the user's pets
    pytest.driver.find_element_by_partial_link_text('Мои питомцы').click()
    # Checking that we have landed on the page with the user's pet table
    # Explicit wait, applicable for educational purposes only
    # Explicit Waits:
    try:
        element = WebDriverWait(pytest.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'smart_cell'))
        )
    finally:
        locator_for_all_my_pets = pytest.driver.find_elements_by_xpath('//td[@class="smart_cell"]')
        # We check the presence of my pets (on request, we take the number of animals from statistics)
        quantity_of_my_pets_from_user_statistic = 3
        assert len(locator_for_all_my_pets) == quantity_of_my_pets_from_user_statistic


# Checking the parameters of pet cards:
def test_card_my_pets():
    images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
    descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')
    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0


# Checking if at least half of my pets have a photo:
def test_half_of_my_pets_with_photo():
    pytest.driver.find_element_by_xpath('//a[contains(text(), "Мои питомцы")]').click()
    # Selecting my pets with the locator of the delete animal button
    locator_for_all_my_pets = pytest.driver.find_elements_by_xpath('//td[@class="smart_cell"]')
    # Select all elements of the user's pet photos
    images = pytest.driver.find_elements_by_xpath('//th/img')
    # Set variable to count the number of user's pets with a photo
    number_of_pets_with_photo = 0
    # We set implicit waits (seconds) for student purposes only.
    pytest.driver.implicitly_wait(5)
    # By checking for all pets that attribute 'src' is not an empty value, we determine
    # number of pets with photo
    for i in range(len(locator_for_all_my_pets)):
        if images[i].get_attribute('src') != '':
            number_of_pets_with_photo += 1
        else:
            number_of_pets_with_photo = number_of_pets_with_photo
    # Check that as min half of all pets has a photos
    assert number_of_pets_with_photo >= (len(locator_for_all_my_pets) / 2)


# Checking that all "my pets" has a name, type (breed) and age:
def test_all_my_pets_with_name_type_age():
    # Press the "Мои питомцы" button to open the list of the user's pets
    pytest.driver.find_element_by_xpath('//a[contains(text(), "Мои питомцы")]').click()
    # Selecting my pets with the locator of the delete animal button
    locator_for_all_my_pets = pytest.driver.find_elements_by_xpath('//td[@class="smart_cell"]')

    for i in range(len(locator_for_all_my_pets)):
        # for the locator_for_all_my_pets element (the button for deleting a pet), we find all three
        # neighbors tag "td" corresponding to the name, type and age of the pet
        pet = locator_for_all_my_pets[i].find_elements_by_xpath('preceding-sibling::td')
        # find the text of the "td" tag with index [2] corresponding to the name of the pet
        # and set variable "name"
        name = pet[2].text
        # Setting implicit waits (seconds), for educational purposes only
        pytest.driver.implicitly_wait(5)
        # find the text of the "td" tag with the index [1] corresponding to the pet type
        # and set variable "animal type"
        anymal_type = pet[1].text
        pytest.driver.implicitly_wait(5)
        # find the text of the "td" tag with index [0] corresponding to the age of the pet
        # and set variable "age"
        age = pet[0].text
        pytest.driver.implicitly_wait(5)
        # check that each pet has a name, type and age
        assert name != ''
        assert anymal_type != ''
        assert age != ''


# Checking if all 'Мои питомцы' has different names:
def test_all_my_pets_with_different_names():
    # Press the "Мои питомцы" button to open the list of the user's pets
    pytest.driver.find_element_by_xpath('//a[contains(text(), "Мои питомцы")]').click()
    # Selecting my pets with the locator of the delete animal button
    locator_for_all_my_pets = pytest.driver.find_elements_by_xpath('//td[@class="smart_cell"]')
    # Create an empty list for the user's pet names
    list_of_pets_names = []
    for i in range(len(locator_for_all_my_pets)):
        # for the locator_for_all_my_pets element (the button for deleting a pet), we find all three
        # neighboring "td" tags corresponding to the name, type and age of the child
        pet = locator_for_all_my_pets[i].find_elements(By.XPATH, 'preceding-sibling::td')
        # find the text of the "td" tag with index 2 corresponding to the name of the pet
        # and sat variable "name"
        name = pet[2].text
        # add the pet's name to list_of_pets_names
        list_of_pets_names.append(name)
    # to check if the pet name is unique, check the number of occurrences of each
    # name in list of pet names
    for name in list_of_pets_names:
        assert list_of_pets_names.count(name) == 1
