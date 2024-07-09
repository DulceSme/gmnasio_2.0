from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import models.persons

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String(255))
    password = Column(LONGTEXT)
    created_at = Column(DateTime)
    estatus = Column(Boolean, default=False)
    # Clave foránea para la relación uno a uno con User
    Id_persona = Column(Integer, ForeignKey("persons.id"))

