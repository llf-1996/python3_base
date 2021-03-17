# -*- encoding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/3/17 09:30
# @Author  : llf
# @File    : new_style_class.py
'''
py3
只有新式类
多重继承
新式类的继承顺序是采用C3算法（非广度优先）。
'''


class NewStyleClassA(object):
    var = 'New Style Class A'


class NewStyleClassB(NewStyleClassA):
    pass


class NewStyleClassC(object):
    var = 'New Style Class C'


class SubNewStyleClass(NewStyleClassB, NewStyleClassC):
    pass


if __name__ == '__main__':
    # 非广度优先
    print(SubNewStyleClass.mro())
    print(SubNewStyleClass.var)
    # [<class '__main__.SubNewStyleClass'>, < class '__main__.NewStyleClassB' >, < class '__main__.NewStyleClassA' >, < class '__main__.NewStyleClassC' >, < class 'object' >]
    # New Style Class A
