from typing import Union

from bson import ObjectId
from database.mongodb import user_db
from instance.error_instance import Error
from instance.mongo_instance import Names
from models.jwt_model import Token
from schema.register_schema import User
from schema.register_schema import Error as ErrorClass


class UserInformation:
    def __init__(self, token: str = None):
        self.token = token
        self.mongo_name = Names()
        self.error = Error()

    def user_(self) -> Union[ErrorClass, User]:
        if self.token is None:
            return ErrorClass(error_code=self.error.User.code_1004, message_code=self.error.User.message_1004)

        token_model = Token()
        valid_token = token_model.decode(token=self.token)

        if valid_token is False:
            return ErrorClass(error_code=self.error.User.code_1005, message_code=self.error.User.message_1005)

        has_time = token_model.check_time(token=self.token)
        if has_time is False:
            return ErrorClass(error_code=self.error.User.code_1006, message_code=self.error.User.message_1006)

        user_info = user_db.find_one({
            Names.id: ObjectId(valid_token)
        })
        if user_info is None:
            return ErrorClass(error_code=self.error.User.code_1007, message_code=self.error.User.message_1007)
        return User(username=user_info[self.mongo_name.username], id=str(user_info[self.mongo_name.id]),
                    family=user_info[self.mongo_name.username], token=token_model.refresh_token(self.token),
                    name=user_info[self.mongo_name.name], role=user_info[self.mongo_name.role],
                    image=user_info[self.mongo_name.image], men_sex=user_info[self.mongo_name.men_sex],
                    money=user_info[self.mongo_name.money], Email=user_info[self.mongo_name.Email],
                    create_date=user_info[self.mongo_name.create_at], updated_at=user_info[self.mongo_name.update_at]
                    )
