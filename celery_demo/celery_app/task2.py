# !/usr/bin/python3
# coding:utf-8

"""
@Author: llf
@File: task2.py
@IDE: Pycharm
@Time: 2019-04-20
"""
import time

from celery_app import app


@app.task
def multiply(x, y):
    time.sleep(4)
    return x*y


