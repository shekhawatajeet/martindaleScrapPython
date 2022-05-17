import os
from selenium import webdriver
import csv
import urllib
import requests
import re
from bs4 import BeautifulSoup
headers = {
    "User-agent": "Chrome/100.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}

main_dir = os.getcwd() + '\\'
if not os.path.exists(main_dir):
    os.mkdir(main_dir)
    

# Name of the CSV File
file_name = 'Task.csv'
# Path of the CSV File
file_path = main_dir + file_name

# Writing to the CSV File
with open(file_path, mode='w') as file:
    writer = csv.writer(file, delimiter=',', lineterminator='\n')
    # Adding the Column Names to the CSV File
    writer.writerow(
        ['Person name', 'Bar number','Profile Link', 'Title','Company Name', 'Address',
        'Phone Number', 'Cell','Fax', 'Email','Website', 'Board Certifications','Email Validation',
         ])
    #enter the value of Quary As Requriement.
    Quary=500
    print(f'\nScraping in progress...\n')
    url = "https://www.martindale.com/all-lawyers/new-york/new-york/?pageSize="+str(Quary)
    response = requests.get(url, headers=headers)
    html = response.text
    #Scrapping the Web
    soup = BeautifulSoup(html, 'lxml')
    people = soup.find_all("li", class_="detail_title")
    t=1;
    for person in people:
        detail =person.find("a", class_="opt-d-title")
        profilelink= detail["href"]
        name =detail.text
        
        url = profilelink
        #for scraping data from profile
        response = requests.get(url, headers=headers)
        html = response.text

        soup = BeautifulSoup(html, 'lxml')
        #Title from profile
        title =soup.find("title").text
        
        
        profile = soup.find("div", class_="attorney-profile-content profile-content")
        #company Where he works
        comp =soup.find("a",class_="link link--gray").text
        
        #mobile number
        m =soup.find("div",class_="small-12 medium-9 columns experience-value")
        mob = m.find("span")
        if (mob == None):
            mobile ="Not Present"
        else:
             mobile=mob.text
        #website
        web = profile.find("a" ,class_="navigable view-website webstats-website-click btn btn--white")
        
        if (web ==None):
            website ="Not Present"
        else:
            website =web["href"]
        #Address
        address =soup.find("address").text
        board = profile.find("div" ,id="education-section").text
        #for geting law university 
        text = board;
        left = 'Law School Attended'
        right = 'Year of First Admission'
        try:
            board_certificate = text[text.index(left)+len(left):text.index(right)];
        except:
            board_certificate ="Data Not Present"
        #cell number

        left = 'Phone'
        right = 'Cell'
        try:
            cell = text[text.index(left)+len(left):text.index(right)];
        except:
            cell ="Cell Numer Is Not Present"
        
        #ISLN Number
        Bar = board.split()
        Bar_number = Bar[-1]
        
        

        
        #getting fax
        FaxFinding = soup.find("div",class_="small-12 medium-9 columns experience-value").text
       
        text = FaxFinding;
        left = 'Phone'
        right = 'Fax'
        try:
            Fax = text[text.index(left)+len(left):text.index(right)];
        except:
            Fax ="Fax Number Not Given"


        #To count the number of loop
        print(t)

        t+=1
        # Writing to CSV File
        writer.writerow( [name, Bar_number ,profilelink ,title ,comp ,address ,mobile ,cell,Fax,"email not present",website,board_certificate ,"not known"])
        
                     
print('Task done successfully.');

