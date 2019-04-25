# !/usr/bin/python3
# coding:utf8

"""
@Author: llf
@File: celeryconfig.py
@IDE: Pycharm
@Time: 2019-04-24
"""
import djcelery

djcelery.setup_loader()

CELERY_QUEUES = {
    'beat_tasks': {
        'exchange': 'beat_tasks',
        'exchange_type': 'direct',
        'binding_key': 'beat_tasks',
    },
    'work_queue': {
        'exchange': 'work_queue',
        'exchange_type': 'direct',
        'binding_key': 'work_queue',
    }
}

CELERY_DEFAULT_QUEUE = 'work_queue'

CELERY_IMPORTS = {
    'celeryapp.tasks',
}

# 有些情况可以防止死锁
CELERYD_FORCE_EXECV = True
# 设置并发的worker数量
CELERYD_CONCURRENCY = 4
# 允许重试
CELERY_ACKS_LATE = True
# 每个worker最多执行100个任务被销毁，可以防止内存泄漏
CELERY_MAX_TASKS_PER_CHILD = 100
# 单个任务的最大运行时间
CELERYD_TASK_TIME_LIMIT = 12*30

