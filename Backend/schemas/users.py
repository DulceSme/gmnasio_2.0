from pydantic import BaseModel
from typing import List, Union
from datetime import datetime

class UserBase(BaseModel):
    usuario: str
    password: str
    created_at: datetime
    estatus: bool
    Id_persona: int
class UserCreate(UserBase):
    pass
class UserUpdate(UserBase):
    pass
class User(UserBase):
    id:int
    class config:
        orm_mode = True