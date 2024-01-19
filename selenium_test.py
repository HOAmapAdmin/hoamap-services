from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.python.org")
print(driver.title)

driver.implicitly_wait(120)
# element = driver.find_element_by_id("homepage")
element = driver.find_element(By.ID, "homepage")
print(element)

driver.close()

# try:
#     element = WebDriverWait(driver, 120).until(
#         EC.presence_of_element_located((By.ID, "homepage"))
#     )
#     print(element)
# finally:
# search_bar = driver.find_element_by_name("description")
# search_bar.clear()
# search_bar.send_keys("getting started with python")
# search_bar.send_keys(Keys.RETURN)
# print(driver.current_url)
    # driver.close()
    # driver.quit()