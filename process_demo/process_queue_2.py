# -*- encoding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/5/6 14:57
# @Author  : llf
from multiprocessing import Process, Queue
import os, time, random


def write(q, datas):
    '''
    写数据进程执行的代码
    '''
    print('Process to write: %s' % os.getpid())
    for value in datas:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


def main():
    datas = [
        [1, 2, 3],
        ['a', 'b', 'c'],
        ['i', 'j', 'k']
    ]
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    process_objs = []
    for data in datas:
        pw = Process(target=write, args=(q, data))
        # 启动子进程
        pw.start()
        process_objs.append(pw)
    for pw in process_objs:
        # 等待子进程结束:
        pw.join()
    print('=================================')
    print('Get queue data...')
    while True:
        value = q.get(True)
        # value = q.get_nowait()
        print('Get %s from queue.' % value)
        if q.empty():
            print('empty')
            break
    return True


if __name__ == '__main__':
    main()
