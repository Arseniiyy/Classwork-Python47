from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime

class CarBase(BaseModel):
    brand:str
    model:str
    year:int
    color:str
    price:float
    vin:str
    mileage:float
    fuel_type:str
    transmission:str

class CarCreate(CarBase):
    pass

class CarResponse(CarBase):
    id:int
    is_available:bool
    arrival_date: datetime

    class Config:
        from_attributes = True

class PurchaseCreate(BaseModel):
    car_id:int 
    buyer_name:str 
    buyer_email:str

class PurchaseResponse(BaseModel):
    id:int 
    car_id:int 
    brand:str 
    model:str 
    price:float 
    buyer_name:str 
    buyer_email:str 
    purchase_date: datetime 

    class Config:
        from_attributes = True