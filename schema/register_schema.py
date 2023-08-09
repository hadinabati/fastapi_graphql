import datetime
from typing import Optional , List
from bson import ObjectId
import strawberry


@strawberry.input
class Register:
    name: Optional[str]
    family: Optional[str]
    password: Optional[str]
    username: Optional[str]



@strawberry.type
class User:
    name: Optional[str]
    family: Optional[str]
    money: Optional[int]
    role: Optional[str]
    image: Optional[str]
    men_sex: Optional[bool]
    Email: Optional[str]
    token: Optional[str]
    create_date: Optional[datetime.datetime]
    updated_at: Optional[datetime.datetime]


@strawberry.field
class Login:
    username: str
    password: str

@strawberry.type
class Error:
    error_code: Optional[int]
    message_code: Optional[str]
