# -*- coding: utf-8 -*-
"""
Created on Fri May 21 13:17:50 2021

@author: dms10
"""

from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8")
#pprint(html.text)

soup = bs(html.text, "html.parser")
dust = soup.find("div", {"class":"detail_box"})
print(dust)
