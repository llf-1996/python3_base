# !/usr/bin/python3
# coding:utf-8

"""
@Author: llf
@File: celeryConfig.py
@IDE: Pycharm
@Time: 2019-04-20 23
"""
from datetime import timedelta
from celery.schedules import crontab

BROKER_URL = 'redis://148.70.214.104:6379/1'  # 任务队列位置
CELERY_RESULT_BACKEND = 'redis://148.70.214.104:6379/2'  # 结果输出位置
CELERY_TIMEZONE = 'Asia/Shanghai'

# 导入指定的任务模块
CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2',
)

# 定时任务
CELERYBEAT_SCHEDULE = {
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

