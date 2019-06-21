## 异步任务：
环境：win10、py3.6.5

安装redis:  pip install redis==2.8.0  
安装celery:  pip install celery==3.1.25  

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





