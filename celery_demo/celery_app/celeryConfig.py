# -*- coding: utf-8 -*-
"""
@Author: llf
@File: celeryConfig.py
@IDE: Pycharm
@Time: 2019-04-20 23
"""
from datetime import timedelta
from celery.schedules import crontab

broker_url = 'pyamqp://admin:admin@localhost//'  # rabbitmq作为broker 任务队列位置
# broker_url = 'redis://localhost:6379/1'  # redis作为broker
result_backend = 'redis://localhost:6379/2'  # 结果输出位置
timezone = 'Asia/Shanghai'

# 导入指定的任务模块
imports = (
    'celery_app.task1',
    'celery_app.task2',
)

# 定时任务
beat_schedule = {
    'task1': {
        'task': 'celery_app.task1.add',
        'schedule': timedelta(seconds=10),
        'args': (2, 8),
    },
    'task2': {
        'task': 'celery_app.task2.multiply',
        'schedule': crontab(hour=20, minute=19),
        'args': (4, 5)
    }
}
