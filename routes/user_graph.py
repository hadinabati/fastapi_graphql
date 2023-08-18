import strawberry
from strawberry.fastapi import GraphQLRouter
from fastapi import Depends, Request
from strawberry.types import Info
from typing import Union
from schema.register_schema import User, Error
from instance.server import Name
from models.user_model import UserInformation


def check_token(request: Request) -> str | None:
    token = request.headers.get(Name.token)
    return token


async def get_context(
        token=Depends(check_token),
):
    return {
        Name.user_info: token,
    }


@strawberry.type
class Query:
    @strawberry.field
    def user_info(self, info: Info) -> Union[User, Error]:
        token = info.context[Name.user_info]
        cl = UserInformation(token=token)
        response = cl.user_()
        return response


schema = strawberry.Schema(Query)

user_graph = GraphQLRouter(
    schema=schema,
    context_getter=get_context

)
