from selenium import webdriver
driver = webdriver.Chrome()

selenium.get('https://google.com')
selenium.quit()
search_input = selenium.find_element_by_name('q')