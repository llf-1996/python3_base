# !/usr/bin/python3
# coding:utf-8

"""
@Author: llf
@File: celeryConfig.py
@IDE: Pycharm
@Time: 2019-04-20 23
"""
BROKER_URL = 'redis://148.70.214.104:6379/1'  # 任务队列位置
CELERY_RESULT_BACKEND = 'redis://148.70.214.104:6379/2'  # 结果输出位置
CELERY_TIMEZONE = 'Asia/Shanghai'

# 导入指定的任务模块
CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2',
)

