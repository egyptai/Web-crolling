# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests

res = requests.get("http://naver.com")
#res = requests.get("http://yyy.tistory.com")

if res.status_code == requests.codes.ok:
    print("정상")
    
else:
    print("오류 : ", res.status_code)

print("status_code :", res.status_code)

res.raise_for_status()
print("정상입니다.")
print(len(res.text))