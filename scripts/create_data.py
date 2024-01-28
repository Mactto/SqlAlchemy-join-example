from faker import Faker
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from models import Order, Product, Base, SessionLocal
from settings import Settings

settings = Settings()

fake = Faker()

def create_random_order(session: Session):
    customer_name = fake.name()
    order = Order(customer_name=customer_name)
    session.add(order)
    session.commit()
    return order

def create_random_product(session: Session, order_id: int):
    product_name = fake.word()
    product = Product(name=product_name, order_id=order_id)
    session.add(product)
    session.commit()
    return product

def main():
    engine = create_engine(settings.DATABASE_URL)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    for _ in range(10):  # 10개의 주문 생성
        order = create_random_order(db)
        for _ in range(3):  # 각 주문당 3개의 상품 생성
            create_random_product(db, order.id)

if __name__ == "__main__":
    main()
