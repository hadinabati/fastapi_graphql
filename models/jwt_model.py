import datetime
import os
import json
from dotenv import load_dotenv
from jose import jwt

load_dotenv()


class Token:
    def __init__(self):
        self.key = os.getenv("secret_key")

    def encode(self, username: str = None, id: str = None) -> str | bool:
        try:
            data = {
                "id": id,
                'username': username,
                'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            }
            token = jwt.encode(data, self.key, algorithm='HS256')
            return token
        except IndexError:
            return False

    def decode(self, token: str = None) -> str | bool:
        try:
            payload = jwt.decode(token, self.key, algorithms=['HS256'])
            return payload["id"]
        except Exception:
            return False

    def check_time(self, token: str = None) -> bool:
        data = jwt.decode(token, self.key, algorithms=['HS256'])
        time: str = data["date"]
        diff = (datetime.datetime.now() - datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")).seconds
        if diff > 5:
            return False
        else:
            return True

    def refresh_token(self, token: str = None) -> str:
        payload = jwt.decode(token, self.key, algorithms=['HS256'])
        new_token = self.encode(username=payload['username'], id=payload['id'])
        return new_token
