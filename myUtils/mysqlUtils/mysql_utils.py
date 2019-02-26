'''
工具方法
'''
import pymysql


################################################################
#        mysql
################################################################
import requests


def get_datas_mysql(conn_info, sql):
    '''
    查询数据
    :param conn_info:  连接信息
    :param sql:  查询sql语句
    :return:  查询到的所有数据
    '''
    db = pymysql.connect(host=conn_info['host'], user=conn_info['user'],
                         password=conn_info['password'], db=conn_info['db'])
    # 使用 cursor() 方法创建游标对象 cursor
    cursor = db.cursor()
    cursor.execute(sql)
    datas = cursor.fetchall()
    db.close()
    return datas


def save_datas_mysql(conn_info, sql, datas):
    '''
    插入数据
    :param conn_info:  连接信息
    :param sql:  插入sql语句
    :param datas:  数据list
    :return:  查询到的所有数据
    '''
    # 目标数据库
    db_t = pymysql.connect(host=conn_info['host'], user=conn_info['user'],
                           password=conn_info['password'], db=conn_info['db'])
    # 使用 cursor() 方法创建游标对象 cursor
    cursor_t = db_t.cursor()
    for data in datas:
        # 异常处理
        try:
            # print(data[-1])
            cursor_t.execute(sql, data)
            # print('Insert a piece of data')
        except Exception as e:
            # print('insert error!', e)
            pass

    # 提交事务
    db_t.commit()
    db_t.close()

