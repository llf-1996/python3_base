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
        print('start celery task')
        time.sleep(6)
        print('args={}, kwargs={}'.format(args, kwargs))
        print('end celery task')


