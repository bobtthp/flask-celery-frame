import os

from flask import Flask
from plog.extensions import celery_task
from plog.config import celeryConfig, Env
from plog.views import VIEW_LIST


__slot__ = ['app', 'celeryTask']




# app
def _app():
    app = Flask(Env.APP)
    [app.register_blueprint(v) for v in VIEW_LIST]
    print(' App register  success!')
    return app

# init
def create_app():
    from plog.config import Env
    print(' App init success!')
    #print(Env.LOGGER_DIR)
    if not os.path.exists(Env.LOGGER_DIR): os.mkdir(Env.LOGGER_DIR)
    app = _app()
    app.config['CELERY_BROKER_URL'] = celeryConfig.BROKER_URL
    app.config['CELERY_RESULT_BACKEND'] = celeryConfig.CELERY_RESULT_BACKEND

    celery_task.init_app(app)
    return app



