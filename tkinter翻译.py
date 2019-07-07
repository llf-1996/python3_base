# !/usr/bin/python3
# coding:utf8

"""
@Author: llf
@File: 6.py
@IDE: Pycharm
@Time: 2019-07-07
"""
'''
GUI翻译---有道
tkinter
requests
'''
from tkinter import *

import requests


def fanyi():
    def youdao_translate():
        # url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"  # 最新
        url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        content = entry.get()
        data = {
            'i': content,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            # 'salt': '15624996098428',
            # 'sign': '612eda4762891f21aa6cae2a5a428e6b',
            'ts': '1562499609842',
            'bv': 'e2a78ed30c66e16a857c5b6486a1d326',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTION',
        }
        resp = requests.post(url, data=data)
        if resp.status_code == 200:
            resp = resp.json()['translateResult'][0][0]['tgt']
            # global res
            res.set(resp)
            return True

    root = Tk()

    # 变量
    res = StringVar()

    root.title("中英互译")
    # 窗口大小
    root.geometry("370x100")
    # 窗口位置
    root.geometry("+500+300")

    # 标签控件
    label = Label(root, text="原文：", font=("微软雅黑",))
    # 控件布局 grid pack place
    label.grid()
    label = Label(root, text="译文：", font=("微软雅黑",))
    # 控件布局 grid pack place
    label.grid()

    # 输入控件
    entry = Entry(root, font=("微软雅黑", 15))
    entry.grid(row=0, column=1)
    entry1 = Entry(root, font=("微软雅黑", 15), textvariable=res)
    entry1.grid(row=1, column=1)

    # 按钮控件
    button = Button(root, text="翻译", width=10, command=youdao_translate)
    # sticky 对齐方式 N S W E 上下左右
    button.grid(row=2, column=0, sticky=W)
    # command 触发的方法
    button1 = Button(root, text="退出", width=10, command=root.quit)
    button1.grid(row=2, column=1, sticky=E)

    # 显示窗口，消息循环
    root.mainloop()


if __name__ == '__main__':
    fanyi()
