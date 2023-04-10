from selenium import webdriver
url = 'https://hub.docker.com'

driver = webdriver.Chrome()
driver.get(url)

is_title = driver.find_element(by='xpath', value='/html/head/title')

expected = 'Docker Hub Container Image Library | App Containerization'
print(is_title.text)


