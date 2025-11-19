from fastapi import FastAPI
from app.database import create_tables
from routers.cars import router as cars_router
from routers.purchases import router as purchases_router

create_tables()

app = FastAPI(
    title="Car Dealership API",
    description="API для управления автопарком и продажей автомобилей",
    version="1.0.0"
)


app.include_router(cars.router)
app.include_router(purchases.router)

@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в API автопарка!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}