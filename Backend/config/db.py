from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'mysql://avnadmin:AVNS_w5V21kW9pfSV8Ypbo7a@mysql-899b561-utxicotepec-9d53.l.aivencloud.com:19027/defaultdb'
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:1234@localhost:3307/test'  #Conexión local

#  Conexión local
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
