
import requests
from bs4 import BeautifulSoup




schools = soup.find_all("span", {"class" : "gs-rating-number"})

if schools is not None:
    schools = (schools[0].get_text(), schools[1].get_text(), schools[2].get_text())
    
print(schools)

schools = soup.find_all("span", {"class" : "gs-rating-number"})
s = ["NA", "NA", "NA"]
for i in range(len(schools)):
    s[i] = schools[i].get_text()
    
print(s)