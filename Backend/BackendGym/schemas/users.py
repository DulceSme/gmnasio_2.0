from pydantic import BaseModel
class UserBase(BaseModel):
    usuario: str
    password: str
    estatus: str
class UserCreate(UserBase):
    pass
class User(UserBase):
    id:int
    class config:
        orm_mode = True