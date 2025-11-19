from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import get_arrived_db
from managers.car_manager import car_manager
from models.user_models import CarCreate, CarResponse

router = APIRouter(prefix="/cars", tags=["cars"])

@router.post("/", response_model=CarResponse, status_code=status.HTTP_201_CREATED)
def add_car(car: CarCreate, db: Session = Depends(get_arrived_db)):
    """Добавление прибывшего автомобиля"""
    
    existing_car = car_manager.get_car_by_vin(db, car.vin)
    if existing_car:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Автомобиль с таким VIN уже существует"
        )
    
    return car_manager.add_car(db, car)

@router.get("/", response_model=List[CarResponse])
def get_available_cars(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_arrived_db)
):
    """Получение списка доступных автомобилей"""
    return car_manager.get_available_cars(db, skip, limit)

@router.get("/{car_id}", response_model=CarResponse)
def get_car(car_id: int, db: Session = Depends(get_arrived_db)):
    """Получение информации об автомобиле по ID"""
    car = car_manager.get_car_by_id(db, car_id)
    if not car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Автомобиль не найден"
        )
    return car