from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import urllib
import csv
import os
import urllib.request
import time
from bs4 import BeautifulSoup

try :
    os.mkdir(os.path.join(os.getcwd(),'icon'))
except:
    pass
os.chdir(os.path.join(os.getcwd(),'icon'))
file_path = '1aaa_Problem_Data.csv'
imageLocation ='C:/Users/Parveen bhai/Desktop/blog-wordpress/blog/imageProblem/icon'
with open(file_path, mode='w') as file:
    writer = csv.writer(file, delimiter=',', lineterminator='\n')
    # Adding the Column Names to the CSV File
    writer.writerow(
        ['Name of Disease', 'URLs associated with diseases','ImageName'])
    url = 'https://dermnetnz.org/image-library/imagesJson'
    response = requests.get(url)
    r = requests.get(url)
    cont = r.json()
    for k in cont:
        url ='https://dermnetnz.org'+k['url']
        Name=k['name']
        urlimage=k['thumbnail']
        ImageName = os.path.basename(urlimage)
        with open(ImageName,'wb') as f:
            im=requests.get(urlimage)
            f.write(im.content)
        print(Name)
        writer.writerow( [Name, url,ImageName])
    

