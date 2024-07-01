# from sqlalchemy import create_engine, MetaData

# engine = create_engine("mysql+pymysql://root:1234@localhost:3307/test.db")
# meta = MetaData()
# conn =engine.connect()
from sqlalchemy import create_engine
from sqlalcheme.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmarker
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234@localhost:3307/test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmarker(autocommit=False,autoflush = False, bind = engine)
Base = declarative_base()
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()