# coding: utf8
# @version : 2
# @Time    : 2020/3/26 3:20 下午
# @Author  : llf
# @File    : sys_demo.py

import sys


def hello_world():
    print sys.argv[0]
    print sys.argv[1], sys.argv[2]
    print sys.argv


if __name__ == '__main__':
    hello_world()

'''
sys通过argv来获取命令行参数，其中argv[0]获取的是脚本的名称，从argv[1]开始获取的是命令行传入的参数。
# 输出
# python sys_demo.py 1 2 3
>>> sys_demo.py
>>> 1 2
'''
