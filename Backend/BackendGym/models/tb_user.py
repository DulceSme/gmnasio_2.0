from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.bd import meta, engine
from datetime import datetime
tb_users = Table("Users", meta,
                 Column("id",Integer, primari_key=true),
                 Column("Usuario",String(255)),
                 Column("Password",String(255)),
                 Column("create_at",datetime = datetime.now()),
                 Column("Estatus",bool= False),
                 Column("Id_persona",Integer),
                 )
meta.create_all(engine)