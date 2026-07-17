from celery import Celery
from dotenv import load_dotenv
import os

load_dotenv()

celery_app = Celery("orders", 
             broker=os.getenv("CELERY_BROKER_URL"), 
             backend=os.getenv("CELERY_RESULT_BACKEND"),
             include=["app.tasks"])

