from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get('http://www.google.com/xhtml')
driver.maximize_window()
try:
    element = driver.find_element_by_name('q')
    ispis = element.text
    print(ispis)
except:
    print('Nije pronadjen element sa imenom: \"q\".')
