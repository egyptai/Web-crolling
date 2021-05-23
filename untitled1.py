# -*- coding: utf-8 -*-
"""
Created on Thu May 20 17:49:45 2021

@author: dms10
"""

from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
pprint(html.text)

soup = bs(html.text, 'html.parser')