from plog.logger import setting_logger
import logging
setting_logger('job-check')
logger = logging.getLogger('job-check')

from plog.extensions import celery_task

@celery_task.task
def check():
    logger.info('job check start')
    return 'healthy'


