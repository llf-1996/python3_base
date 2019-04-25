
## django配置celery

### 启动
**异步任务**
```py
python manage.py runserver
python manage.py celery worker -l info
```

**定时任务**
```py
python manage.py runserver
python manage.py celery worker -l info
python manage.py celery beat -l info
```


