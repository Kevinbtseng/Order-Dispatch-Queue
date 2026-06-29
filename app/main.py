from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud, database

app = FastAPI()

@app.post("/orders/", response_model=schemas.OrderResponse)
async def create_order(order: schemas.OrderCreate, db: Session = Depends(database.get_db)):
    return crud.create_order(db, order)

@app.get("/orders/{id}", response_model=schemas.OrderResponse)
async def get_order(id: int, db: Session = Depends(database.get_db)):
    order = crud.get_order(db, id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order