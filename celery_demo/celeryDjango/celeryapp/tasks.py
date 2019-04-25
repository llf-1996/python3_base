# !/usr/bin/python3
# coding:utf8

"""
@Author: llf
@File: tasks.py
@IDE: Pycharm
@Time: 2019-04-24
"""
import time
from celery.task import Task


class CeleryTask(Task):
    name = 'celery-task'

    def run(self, *args, **kwargs):
        print('开始异步任务')
        time.sleep(6)
        print('args={}, kwargs={}'.format(args, kwargs))
        print('结束异步任务')


class CeleryTask2(Task):
    name = 'celery-task2'

    def run(self, *args, **kwargs):
        print('开始定时任务')
        time.sleep(6)
        print('args={}, kwargs={}'.format(args, kwargs))
        print('结束定时任务')

