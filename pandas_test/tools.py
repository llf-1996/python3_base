# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2020/8/26 2:02 下午
# @Author  : llf
# @File    : tools.py
import os

import pandas as pd


def read_file_from_path(fpath, file_type=None, encoding='utf-8'):
    '''
    pandas读取文件
    Args:
        fpath: 文件路径
        file_type: 文件类型(excel, csv, tsv)
        encoding: 编码方式

    Returns: status, dataframe

    '''
    if file_type:
        if file_type == 'excel':
            df = pd.read_excel(fpath, encoding=encoding)
            return True, df
        elif file_type == 'tsv':
            df = pd.read_csv(fpath, sep='\t', encoding=encoding)
            return True, df
        elif file_type == 'csv':
            df = pd.read_csv(fpath, sep=',', encoding=encoding)
            return True, df
        else:
            return False, '文件格式不支持'
    else:
        # 通过文件后缀名读取文件
        suffix = os.path.splitext(fpath)
        if suffix in ['.xlsx', '.xls']:
            df = pd.read_excel(fpath, encoding=encoding)
            return True, df
        elif suffix in ['.csv']:
            df = pd.read_csv(fpath, sep=',', encoding=encoding)
            return True, df
        elif suffix in ['.tsv', '.txt']:
            df = pd.read_csv(fpath, sep='\t', encoding=encoding)
            return True, df
        else:
            return False, '文件格式不支持'


def read_file_from_request_obj(file_obj):
    '''
    通过request文件对象读取文件
    Args:
        file_obj: request file obj

    Returns: status, dataframe

    '''
    file_name = file_obj.name
    suffix = os.path.splitext(file_name)[1]
    if suffix in ['.xlsx', '.xls']:
        df = pd.read_excel(file_obj)
        return True, df
    elif suffix == '.txt' or suffix == '.tsv':
        df = pd.read_csv(file_obj, sep='\t')
        return True, df
    elif suffix == '.csv':
        df = pd.read_csv(file_obj)
        return True, df
    else:
        return False, '无法读取文件'
