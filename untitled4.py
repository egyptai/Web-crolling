# -*- coding: utf-8 -*-
"""
Created on Fri May 21 10:53:40 2021

@author: dms10
"""

import bs4 

html_str = """
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>
"""
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
ul = bs_obj.find("ul")
lis = ul.findAll("li")
print(li)
print(li.text)
