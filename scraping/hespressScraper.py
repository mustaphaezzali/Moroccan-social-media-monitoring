from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

driver = webdriver.Chrome('.\chromedriver.exe')

#driver.get('https://www.hespress.com/')

categories_links = ["https://www.hespress.com/politique",
              "https://www.hespress.com/regions",
              "https://www.hespress.com/societe",
              "https://www.hespress.com/economie",
              "https://www.hespress.com/faits-divers",
              "https://www.hespress.com/medias",
              "https://www.hespress.com/art-et-culture",
              "https://www.hespress.com/sport",
              "https://www.hespress.com/tamazight",
            ]
categories = ["Politique",'regions','societe','economie','faits-divers','medias','art-et-culture','sport','tamazight']

driver.get(categories[0])
driver.implicitly_wait(10)
driver.maximize_window()
#cards = driver.find_element(By.XPATH,"//div[@class='col-12 col-sm-6 col-md-6  col-xl-4']")
#cards = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'col-12')]")))
#time.sleep(5)
#links = driver.find_elements(By.XPATH,"//a[@class='stretched-link']//@href")
#links = driver.find_element(By.XPATH,"//a[@class='stretched-link']//@href")
#wait for the page to scroll down
for i in range(10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
links =  WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH,"//a[contains(@class,'stretched-link')]")))
datetime = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'card-details')]//div"))) 
title = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'card-details')]//h3")))
titles = []
urls = []
dates = []

for link in links:
    url = link.get_attribute('href')
    urls.append(url)
for date in datetime:
    date = date.text
    dates.append(date)
for t in title:
    t = t.text
    titles.append(t)

with open('hespress.csv', 'w',encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Date", "URL"])
    for i in range(len(titles)):
        writer.writerow([titles[i], dates[i], urls[i]])

# Print the extracted links
print(dates,len(dates),len(urls))

