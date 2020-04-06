# coding:utf8
import time
from celery import Celery

broker = 'redis://127.0.0.1:6379/1'  # 任务队列位置
backend = 'redis://127.0.0.1:6379/2'  # 结果输出位置
app = Celery('my_task', broker=broker, backend=backend)  # my_task为定时任务名字，自定义


@app.task
def add(x, y):
    print("enter func...")
    time.sleep(4)
    return x + y


