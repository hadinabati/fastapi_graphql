from fastapi import FastAPI
from  routes.user_graph import user_graph
from routes.register_graph import register_graph




app = FastAPI()

app.include_router(user_graph , prefix="/user")
app.include_router(register_graph , prefix="/register")

