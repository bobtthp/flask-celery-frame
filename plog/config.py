import logging
import os



class celeryConfig(object):
    timezone = 'Asia/Shanghai'
    broker_transport_options = {'visibility_timeout': 3600}

    BROKER_URL = 'redis://:123456@127.0.0.1:6379/2'
    CELERY_RESULT_BACKEND = 'redis://:123456@127.0.0.1:6379/3'

    CELERY_ENABLE_UTC = True

    #CELERY_ANNOTATIONS = {'tasks.add':{'rate_limit':'10/s'}} 限制执行10s执行一次

    #celery worker每次去redis取任务的数量，默认值就是4
    CELERYD_PREFETCH_MULTIPLIER = 4

    #每个worker执行了多少次任务后就会死掉，建议数量大一些，默认是无限的
    #CELERYD_MAX_TASKS_PER_CHILD = 200

    #celery任务执行结果的超时时间
    CELERY_TASK_RESULT_EXPIRES = 1200

    #CELERY_TASK_SERIALIZER = 'pickle' | 'json'

    # 关闭限速
    #CELERY_DISABLE_RATE_LIMITS = True

    # 压缩方案选择，可以是zlib, bzip2，默认是发送没有压缩的数据
    CELERY_MESSAGE_COMPRESSION = 'zlib'

    # 在5s内完成任务，否则执行该任务的worker将被杀死，任务移交给父进程
    CELERYD_TASK_TIME_LIMIT = 5

    # 设置默认的队列名称，如果一个消息不符合其他的队列就会放在默认队列里面，如果什么都不设置的话，数据都会发送到默认的队列中
    #CELERY_DEFAULT_QUEUE = "default"

    CELERY_QUEUES = {
        # "default": {  # 这是上面指定的默认队列
        #     "exchange": "default",
        #     "exchange_type": "direct",
        #     "routing_key": "default"
        # },
        "plog.task.utils.check": {  # 这是上面指定的默认队列
            "queue": 'test_1'
        },
        "plog.task.utils.check": {  # 这是上面指定的默认队列
            "queue": 'test_2'
        },
        # "topicqueue": {  # 这是一个topic队列 凡是topictest开头的routing key都会被放到这个队列
        #     "routing_key": "topic.#",
        #     "exchange": "topic_exchange",
        #     "exchange_type": "topic",
        # },
        # "task_eeg": {  # 设置扇形交换机
        #     "exchange": "tasks",
        #     "exchange_type": "fanout",
        #     "binding_key": "tasks",
        # }
    }

    CELERY_QUEUES={
        "test_1": {
            "exchange": "test_1"
        },
        "test_2": {
            "exchange": "test_2"
        },

    }


class Env(object):

    # APP
    APP = 'PROJECT'

    # SERVER
    SERVER_PORT = 8000

    # PROJECT
    PROJECT_DIR = os.path.abspath('.')

    # LOG
    LOGGER_LEVEL = logging.INFO
    LOGGER_DIR = os.path.join(PROJECT_DIR, "plog/logs")

