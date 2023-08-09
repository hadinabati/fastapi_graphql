import datetime
import hashlib
import os

from dotenv import load_dotenv

from database.mongodb import user_db
from instance.error_instance import Error
from instance.mongo_instance import Names
from models.jwt_model import Token
from schema.register_schema import User, Register
from schema.register_schema import Error as ErrorClass


class UserRegister:
    def __init__(self, username: str = None, token: str = None):
        self.username = username
        self.token = token
        self.mongo_name = Names()
        self.error = Error()

    def check_exist_user(self) -> bool:
        count = user_db.count_documents({
            self.mongo_name.username: self.username
        })
        if count > 0:
            return True
        else:
            return False

    def create_user(self, user_info: Register) -> ErrorClass | User:
        check = self.check_exist_user()
        date = datetime.datetime.now()
        if check:
            return ErrorClass(error_code=self.error.Register.code_1001, message_code=self.error.Register.message_1001)
        else:
            token_class = Token()
            token = token_class.encode(username=user_info.username)
            if token is False:
                return ErrorClass(error_code=self.error.Register.code_1003, message_code=self.error.Register.message_1003)

            load_dotenv()
            extra = str(os.getenv("extra"))
            new_pass = user_info.password + extra
            hashed_password = hashlib.md5(new_pass.encode())

            res = user_db.insert_one({
                self.mongo_name.username: user_info.username,
                self.mongo_name.name: user_info.name,
                self.mongo_name.family: user_info.family,
                self.mongo_name.Email: '',
                self.mongo_name.image: '',
                self.mongo_name.password: str(hashed_password),
                self.mongo_name.update_at: date,
                self.mongo_name.create_at: date,
                self.mongo_name.men_sex: None,
                self.mongo_name.role: self.mongo_name.role_user,
                self.mongo_name.token: token,
                self.mongo_name.money: 0

            }).acknowledged
            if not res:
                return ErrorClass(error_code=self.error.Register.code_1002, message_code=self.error.Register.message_1002)
            else:
                return User(
                    family=user_info.family, token=token, name=user_info.name, role=self.mongo_name.role_user,
                    image="", men_sex=None, money=0, Email="", create_date=date, updated_at=date
                )
