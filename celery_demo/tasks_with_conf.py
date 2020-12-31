# -*- coding: utf-8 -*-
import time
from celery import Celery

broker = 'pyamqp://admin:admin@localhost//'  # rabbitmq作为broker 任务队列位置
# broker = 'redis://localhost:6379/1'  # redis作为broker
backend = 'redis://localhost:6379/2'  # 结果输出位置
app = Celery('tasks_with_conf', broker=broker, backend=backend)  # tasks为celery任务名与模块名保持一致
# # 单项配置
# app.conf.task_serializer = 'json'
# 多项配置
app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Asia/Shanghai',
    enable_utc=True,
)

# app.config_from_object('celeryconfig')
# # celeryconfig.py
# broker_url = 'pyamqp://admin:admin@localhost//'
# result_backend = 'redis://localhost:6379/2'
# task_serializer = 'json'
# result_serializer = 'json'
# accept_content = ['json']
# timezone = 'Europe/Oslo'
# enable_utc = True


@app.task
def add(x, y):
    print("enter func...")
    time.sleep(4)
    return x + y


if __name__ == '__main__':
    add.delay(1, 2)
