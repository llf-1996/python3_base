# -*- coding: utf-8 -*-
import time
from celery import Celery

broker = 'pyamqp://admin:admin@localhost//'  # rabbitmq作为broker 任务队列位置
# broker = 'redis://localhost:6379/1'  # redis作为broker
backend = 'redis://localhost:6379/2'  # 结果输出位置
app = Celery('tasks', broker=broker, backend=backend)  # tasks为celery任务名与模块名保持一致


@app.task(bind=True, ignore_result=True, max_retries=3, default_retry_delay=30 * 60)
def add(x, y):
    '''
    bind：函数将是一个"Bound Method"，这样可以访问任务类型实例上的属性和方法。
    ignore_result:不存储任务结果
    max_retries: 重试次数
    default_retry_delay: 重试等待时间，默认3分钟 单位：秒
    api: https://docs.celeryproject.org/en/stable/reference/celery.app.task.html
    Args:
        x:
        y:
    Returns:
    '''
    print("enter func...")
    time.sleep(4)
    return x + y


if __name__ == '__main__':
    add.delay(1, 2)
