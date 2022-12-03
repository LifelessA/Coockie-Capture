import requests as rq

import urllib
import http.cookiejar

inp = input("Enter the url : ")
URL = f"https://{inp}"

headers = {'content-type':'multipart/form-data'}

r = rq.get(f"{URL}/post",headers=headers)
rr = r.headers
rrr = r.request.headers


for j in rrr:
    print(f"{j} : {rrr[j]}")

for i in rr:

    print(f"{i} : {rr[i]}")

for i in range(0,2):
    print("")



def ex_cookies():
    cookie_jar = http.cookiejar.CookieJar()

    url_opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))

    url_opener.open(URL)

    for cookie in cookie_jar:
        print("%s : %s" %(cookie.name, cookie.value))



ex_cookies()