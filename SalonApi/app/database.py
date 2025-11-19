from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.car_models import Base


ARRIVED_CARS_DB_URL = "sqlite:///./arrived_cars.db"
PURCHASED_CARS_DB_URL = "sqlite:///./purchased_cars.db"

engine_arrived = create_engine(ARRIVED_CARS_DB_URL, connect_args={"check_same_thread":False})
engine_purchased = create_engine(PURCHASED_CARS_DB_URL, connect_args={"check_same_thread":False})

SessionLocalArrived = sessionmaker(autocommit=False,autoflush=False,bind=engine_arrived)
SessionLocalPurchased = sessionmaker(autocommit=False,autoflush=False,bind=engine_purchased)

def create_tables():
    Base.metadata.create_all(bind=engine_arrived)
    Base.metadata.create_all(bind=engine_purchased)

def get_arrived_db():
    db = SessionLocalArrived()
    try:
        yield db
    finally:
        db.close()


def get_purchased_db():
    db = SessionLocalPurchased()
    try:
        yield db
    finally:
        db.close()