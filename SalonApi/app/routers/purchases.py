from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_arrived_db, get_purchased_db
from app.managers.car_manager import car_manager
from app.models.user_models import PurchaseCreate, PurchaseResponse

router = APIRouter(prefix="/purchases", tags=["purchases"])

@router.post("/", response_model=PurchaseResponse, status_code=status.HTTP_201_CREATED)
def purchase_car(
    purchase: PurchaseCreate,
    arrived_db: Session = Depends(get_arrived_db),
    purchased_db: Session = Depends(get_purchased_db)
):
    """Покупка автомобиля"""
    purchased_car = car_manager.purchase_car(arrived_db, purchased_db, purchase)
    
    if not purchased_car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Автомобиль не найден или уже продан"
        )
    
    return purchased_car

@router.get("/", response_model=List[PurchaseResponse])
def get_purchased_cars(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_purchased_db)
):
    """Получение списка проданных автомобилей"""
    return car_manager.get_purchased_cars(db, skip, limit)