import uvicorn
from fastapi import FastAPI
from app.routers import category
from app.routers import products
from app.routers import auth


app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "My App"}


app.include_router(auth.router)
app.include_router(category.router)
app.include_router(products.router)

if __name__ == "__main__":
    uvicorn.run("app.main:app")
