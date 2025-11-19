from sqlalchemy import Column,Integer,String,Float,Boolean,DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class ArrivedCar(Base):
    __tablename__ = "arrived_cars"

    id = Column(Integer,primary_key=True,index=True)
    brand = Column(String,index= True) 
    model = Column(String,index=True)
    year = Column(Integer)
    color = Column(String)
    price = Column(Float)
    vin = Column(String,unique=True,index=True)
    mileage = Column(Float)
    fuel_type = Column(String)
    transmission = Column(String)
    is_available = Column(Boolean, default=True)
    arrival_date = Column(DateTime,default=datetime.utcnow)

class PurchasedCar(Base):
    __tablename__ = "purchased_cars"

    id = Column(Integer,primary_key=True,index=True)
    car_id = Column(Integer,index = True)
    brand = Column(String, index=True)  
    model = Column(String, index=True)
    year = Column(Integer)
    color = Column(String) 
    price = Column(Float)
    vin = Column(String,index=True)
    buyer_name = Column(String, index=True)
    buyer_email = Column(String,index=True)
    purchase_date = Column(DateTime,default=datetime.utcnow)