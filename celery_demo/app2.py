# !/usr/bin/python3
# coding:utf8

"""
@Author: llf
@File: app2.py
@IDE: Pycharm
@Time: 2019-04-21

依赖文件：
安装redis:  pip install redis==2.8.0
安装celery:  pip install celery==3.1.25

celery worker -A celery_app -l info -P eventlet
"""
from celery_app import task1, task2

task1.add.apply_async([1, 2])
task2.multiply.delay(2, 5)
print('end...')

