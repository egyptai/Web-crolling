# -*- coding: utf-8 -*-
"""
Created on Fri May 21 14:26:37 2021

@author: dms10
"""

import requests
from bs4 import BeautifulSoup


url = "https://search.daum.net/search?w=tot&q=2019%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
images = soup.find_all("img", attrs={"class":"thumb_img"})

for idx, image in enumerate(images):
    print(image["src"])
    img_url = (image["src"])
    if img_url.startswith("//"):
        img_url = "https:" + img_url
            
    img_res = requests.get(img_url)
    img_res.raise_for_status()
    
    with open("movie{}.jpg".format(idx+1), "wb") as f:
        f.write(img_res.content)
        
    if idx >= 4:
        break;