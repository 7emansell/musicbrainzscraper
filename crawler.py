from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import sys
import time

ba_list = []
area_list = []
name_list = []
url_list = []
og = pd.read_csv("file://localhost/Users/emansell/Desktop/urls.csv")
urls=og.values.flatten()

for url in urls:
    time.sleep(0.5) 
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    name = [x.text for x in soup.select('name')]
    area = [x.text for x in soup.select('area + name')]
    url_list.append(url)
    if (len(name) > 0):
        name_list.append(name[0])
    else:
        name_list.append(" ")
    if (len(area) > 0):
        area_list.append(area[0])
    else:
        area_list.append(" ")
             


# url = "https://musicbrainz.org/ws/2/artist/?query=artist:hall-of-fame"
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'lxml')
# name = soup.find('name') #[x.text for x in soup.select('name')]
# area = soup.select('area + name')[0]
# beginarea = soup.findChild(name)
# print(name, area.text, beginarea)


#  create dataframe from your lists
df = pd.DataFrame(list(zip(url_list, name_list, area_list)),
               columns =['url', 'name', 'area'])

df.to_csv('RESULTS>8.csv', index=False, errors='ignore')
