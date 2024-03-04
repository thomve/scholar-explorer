import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
url = 'https://scholar.google.com/'
browser.get(url)

time.sleep(2)

id_input: str = 'gs_hdr_tsi'
test_input: str = 'reinforcement learning'
input_element = browser.find_element(By.ID, id_input)
input_element.send_keys(test_input)
input_element.send_keys(Keys.ENTER)

time.sleep(2)

print('title of the new page', browser.title)

parent_div = browser.find_element(By.ID, 'gs_res_ccl_mid')

child_elements = parent_div.find_elements(By.CLASS_NAME, 'gs_ri')

print(len(child_elements))

browser.quit()