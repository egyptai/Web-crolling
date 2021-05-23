# -*- coding: utf-8 -*-
"""
Created on Fri May 21 17:46:41 2021

@author: dms10
"""

import requests
import csv
from bs4 import BeautifulSoup
url = "http://www.cgs.or.kr/business/esg_tab04.jsp?pg=1&pp=10&skey=&svalue=&sfyear=2020&styear=2020&sgtype=TOTAL&sgrade=A%EF%BC%8B#ui_contents"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "html.parser")
table = soup.find("div", {"class", "business_board"})

data = []
for row in table.findAll("tr"):
    cols = row.findAll("td")
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])
    
    print(cols)