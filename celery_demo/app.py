# !/usr/bin/python3
# coding:utf8

"""
@Author: llf
@File: app2.py
@IDE: Pycharm
@Time: 2019-04-21
"""
from celery_app import task1, task2

if __name__ == '__main__':
    t1 = task1.add.apply_async([1, 2])
    t2 = task2.multiply.delay(2, 5)
    print('t1:', t1)
    print('t2:', t2)
    print('end...')
