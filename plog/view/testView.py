from plog.logger import setting_logger
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import logging

setting_logger('health')
logger = logging.getLogger('health')

testView = Blueprint('health', __name__, url_prefix='/health')

@testView.route('/')
def testApi():
    logger.info("healthy")
    return 'health'