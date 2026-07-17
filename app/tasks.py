from app.database import SessionLocal
from app.celery_app import celery_app
from app import models
from celery.exceptions import MaxRetriesExceededError, SoftTimeLimitExceeded
import time

@celery_app.task(bind=True, max_retries=6, retry_backoff=True, soft_time_limit=10.0, time_limit=15.0)
def process_order(self, order_id: int):
    db = SessionLocal()
    order = None
    try:
        order = db.get(models.Order, order_id)
        if order is None:
            return
        order.status = models.Status.processing
        db.commit()
        time.sleep(5.0) #simulates order time
        order.status = models.Status.completed
        db.commit()
    except SoftTimeLimitExceeded:
        if order:
            order.status = models.Status.failed
            db.commit()
    except Exception as exc:
        try:
            self.retry(exc=exc)
        except MaxRetriesExceededError:
            if order:
                order.status = models.Status.failed
                db.commit()
    finally:
        db.close()