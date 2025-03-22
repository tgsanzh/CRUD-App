from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine("mysql+pymysql://root:root@localhost:3306/testdb", echo=True)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass