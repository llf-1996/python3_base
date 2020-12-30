>python 3.7
>celery 5.0.5

## 安装
```sh
pip install celery==5.0.5
pip install redis==3.5.3  # 使用redis作为broker或backend
```

## 异步任务：
* tasks.py

#### 启动
启动worker:
```bash
celery -A tasks worker -l INFO
```
* -A tasks  # 指定worker所在模块
* -l info   # 指定日志级别
#### 执行
```bash
python tasks.py
```

## 定时任务：
* |--app.py
* |--celery_app
  +   |--__init__.py
  +   |--celeryconfig.py
  +   |--task1.py
  +   |--task2.py

#### 启动：
第一种：
```bash
$ celery -A celery_app beat -l INFO
$ celery -A celery_app worker -l INFO
```
第二种：
```bash
$ celery -A celery_app worker -B -l INFO
```
#### 执行
```bash
# 执行异步任务
$ python app.py
```


## 错误汇总
#### window

1. asks, accept, hostname = _loc ValueError: not enough values to unpack (expected 3, got 0)
解决方案:
```bash
pip install eventlet # 协程包
# 启动celery指定池实现为eventlet
celery -A tasks --loglevel=info -P eventlet
```
参考博客：https://blog.csdn.net/diqiuyi7777/article/details/88314549
