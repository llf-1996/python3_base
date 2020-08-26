# coding: utf8
# @version : 2
# @Time    : 2020/3/26 4:13 下午
# @Author  : llf
# @File    : extract_zip_demo.py
import os
import zipfile


def extract_zip(filepath, file_full_name):
    '''
    解压文件
    Args:
        filepath: /a/a.zip
        file_full_name: a.txt

    Returns: /a/a.txt

    '''
    file_type = os.path.splitext(filepath)[1]
    if file_type == '.zip':
        # 解压文件
        try:
            zip_obj = zipfile.ZipFile(filepath)
            dir_path = os.path.dirname(filepath)
            file_path = zip_obj.extract(file_full_name, dir_path)
            return file_path
        except:
            return None

