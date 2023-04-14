from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome('.\chromedriver.exe')

#driver.get('https://www.hespress.com/')

categories = ["https://www.hespress.com/politique",
              "https://www.hespress.com/regions",
              "https://www.hespress.com/societe",
              "https://www.hespress.com/economie",
              "https://www.hespress.com/faits-divers",
              "https://www.hespress.com/medias",
              "https://www.hespress.com/art-et-culture",
              "https://www.hespress.com/sport",
              "https://www.hespress.com/tamazight",
            ]

driver.get(categories[0])
driver.implicitly_wait(10)
driver.maximize_window()
#cards = driver.find_element(By.XPATH,"//div[@class='col-12 col-sm-6 col-md-6  col-xl-4']")
#cards = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'col-12')]")))
#time.sleep(5)
#links = driver.find_elements(By.XPATH,"//a[@class='stretched-link']//@href")
#links = driver.find_element(By.XPATH,"//a[@class='stretched-link']//@href")
links =  WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH,"//a[contains(@class,'stretched-link')]")))

urls = []
for link in links:
    url = link.get_attribute('href')
    urls.append(url)

# Print the extracted links
print(urls)

