from celery import Celery
from flask_celery import Celery

from plog.config import celeryConfig, Env


# tasks
def _celey():
    print(' Celery init success!')
    task = Celery()
    task.config_from_object(celeryConfig)
    return task


celery_task = _celey()
