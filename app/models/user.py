from app.backend.db import Base
from sqlalchemy import *

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(150))
    last_name = Column(String(150))
    username = Column(String(150), unique=True)
    email = Column(String(150), unique=True)
    hashed_password = Column(String(250))