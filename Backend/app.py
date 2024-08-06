from fastapi import FastAPI
from routes.user import user
from routes.person import person
from routes.rol import rol
from routes.usersrols import userrol
from routes.Pregunta import pregunta_router 
from routes.OpinionCliente import opinion_router

app = FastAPI()
app.include_router(user)
app.include_router(person)
app.include_router(rol)
app.include_router(userrol)
app.include_router(pregunta_router )
app.include_router(opinion_router)
print("Hola bienvenido a mi backend")