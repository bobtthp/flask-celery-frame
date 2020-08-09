from flask import (
    flash, g, redirect, render_template, request, session, url_for, Blueprint
)
from  celery.signals import task_postrun
import logging

from plog.logger import setting_logger
from plog.task.utils import check

setting_logger('task')
logger = logging.getLogger('task')

taskView = Blueprint('task',__name__,url_prefix='/task')

'''
task_id   : 为任务分配唯一id，默认是uuid;
countdown : 设置该任务等待一段时间再执行，单位为s；
eta       : 定义任务的开始时间；eta=time.time()+10;
expires   : 设置任务时间，任务在过期时间后还没有执行则被丢弃；
retry     : 如果任务失败后, 是否重试;使用true或false，默认为true
shadow    : 重新指定任务的名字str，覆盖其在日志中使用的任务名称；
retry_policy : {},重试策略.如下：
----max_retries    : 最大重试次数, 默认为 3 次.
----interval_start : 重试等待的时间间隔秒数, 默认为 0 , 表示直接重试不等待.
----interval_step  : 每次重试让重试间隔增加的秒数, 可以是数字或浮点数, 默认为 0.2
----interval_max   : 重试间隔最大的秒数, 即 通过 interval_step 增大到多少秒之后, 就不在增加了, 可以是数字或者浮点数, 默认为 0.2 .

routing_key : 自定义路由键；
queue       : 指定发送到哪个队列；
exchange    : 指定发送到哪个交换机；
priority    : 任务队列的优先级，0到255之间，对于rabbitmq来说0是最高优先级；
serializer  :任务序列化方法；通常不设置；
compression : 压缩方案，通常有zlib, bzip2
headers     : 为任务添加额外的消息；
link        : 任务成功执行后的回调方法；是一个signature对象；可以用作关联任务；
link_error  : 任务失败后的回调方法，是一个signature对象；
'''

@taskView.route('/test_1')
def testApi():
    q = request.args.get('queue')
    logger.info("healthy")
    res = check.apply_async(queue=q)
    return 'health'


@taskView.route('/logSearch',methods=['POST', 'GET'])
def logSearch():
    dataDict = request.json
    appname = dataDict.get('appname')
    zone = dataDict.get('zone')
    log = dataDict.get('loginfo')
    print(log)
    return 'ok'


@task_postrun.connect
def task_postrun_handler(sender=None, task_id=None, task=None, args=None, kwargs=None, retval=None, state=None, **kwds):
    """任务完成的信号处理函数"""
    print('''   Done!
    sender: %s
    task_id: %s
    task: %s
    retval: %s
    state: %s
    args:%s
    kwargs:%s
    kwds:%s''' % (sender, task_id, task, retval, state, args, kwargs, kwds,))