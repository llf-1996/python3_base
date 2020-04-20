## Django使用celery
>旧版celery3.1.26
#### 安装
```sh
pip install django-celery
```
|--celeryDjango
	|--celeryapp
	   |--__init__.py
	   |--models.py
	   |--views.py
	   |--urls.py
	   |--tasks.py
	|--celeryDjango
		|--__init__.py
		|--settings.py
		|--urls.py
		|--wsgi.py
		|--celeryconfig.py
	|--manage.py

#### celeryconfig
```py
# celeryconfig.py

# !/usr/bin/python3
# coding:utf8

from datetime import timedelta
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

# 定时任务
CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': 'celery-task2',
        'schedule': timedelta(seconds=5),
        # 'schedule': crontab(hour=20, minute=19),
        'args': [1, 2],  # 参数
        'kwargs': {'name': 'llf'},  # 参数
        'options': {
            'queue': 'beat_tasks',  # 指定队列
        }
    }
}


```

#### settings
```py
# settings.py

INSTALLED_APPS = [
	...
    'djcelery',
]

# celery
from .celeryconfig import *
BROKER_BACKEND = 'redis'
BROKER_URL = 'redis://127.0.0.1:6379/1'  # 任务队列位置
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/2'  # 结果输出位置
CELERY_TIMEZONE = 'Asia/Shanghai'
```

#### tasks
```py
# celeryapp/tasks.py

# !/usr/bin/python3
# coding:utf8

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

```

#### views
```py
from celeryapp.tasks import CeleryTask


# Create your views here.
def do(request):
    # 执行异步任务
    print('start do request')
    # CeleryTask.delay()
    CeleryTask.apply_async(args=[1, 2], kwargs={'name': 'l'}, queue='work_queue')  # 也可在这里指定参数和队列
    print('end do request')
    return JsonResponse({'result': 'ok'})

```

#### 启动
```sh
python manage.py runserver
python manage.py celery worker -l INFO
python manage.py celery beat -l INFO
```

#### 监控工具flower
```sh
# 安装
pip install flower
# 启动
celery flower --address=0.0.0.0 --port=5555 --broker=xxx --basic_auth=test:test

python manage.py celery flower --basic_auth=test:test
```

## 进程管理supervisor

|--celeryDjango
	|--celeryapp
	|--celeryDjango
	|--conf
		|--supervisord.conf
		|--supervisor_celery_worker.ini
	|--logs
	|--manage.py

#### 安装
```sh
pip install supervisor
mkdir conf
echo_supervisord_conf > conf/supervisord.conf
```
#### supervisord.conf
```ini
;conf/supervisord.conf

[inet_http_server]
port=127.0.0.1:9001

[supervisorctl]
serverurl=http://127.0.0.1:9001

[include]
files = *.ini
```

#### supervisor_celery_worker.ini
```ini
;conf/supervisor_celery_worker.ini

[program:celery-worker]
command=python3 manage.py celery worker -l INFO
directory=/celery_demo/celeryDjango
environment=PATH="/py36/bin"
stdout_logfile=/celery_demo/celeryDjango/logs/celery_worker.log
stderr_logfile=/celery_demo/celeryDjango/logs/celery_worker.log
autostart=true
autorestart=true
startsecs=10
stopwaitsecs=60
priority=998  ;优先级

```

#### supervisor_celery_beat.ini
```ini
;conf/supervisor_celery_beat.ini

[program:celery-beat]
command=python3 manage.py celery beat -l INFO
directory=/celery_demo/celeryDjango
environment=PATH="/py36/bin"
stdout_logfile=/celery_demo/celeryDjango/logs/celery_beat.log
stderr_logfile=/celery_demo/celeryDjango/logs/celery_beat.log
autostart=true
autorestart=true
startsecs=10
stopwaitsecs=60
priority=997  ;优先级

```

#### supervisor_celery_flower.ini
```ini
;conf/supervisor_celery_flower.ini

[program:celery-flower]
command=python3 manage.py celery flower
directory=/celery_demo/celeryDjango
environment=PATH="/py36/bin"
stdout_logfile=/celery_demo/celeryDjango/logs/celery_flower.log
stderr_logfile=/celery_demo/celeryDjango/logs/celery_flower.log
autostart=true
autorestart=true
startsecs=10
stopwaitsecs=60
priority=1000  ;优先级

```

#### 启动
```sh
supervisord -c conf/supervisord.conf

ps -aux | grep supervisor

supervisorctl
>help
>update
```

#### 查看
127.0.0.1：9001


## admin
admin
admin123

