from django.shortcuts import render
from django.http import JsonResponse

from celeryapp.tasks import CeleryTask


# Create your views here.
def do(request):
    # 执行异步任务
    print('start do request')
    # CeleryTask.delay()
    CeleryTask.apply_async(args=[1, 2], kwargs={'name': 'l'}, queue='work_queue')  # 也可在这里指定参数和队列
    print('end do request')
    return JsonResponse({'result': 'ok'})

