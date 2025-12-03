import uvicorn
from fastapi import FastAPI
from app.routers import users, products,admin,categories,cart
from app.db.database import engine,Base
from app.core.logging_config import logger 

# Base.metadata.create_all(bind=engine)

app = FastAPI()

# Routers
app.include_router(users.router, prefix="/auth", tags=["users"])

app.include_router(categories.router, prefix="/categories", tags=["categories"])

app.include_router(products.router, prefix="/products", tags=["products"])

app.include_router(admin.router, prefix="/admin", tags=["admin"])

app.include_router(cart.router,prefix="/cart" ,tags=["cart"])


from fastapi_pagination import add_pagination
add_pagination(app)


if __name__ == '__main__':
    logger.info("Starting Uvicorn server...")
    uvicorn.run(app, host='127.0.0.1', port=8000)
    