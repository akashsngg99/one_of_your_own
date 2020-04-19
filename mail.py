# Python code to illustrate Sending mail
# to multiple users
# from your Gmail account
#r'C:\Users\AKASH\Desktop\chromedriver.exe'
import smtplib

import requests
from bs4 import BeautifulSoup
import schedule
import time
import csv
import numpy as np
from tkinter import *



def oo(fuu):
    #with open('Book1.csv','a') as f:
    with open(r'C:\Users\AKASH\Desktop\Book1.csv','a') as f:
        w=csv.writer(f)
        w.writerow(fuu)        


def corona():
    url = 'https://www.worldometers.info/coronavirus/country/india/'
    webpage_response = requests.get(url)

    webpage = webpage_response.content
    soup = BeautifulSoup(webpage, "html.parser")
    soup.prettify()

    # print(soup)

    # print(soup.find_all('div',class_='confirmed'))
    # items=soup.find_all(id='maincounter-wrap')
    items = soup.find_all(class_='maincounter-number')
    # print(items)
    # print(len(items))
    te=[]
    for i in range(0, len(items)):
        
        temp = (items[i].get_text()).replace(",","")
        te.append((items[i].get_text()))
        print(temp)
        df=np.array(te)
        #print(df)

    #print(te)
    oo(df)
    return te 

    #upload(df)




# list of email_id to send the mail
li = ["sngg99.akash@gmail.com", "akash.sngg2k17@gmail.com"]
te=corona()
for i in range(len(li)):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("akash.sngg99@gmail.com", "pgssehwyfvnwifpp")
    message = "\n\n\t\t\t\t Covid19 Information In India\n\n\nTotal Affected:"+str(te[0])+" Total Deaths : "+str(te[1])+"Total Recoverd: "+str(te[2])+"\n"
    s.sendmail("akash.sngg99@gmail.com", li[i], message)
    print("Done")
    s.quit()
#driver = webdriver.Chrome('C:/Users/AKASH/Desktop/chromedriver') 
