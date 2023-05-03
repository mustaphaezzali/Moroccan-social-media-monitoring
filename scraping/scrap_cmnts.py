from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import os
import hashlib
from utils import transform
import datetime
import json

driver = webdriver.Chrome('.\chromedriver.exe')

def ferch_urls():
    urls_cats = []
    with open('hespress.csv', 'r',encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            urls_cats.append((row[2],row[3]))
    urls_cats.pop(0)
    return urls_cats
urls_cats = ferch_urls()
all_comments = []
number_comments = 0
for i in range(len(urls_cats)):
    try:
        url = urls_cats[i][0]
        cat = urls_cats[i][1]
        driver.get(url)
        comments = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'comment-body')]//p")))
        dates = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'comment-date')]")))
        authors = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'comment-author vcard')]")))
        print(len(comments),len(dates),len(authors))
        number_comments += len(comments)
        print(comments[0].text)
        for i in range(len(comments)):
            comments[i] = comments[i].text
            all_comments.append(comments[i])
    except:
        continue
with open('comments.csv',mode='a',encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["comment"])
        for j in range(len( all_comments)):
            writer.writerow([all_comments[j]])
      
print("comments number: ",number_comments)
    