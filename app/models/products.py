from app.backend.db import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150))
    slug = Column(String(150), unique=True, index=True)
    description = Column(String(150))
    price = Column(Integer)
    image_url = Column(String(150))
    stock = Column(Integer)
    supplier_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    rating = Column(Float)
    is_active = Column(Boolean, default=True)

    relationship("Category", back_populates="products")