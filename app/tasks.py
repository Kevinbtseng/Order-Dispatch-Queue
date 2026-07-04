from app.database import SessionLocal
from app.celery_app import celery_app
from app import models
import time

@celery_app.task()
def process_order(order_id: int):
    db = SessionLocal()
    try:
        order = db.get(models.Order, order_id)
        if order is None:
            return
        order.status = models.Status.processing
        db.commit()
        time.sleep(5.0) #simulates order time
        order.status = models.Status.completed
        db.commit()
    except Exception:
        if order:
            order.status = models.Status.failed
            db.commit()
    finally:
        db.close()