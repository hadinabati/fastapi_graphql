import datetime
import os
import json
from dotenv import load_dotenv
from jose import jwt

load_dotenv()


class Token:
    def __init__(self):
        self.key = os.getenv("secret_key")

    def encode(self, username: str) -> str | bool:
        try:
            data = {
                'username': username,
                'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            }
            token = jwt.encode(data, self.key, algorithm='HS256')
            return token
        except IndexError:
            return False

    def decode(self, token: str = None) -> str | bool:
        try:
            data = jwt.decode(token, self.key, algorithms=['HS256'])
            return data["username"]
        except IndexError:
            return False

    def check_time(self, token: str = None) -> bool:
        data = jwt.decode(token, self.key, algorithms=['HS256'])
        time: datetime.datetime = data["date"]
        diff = (datetime.datetime.now() - time.strptime("%Y-%m-%d %H:%M:%S")).seconds
        if diff > 1800:
            return False
        else:
            return True
