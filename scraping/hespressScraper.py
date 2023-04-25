from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

driver = webdriver.Chrome('.\chromedriver.exe')


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

for i in range(len(categories)):
    driver.get(categories_links[i])
    driver.implicitly_wait(10)
    driver.maximize_window()

    for k in range(10):
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

    with open('hespress.csv',mode='a',encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        #writer.writerow(["Title", "Date", "URL", "Category"])
        for j in range(len(titles)):
            writer.writerow([titles[j], dates[j], urls[j], categories[i]])

# Print the extracted links
print(dates,len(dates),len(urls))

