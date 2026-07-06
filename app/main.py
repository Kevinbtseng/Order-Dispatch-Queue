from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app import schemas, crud, database
from app.tasks import process_order

app = FastAPI()

@app.post("/orders/", response_model=schemas.OrderResponse)
async def create_order(order: schemas.OrderCreate, db: Session = Depends(database.get_db)):
    db_order = crud.create_order(db, order)
    process_order.delay(db_order.id)
    return db_order

@app.get("/orders/{oredr_id}", response_model=schemas.OrderResponse)
async def get_order(order_id: int, db: Session = Depends(database.get_db)):
    order = crud.get_order(db, order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order