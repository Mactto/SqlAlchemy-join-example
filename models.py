from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
from settings import Settings

Base = declarative_base()

settings = Settings()


engine = create_engine(settings.DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    products = relationship("Product", back_populates="order")

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    order_id = Column(Integer, ForeignKey('orders.id'))
    order = relationship("Order", back_populates="products")


Base.metadata.create_all(bind=engine)