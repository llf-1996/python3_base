'''
环境：win10、py3.6.5

运行程序之前需要先启动worker：celery worker -A tasks -l INFO
-A tasks指定worker，在当前文件夹下的tasks.py文件
-l info 指定日志级别

error:
asks, accept, hostname = _loc
ValueError: not enough values to unpack (expected 3, got 0)
解决方案:
第二种: pip install eventlet
启动celeryworker时: celery -A tasks --loglevel=info -P eventlet  # 协程

参考博客：https://blog.csdn.net/diqiuyi7777/article/details/88314549

'''
from tasks import add

if __name__ == '__main__':
    print('start task...')
    result = add.delay(2, 8)  # 异步调用
    print('end task...')
    print(result)
    print(result.ready())  # 任务是否完成
    print(result.get())  # 任务结果


