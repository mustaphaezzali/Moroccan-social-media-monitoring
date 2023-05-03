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
driver = webdriver.Chrome('.\chromedriver.exe')

def ferch_urls(start_date,end_date):
    urls_cats = []
    with open('hespress.csv', 'r',encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                date = transform(row[1])[0]
                if start_date <= date and date <= end_date:
                    print(row[2])
                    urls_cats.append((row[2],row[3]))
            except:
                print("error")
    urls_cats.pop(0)
    return urls_cats
urls_cats = ferch_urls(datetime.date(2023,3,29),datetime.date(2023,4,29))
for i in range(len(urls_cats)):
    url = urls_cats[i][0]
    cat = urls_cats[i][1]
    driver.get(url)
    paragraphs = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'article-content')]//p")))
    text = []
    for p in paragraphs:
        p = p.text
        text.append(p)
    print(text)
    full_text = '\n '.join(text)


    document_text = full_text
    document_hash = hashlib.sha256(document_text.encode()).hexdigest()
    document_id = f"document_{document_hash}"
    filename = f"{document_id}.txt"
    subfolder = cat
    main_folder = "./Docs"
    folder = os.path.join(main_folder, subfolder)
    if not os.path.exists(folder):
        os.makedirs(folder)
    filename = os.path.join(folder, filename)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(document_text)