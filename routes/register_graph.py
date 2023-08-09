from typing import Union

import strawberry
from strawberry.fastapi import GraphQLRouter
from models.register_model import UserRegister
from schema.register_schema import Register, User, Error


@strawberry.type
class Mutation:

    @strawberry.mutation
    def register_user(self, data: Register) -> Union[User, Error]:
        user_input = data
        register_model = UserRegister(token=None , username=user_input.username)
        response = register_model.create_user(user_info=user_input)
        a=6
        return  response






@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "world"


schema = strawberry.Schema(query=Query, mutation=Mutation)

register_graph = GraphQLRouter(schema)
