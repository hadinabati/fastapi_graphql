from typing import Union

import strawberry
from strawberry.fastapi import GraphQLRouter
from models.register_model import UserRegister
from schema.register_schema import Register, User, Error, SMS
from models.sms_model import Sms


@strawberry.type
class Mutation:

    @strawberry.mutation
    def register_user(self, data: Register) -> Union[User, Error]:
        user_input = data
        register_model = UserRegister(token=None, username=user_input.username)
        response = register_model.create_user(user_info=user_input)
        return response

    @strawberry.mutation
    def send_otp(self, number: str) -> Union[Error, SMS]:
        phone = number
        cl = Sms(mobile=phone)
        return cl.otp()


@strawberry.type
class Query:
    @strawberry.field
    def user_info(self) -> str:
        return 'hi'


schema = strawberry.Schema(query=Query, mutation=Mutation)

register_graph = GraphQLRouter(schema)
