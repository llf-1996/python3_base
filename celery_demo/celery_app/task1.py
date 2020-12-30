# -*- coding: utf-8 -*-
"""
@Author: llf
@File: task1.py
@IDE: Pycharm
@Time: 2019-04-20
"""
import time

from celery_app import app


@app.task
def add(x, y):
    time.sleep(3)
    return x+y
