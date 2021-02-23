# -*- encoding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/1/27 16:07
# @Author  : llf
# @File    : config.py
from __future__ import unicode_literals

primer_mysql_conf = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'root',
    'db': 'db1',
    'charset': 'utf8'
}

primer_tbls = {
    'tbl_1': {
        'name': 'student',
        'headers': [
            'id', 'name', 'age'
        ],
        'default_data': {
            'name': None,
            'age': 18
        }
    }
}
