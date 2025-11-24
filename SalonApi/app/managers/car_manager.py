from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.car_models import ArrivedCar, PurchasedCar  
from app.models.user_models import CarCreate, PurchaseCreate

class CarManager:
    def __init__(self):
        pass

    def add_car(self, db: Session, car: CarCreate) -> ArrivedCar:
        db_car = ArrivedCar(
            brand=car.brand,
            model=car.model,
            year=car.year,
            color=car.color,
            price=car.price,
            vin=car.vin,
            mileage=car.mileage,
            fuel_type=car.fuel_type,
            transmission=car.transmission
        )
        db.add(db_car)
        db.commit()
        db.refresh(db_car)
        return db_car

    def get_available_cars(self, db: Session, skip: int = 0, limit: int = 100) -> List[ArrivedCar]:
        return db.query(ArrivedCar).filter(ArrivedCar.is_available == True).offset(skip).limit(limit).all()

    def get_car_by_id(self, db: Session, car_id: int) -> Optional[ArrivedCar]:
        return db.query(ArrivedCar).filter(ArrivedCar.id == car_id).first()

    def get_car_by_vin(self, db: Session, vin: str) -> Optional[ArrivedCar]:
        return db.query(ArrivedCar).filter(ArrivedCar.vin == vin).first()

    def purchase_car(self, arrived_db: Session, purchased_db: Session, purchase: PurchaseCreate) -> Optional[PurchasedCar]:
        car = self.get_car_by_id(arrived_db, purchase.car_id)

        if not car or not car.is_available:
            return None

        car.is_available = False
        arrived_db.commit()

        purchased_car = PurchasedCar(
            car_id=car.id,
            brand=car.brand,
            model=car.model,
            year=car.year,
            color=car.color,
            price=car.price,
            vin=car.vin,
            buyer_name=purchase.buyer_name,
            buyer_email=purchase.buyer_email
        )

        purchased_db.add(purchased_car)
        purchased_db.commit()
        purchased_db.refresh(purchased_car)
        
        return purchased_car

    def get_purchased_cars(self, db: Session, skip: int = 0, limit: int = 100) -> List[PurchasedCar]:
        return db.query(PurchasedCar).offset(skip).limit(limit).all()

car_manager = CarManager()