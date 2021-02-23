# -*- encoding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/1/29 09:53
# @Author  : llf
# @File    : mysql_utils.py
from __future__ import unicode_literals
import pymysql

from .config import primer_mysql_conf, primer_tbls


def insert_data(data, table_name, db_conf):
    '''
    新增数据
    Args:
        data: dict
        table_name: str
        db_conf: dict
    Returns:
    '''
    db = pymysql.connect(**db_conf)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    keys = []
    values = []
    values_tags = []
    for k, v in data.items():
        keys.append(k)
        values.append(v)
        values_tags.append('%s')
    titles = ','.join(keys)
    values_tag = ','.join(values_tags)
    sql = 'INSERT INTO {}({}) VALUES ({});'.format(table_name, titles, values_tag)
    is_success = True
    try:
        cursor.execute(sql, values)
        db.commit()
    except Exception as e:
        print('{}表插入数据失败：{}'.format(table_name, e))
        db.rollback()
        is_success = False
    db.close()
    return is_success


def delete_datas(table_name, db_conf):
    '''
    清空表中数据
    Args:
        table_name: str
        db_conf: dict
    Returns:
    '''
    # 打开数据库连接
    db = pymysql.connect(**db_conf)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = 'DELETE FROM {};'.format(table_name)
    is_success = True
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print('{}表清空数据失败：{}'.format(table_name, e))
        db.rollback()
        is_success = False
    db.close()
    return is_success


def select_datas(table_name, header, db_conf):
    '''
    查询表中所有数据
    Args:
        table_name: str
        header: list
        db_conf: dict
    Returns:
    '''
    # 打开数据库连接
    db = pymysql.connect(**db_conf)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    header_str = ','.join(header)
    sql = 'SELECT {} FROM {};'.format(header_str, table_name)
    cursor.execute(sql)
    rowcount = cursor.rowcount
    query_datas = cursor.fetchall()
    cursor.close()
    # 关闭数据库连接
    db.close()
    if rowcount == 0:
        return False, []
    else:
        datas = []
        for query_data in query_datas:
            data = {}
            for i, k in enumerate(header):
                data[k] = query_data[i]
            datas.append(data)
        return True, datas


def get_gene_data(id, tbl_info):
    '''
    通过id查询
    Args:
        id:
        tbl_info: dict
    Returns:
    '''
    table_name = primer_tbls['gene']
    # 打开数据库连接
    db = pymysql.connect(**primer_mysql_conf)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 使用execute方法执行SQL语句
    select_header = ','.join(tbl_info['headers'])
    query_sql = 'SELECT {} FROM {} WHERE id=%s;'.format(select_header, table_name)
    cursor.execute(query_sql, [id])
    rowcount = cursor.rowcount
    query_datas = cursor.fetchall()
    cursor.close()
    # 关闭数据库连接
    db.close()
    if rowcount == 0:
        return False, tbl_info['default_data']
    else:
        datas = []
        for q_data in query_datas:
            data = {}
            for i, k in enumerate(tbl_info['headers']):
                data[k] = q_data[i]
            datas.append(data)
        return True, datas


def update_tbl_data(data, tbl_info):
    '''
    更新数据
    Args:
        data: dict
        tbl_info: dict
    Returns:
    '''
    table_name = tbl_info['name']
    # 打开数据库连接
    db = pymysql.connect(**primer_mysql_conf)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = 'UPDATE {} SET name=%s, age=%s WHERE id=%s;'.format(table_name)
    is_success = True
    try:
        cursor.execute(sql, [data['name'], data['age'], data['id']])
        db.commit()
    except Exception as e:
        print('{}表更新数据失败：{}'.format(table_name, e))
        db.rollback()
        is_success = False
    db.close()
    return is_success
