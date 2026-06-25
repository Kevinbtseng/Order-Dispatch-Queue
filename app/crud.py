from sqlalchemy.orm import Session
from app import models, schemas

def create_order(db: Session, order: schemas.OrderCreate):
    
    db_order = models.Order(
        items=order.items,
        quantity=order.quantity
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order(db: Session, order_id: int):
    order = db.get(models.Order, order_id)

    return order