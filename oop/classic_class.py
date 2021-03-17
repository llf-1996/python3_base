# -*- encoding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/3/17 09:33
# @Author  : llf
# @File    : classic_class.py
'''
py2
存在经典类和新式类
多重继承
经典类的钻石继承是深度优先，即从下往上搜索。
'''


class ClassicClassA():
    var = 'Classic Class A'


class ClassicClassB(ClassicClassA):
    pass


class ClassicClassC():
    var = 'Classic Class C'


class SubClassicClass(ClassicClassB, ClassicClassC):
    pass


if __name__ == '__main__':
    print(SubClassicClass.var)
