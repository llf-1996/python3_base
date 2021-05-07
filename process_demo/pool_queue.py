# -*- encoding: utf-8 -*-
from multiprocessing import Pool, Manager
import os, time, random


class MyPool(object):
    def __init__(self, count):
        self.pool = Pool(count)
        self.queue = Manager().Queue()

    def start_task(self, task, datas, max_count=3):
        for i in range(0, len(datas), max_count):
            data = datas[i: i+max_count]
            self.pool.apply_async(task, args=(self.queue, data))
        self.pool.close()
        self.pool.join()

    def get_result(self):
        print('=================================')
        print('Get queue data...')
        while True:
            if self.queue.empty():
                print('empty')
                break
            value = self.queue.get()
            print('Get %s from queue.' % value)
        return True


def task(q, datas):
    '''
    写数据进程执行的代码
    '''
    print('Process to write: %s' % os.getpid())
    for value in datas:
        print('Put %s to queue...' % value)
        q.put(value**2)
        time.sleep(random.random())


def main():
    print('Parent process %s.' % os.getpid())
    datas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    count = 3  # 进程数
    my_pool_obj = MyPool(count)
    my_pool_obj.start_task(task, datas)
    my_pool_obj.get_result()
    return True


if __name__ == '__main__':
    main()
