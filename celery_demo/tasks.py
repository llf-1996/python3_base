# -*- coding: utf-8 -*-
import time
from celery import Celery

broker = 'pyamqp://admin:admin@localhost//'  # rabbitmq作为broker 任务队列位置
# broker = 'redis://localhost:6379/1'  # redis作为broker
backend = 'redis://localhost:6379/2'  # 结果输出位置
app = Celery('tasks', broker=broker, backend=backend)  # tasks为celery任务名与模块名保持一致


@app.task
def add(x, y):
    print("enter func...")
    time.sleep(4)
    return x + y


if __name__ == '__main__':
    add.delay(1, 2)
