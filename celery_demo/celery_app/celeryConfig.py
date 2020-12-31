# -*- coding: utf-8 -*-
"""
@Author: llf
@File: celeryConfig.py
@IDE: Pycharm
@Time: 2019-04-20 23
"""
from datetime import timedelta
from celery.schedules import crontab
from kombu import Queue

# broker_url = 'pyamqp://admin:admin@localhost//'  # rabbitmq作为broker 任务队列位置
broker_url = 'redis://localhost:6379/1'  # redis作为broker
result_backend = 'redis://localhost:6379/2'  # 结果输出位置
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
# using serializer name
result_accept_content = ['json']
timezone = 'Asia/Shanghai'  # 默认UTC
enable_utc = True  # 转换为utc时间，celery>=3.0自动开启
result_expires = 3600  # 结果保存时间，默认一天，单位秒
task_ignore_result = True  # 是否存储任务结果 默认False
task_store_errors_even_if_ignored = True  # 存储所有任务的错误信息，即使task_ignore_result为True。默认值False
result_backend_always_retry = True  # 失败重试，默认False
result_backend_max_sleep_between_retries_ms = 10000  # 失败重试最大等待时间，默认10000，单位毫秒
result_backend_base_sleep_between_retries_ms = 10  # 失败重试基本等待时间，默认10，单位毫秒
result_backend_max_retries = 3  # 设置可恢复异常情况下的最大重试次数
result_compression = 'gzip'  # 压缩任务结果，默认不压缩  用于任务消息的默认压缩。可以是gzip、bzip2（如果可用）或在Kombu压缩注册表中注册的任何自定义压缩方案。


# 导入指定的任务模块
imports = (
    'celery_app.task1',
    'celery_app.task2',
)

# # 定时任务
# beat_schedule = {
#     'task1': {
#         'task': 'celery_app.task1.add',
#         'schedule': timedelta(seconds=10),
#         'args': (2, 8),
#     },
#     'task2': {
#         'task': 'celery_app.task2.multiply',
#         'schedule': crontab(hour=20, minute=19),
#         'args': (4, 5)
#     }
# }


# 创建queue
task_create_missing_queues = True    # 如果启用（默认），将自动创建未在task_queues中定义的任何指定队列
# # 1
# task_queues = {
#     'celery': {
#         'exchange': 'celery',
#         'exchange_type': 'direct',  # 默认值direct
#         'routing_key': 'celery.#',
#     },
#     'low-priority': {
#         'exchange': 'low-priority',
#         'routing_key': 'low-priority.#',
#     },
# }

# 2
task_queues = (
    Queue('default',    routing_key='default.#'),
    Queue('celery'),
    Queue('low-priority', routing_key='low-priority.#'),
)
task_default_queue = 'default'             # 指定默认queue
task_default_exchange = 'tasks'            # task_queues配置中使用Queue实例化的queue对象的exchange默认值
task_default_exchange_type = 'topic'       # task_queues配置中使用Queue实例化的queue对象的exchange_type默认值，默认direct
task_default_routing_key = 'task.default'  # task_queues配置中使用Queue实例化的queue对象的routing_key默认值
task_default_delivery_mode = 'persistent'   # transient（消息未写入磁盘）；persistent（写入磁盘）。 默认值: "persistent"


# 设置任务执行错误时的专用队列
task_routes = {
    'celery_app.task1.add': {
        'queue': 'low-priority',
        'routing_key': 'low-priority.add',
    },
    'celery_app.task2.multiply': 'default'
}

# 任务进行限速
task_annotations = {
    'celery_app.task1.add': {'rate_limit': '1/m'},
    '*': {'rate_limit': '1/m'},  # 所有任务
}

# api: https://docs.celeryproject.org/en/stable/userguide/configuration.html?highlight=result_expires#std-setting-task_compression
