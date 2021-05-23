# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:28:45 2021

@author: dms10
"""

bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
ul = bs_obj.find("ul", {"class" : "reply"})
print(ul)