
import time


def test_petfriends(web_browser):
    # Open PetFriends base page:
    web_browser.get("https://petfriends1.herokuapp.com/")

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    # click on the new user button
    btn_newuser = web_browser.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]")
    btn_newuser.click()

    # click existing user button
    btn_exist_acc = web_browser.find_element_by_css_selector("form > div:nth-of-type(4) > a")
    btn_exist_acc.click()

    # add email
    field_email = web_browser.find_element_by_css_selector("input#email")
    field_email.clear()
    field_email.send_keys("Bazucer@gmail.com")

    # add password
    field_pass = web_browser.find_element_by_css_selector("input#pass")
    field_pass.clear()
    field_pass.send_keys("qwerty555")

    # click submit button
    btn_submit = web_browser.find_element_by_css_selector("div:nth-of-type(3) > button")
    btn_submit.click()

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!
    # Checking if element on the page.
    card_elem = web_browser.find_element_by_css_selector("div:nth-of-type(2) > div.card")
    if card_elem is None:
        print('There are no element')