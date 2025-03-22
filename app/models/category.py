from app.backend.db import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150))
    slug = Column(String(150), unique=True, index=True)
    is_active = Column(Boolean, default=True)
    parent_id = Column(Integer, ForeignKey('categories.id'), nullable=True)

    relationship("Products", back_populates="categories")
