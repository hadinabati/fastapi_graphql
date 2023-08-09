import  strawberry
from strawberry.fastapi import GraphQLRouter





@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"


schema = strawberry.Schema(Query)

user_graph = GraphQLRouter(schema)