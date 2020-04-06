## 异步任务：
环境：win10、py3.6.8

### 安装
```sh
pip install celery[redis]
```

### 启动
运行程序之前需要先启动worker：celery worker -A tasks -l INFO  
-A tasks指定worker，在当前文件夹下的tasks.py文件  
-l info 指定日志级别  

error:  
asks, accept, hostname = _loc  
ValueError: not enough values to unpack (expected 3, got 0)  
### 解决方案:  
第二种: pip install eventlet  
启动celeryworker时: celery -A tasks --loglevel=info -P eventlet  # 协程  

参考博客：https://blog.csdn.net/diqiuyi7777/article/details/88314549  


## 定时任务：
### 启动：
第一种：  
celery_demo# celery beat -A celery_app -l INFO   # celery4.1.0的时区有bug  
celery_demo# celery worker -A celery_app -l INFO  
第二种：  
celery -B -A celery_app worker -l INFO  


## celery base demo

```py
# tasks.py
import time
from celery import Celery

broker = 'redis://localhost:6379/1'
backend = 'redis://localhost:6379/2'
app = Celery('my_task', broker=broker, backend=backend)

@app.task
def add(x, y):
	print('enter call func...')
	time.sleep(4)
	return x + y

```

```py
# app.py
from tasks import add


if __name__ == '__main__':
	print('start task...')
	result = add.delay(2, 8)
	print('end task...')
	pirnt(result)
```
#### 启动worker
```sh
celery worker -A tasks -l INFO
```

#### 执行异步任务
```sh
python app.py
```


## celery config file demo

|--celery_app
   |--__init__.py
   |--celeryconfig.py
   |--task1.py
   |--task2.py
|--app.py

```py
# __init__.py
from celry import Celery

app = Celery('demo')
app.config_from_object('celery_app.celeryconfig')  # 通过Celery实例加载配置文件

```

```py
# celeryconfig.py
BROKER_URL = 'redis://localhost:6379/1'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'

CELERY_TIMEZONE = 'Asia/Shanghai'  # 默认UTC

# 导入指定的任务模块
CELERY_IMPORTS = (
	'celery_app.task1',
	'celery_app.task2'
	)

```

```py
# task1.py
import time

from celery_app import app


@app.task
def add(x, y):
	time.sleep(3)
	return x + y

```

```py
# task2.py
import time

from celery_app import app


@app.task
def multiply(x, y):
	time.sleep(3)
	return x * y

```


```py
# app.py
from celery_app import task1
from celery_app import task2


task1.add.delay(2, 4)
task2.multiply.delay(4, 5)
print('end task')

```

#### 启动
```sh
celery worker -A celery_app -l INFO
```

#### 执行任务
```sh
python app.py
```


#### celery 定时任务
>celery 4.1.0时区存在问题
https://github.com/celery/celery/issues/4177

|--celery_app
   |--__init__.py
   |--celeryconfig.py
   |--task1.py
   |--task2.py
|--app.py

```py
# __init__.py
from celry import Celery

app = Celery('demo')
app.config_from_object('celery_app.celeryconfig')  # 通过Celery实例加载配置文件

```

```py
# celeryconfig.py
from datetime import timedelta

from celery.schedules import crontab

BROKER_URL = 'redis://localhost:6379/1'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'

CELERY_TIMEZONE = 'Asia/Shanghai'  # 默认UTC

# 导入指定的任务模块
CELERY_IMPORTS = (
	'celery_app.task1',
	'celery_app.task2'
	)

CELERYBEAT_SCHEDULE = {
	'task1': {
		'task': 'celery_app.task1.add',
		'schedule': timedelta(seconds=10),
		'args': (2, 8)
	},
	'task2': {
		'task': 'celery_app.task2.multiply',
		'schedule': crontab(hour=19, minute=30),
		'args': (2, 8)
	}
}

```

```py
# task1.py
import time

from celery_app import app


@app.task
def add(x, y):
	time.sleep(3)
	return x + y

```

```py
# task2.py
import time

from celery_app import app


@app.task
def multiply(x, y):
	time.sleep(3)
	return x * y

```


```py
# app.py
from celery_app import task1
from celery_app import task2


task1.add.delay(2, 4)
task2.multiply.delay(4, 5)
print('end task')

```

#### 启动
```sh
## 第一种
# 启动beat
celery beat -A celery_app -l INFO
# 启动worker
celery worker -A celery_app -l INFO

## 第二种
celery -B -A celery_app worker -l INFO

```

#### 执行任务
```sh
python app.py
```



