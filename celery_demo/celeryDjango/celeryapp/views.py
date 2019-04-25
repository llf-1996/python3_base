from django.shortcuts import render
from django.http import JsonResponse

from celeryapp.tasks import CeleryTask


# Create your views here.
def do(request):
    # 执行异步任务
    print('start do request')
    CeleryTask.delay()
    print('end do request')
    return JsonResponse({'result': 'ok'})

