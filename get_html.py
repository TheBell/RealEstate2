

import urllib.request
import sys
import zillow_functions  as zl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

# Initialize the webdriver.
driver = zl.init_driver("C:/Programming/RealEstate/Zillow-master/chromedriver.exe")
output = []

# Go to www.zillow.com/homes
zl.navigate_to_website(driver, "http://www.zillow.com/homes")

def get_home_html(url):
    try:
        zl.navigate_to_website(driver, url)
        output.append(driver.page_source)
        print("Scraped: " + url)
    except:
        print("Invalid url: " + url)
    

def read_url(url, file):
    try:
        f = urllib.request.urlopen(url)
        html = ""
        for line in f:
            html += line.decode() +"\r\n"
        file.write(html)
        print("Scraped: " + url)

    except:
        print("Invalid url: " + url)
    
def get_url_list(file_name):
    urls = []
    with open(file_name, "r") as file:
        for line in file:
            url = line.split(",")[-1][:-1]
            urls.append(url)
    return urls[1:]
              
        

if __name__ == "__main__":
    csv_file = sys.argv[1]
    urls = get_url_list(csv_file)
    
    for url in urls[:10]:
        get_home_html(url)
    
    with open(sys.argv[2], "a") as file:
        for home in output:
            file.write(home)
            file.write("###")
    
    
    
    