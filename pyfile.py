import pandas as pd
import re
import csv
import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url="https://parents.kletech.ac.in/kletechparenteven2023/"
driver.get(url)
soup=BeautifulSoup(driver.page_source,features="html.parser")
usn='01fe21bci051'
dd=26
mm='Jul'
yyyy='2003'
driver.find_element(by='id',value="username").send_keys(usn)
driver.find_element(by='id',value="dd").send_keys(dd)
driver.find_element(by='id',value="mm").send_keys(mm)
driver.find_element(by='id',value="yyyy").send_keys(yyyy)
image_div = soup.find_all("img")  
link=str(image_div[-1])
image_link = url+re.search(r'src="([^"]+)"', link).group(1)# type:ignore
#print(image_link.replace("amp;", ""))
cpa=input("Enter capthcha :")
driver.find_element(by='id',value="security_code").send_keys(cpa)
driver.find_element(by="xpath",value='//*[@id="loginPanel"]/div/div[6]/button').click()
soup=BeautifulSoup(driver.page_source,features="html.parser")
name=soup.find_all('div',class_="tname2")[0].text.strip()
semester=soup.find_all('div',class_="tname2")[2].text.strip().split()[1]
courses=soup.find_all('div',class_="coursename")
attendence=soup.find_all('a',title="Attendence")
marks=soup.find_all('div',class_='cie')

print(f"Name {name}\nSemester {semester}")
marks_list=list()
course_list=list()
attendence_list=list()
for i in range(len(courses)):
    course_list.append(courses[i].text)
    attendence_list.append(attendence[i*2].text)
    marks_list.append(marks[i].text.strip('\nInternal Assessment'))
df=pd.DataFrame({'Attendence':attendence_list,'Marks':marks_list},index=course_list)

print(df)
driver.quit()