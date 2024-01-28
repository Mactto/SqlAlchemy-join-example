from fastapi import FastAPI
from pydantic import BaseModel
from models import Order, Product, SessionLocal
from sqlalchemy.orm import joinedload, lazyload
from sqlalchemy.sql import expression


app = FastAPI()

session = SessionLocal()

class GetAllOrdersResponse(BaseModel):
    class Product(BaseModel):
        id: int
        name: str
        id: int

    customer_name: str
    products: list[Product]


# lazy 로딩으로 order 들을 불러오는 예제
@app.get("/orders/lazy")
async def get_all_orders_by_lazy_load() -> list[GetAllOrdersResponse]:
    orders = (
        session.execute(
            expression.select(Order).join(Order.products).limit(1)
        )
        .scalars().all()
    )

    return [
        GetAllOrdersResponse(
            id=order.id,
            customer_name=order.customer_name,
            products=[
                GetAllOrdersResponse.Product(
                    id=product.id,
                    name=product.name
                )
                for product in order.products
            ]
        )
        for order in orders
    ]


# eager 로딩으로 order 들을 불러오는 예제
@app.get("/orders/eager")
async def get_all_orders_by_eager_loading() -> list[GetAllOrdersResponse]:
    orders = (
        session.execute(
            expression.select(Order).options(joinedload(Order.products))
        )
        .scalars()
        .all()
    )

    return [
        GetAllOrdersResponse(
            id=order.id,
            customer_name=order.customer_name,
            products=[
                GetAllOrdersResponse.Product(
                    id=product.id,
                    name=product.name
                )
                for product in order.products
            ]
        )
        for order in orders
    ]


# joinload로 필터링 거는 예제 
@app.get("/orders/eager/filtering")
async def get_orders_by_eager_loading_with_filter() -> list[GetAllOrdersResponse]:
    orders = (
        session.execute(
            expression
            .select(Order)
            .filter(Product.name =="practice")
            .options(joinedload(Order.products))
        )
        .scalars()
        .all()
    )

    return [
        GetAllOrdersResponse(
            id=order.id,
            customer_name=order.customer_name,
            products=[
                GetAllOrdersResponse.Product(
                    id=product.id,
                    name=product.name
                )
                for product in order.products
            ]
        )
        for order in orders
    ]



# joinload와 join으로 필터링 거는 예제 
@app.get("/orders/eager/filtering_with_join")
async def get_orders_by_eager_loading_with_filter_join() -> list[GetAllOrdersResponse]:
    orders = (
        session.execute(
            expression
            .select(Order)
            .join(Product)
            .filter(Product.name =="practice")
            .options(joinedload(Order.products))
        )
        .unique()
        .scalars()
        .all()
    )

    return [
        GetAllOrdersResponse(
            id=order.id,
            customer_name=order.customer_name,
            products=[
                GetAllOrdersResponse.Product(
                    id=product.id,
                    name=product.name
                )
                for product in order.products
            ]
        )
        for order in orders
    ]