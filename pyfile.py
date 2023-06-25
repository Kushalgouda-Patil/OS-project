import pandas as pd
import re
import sys
import time
import os
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
usn=''
dd=''
mm=''
yyyy=''
def print_with_decoration(text):
    print("\033[1;31m" + text + "\033[0m"+'\U0001F60C')

def save_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
def read_file():
    try:
        with open('login.txt', 'r') as fp:
            globals()['usn'] = fp.readline()
            globals()['dd'] = fp.readline()
            globals()['mm'] = fp.readline()
            globals()['yyyy'] = fp.readline()
    except FileNotFoundError:
        print('The file login.txt does not exist.')
        sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)
def main():
    print_with_decoration("Sit back and relax until captcha image pops up")
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    url="https://parents.kletech.ac.in/kletechparenteven2023/"
    driver.get(url)
    soup=BeautifulSoup(driver.page_source,features="html.parser")
    read_file()
    driver.find_element(by='id',value="username").send_keys(usn)
    driver.find_element(by='id',value="dd").send_keys(dd)
    driver.find_element(by='id',value="mm").send_keys(mm)
    driver.find_element(by='id',value="yyyy").send_keys(yyyy)
    image_div = soup.find_all("img")  
    link=str(image_div[-1])
    image_link = url+re.search(r'src="([^"]+)"', link).group(1)# type:ignore
    image_link=image_link.replace("amp;", "")
    #print(image_link)
    save_image(image_link, "captcha.png")
    os.system('xdg-open captcha.png ')
    cpa=input("Enter capthcha :")
    driver.find_element(by='id',value="security_code").send_keys(cpa)
    driver.find_element(by="xpath",value='//*[@id="loginPanel"]/div/div[6]/button').click()
    soup=BeautifulSoup(driver.page_source,features="html.parser")
    name=soup.find_all('div',class_="tname2")[0].text.strip()
    semester=soup.find_all('div',class_="tname2")[2].text.strip().split()[1]
    courses=soup.find_all('div',class_="coursename")
    attendence=soup.find_all('a',title="Attendence")
    marks=soup.find_all('div',class_='cie')
    print("\033[92m"+'Here you go......')
    print(f"Name\t {name}\nSemester {semester}"+"\033[0m")
    marks_list=list()
    course_list=list()
    attendence_list=list()
    for i in range(len(courses)):
        course_list.append(courses[i].text)
        attendence_list.append(attendence[i*2].text)
        marks_list.append(marks[i].text.strip('\nInternal Assessment'))
    df=pd.DataFrame({'Attendence':attendence_list,'Marks':marks_list},index=course_list)

    print(df)
    df.to_csv('data.csv')
    driver.quit()
if __name__=='__main__':
    main()