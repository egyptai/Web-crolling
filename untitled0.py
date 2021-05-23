# -*- coding: utf-8 -*-
"""
Created on Thu May 20 17:37:08 2021

@author: dms10
"""

from urllib.request import urlopen

url = "https://www.naver.com"
html = urlopen(url)
print(html.read())

from urllib.request import urlopen
from urllib.request import HTTPError

try:
    html = urlopen("http://www.dddsdf.com/kim.html")
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    print("성공")