# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2020/8/26 2:52 下午
# @Author  : llf
# @File    : mysql_ctr.py
import math

import pymysql

filterdbip = '127.0.0.1'
clinvar_conf = {
    'host': filterdbip,
    'username': 'jingzhundb',
    'passwd': 'jingzhundb',
    'dbname': 'jingzhundb',
    'port': 3306,
    'table_name': 'clinvar_combine_GRCh37',
    'charset': 'utf8',
}


class MysqlDbController(object):
    '''pymysql默认关闭autocommit'''
    def __init__(self, dbconf):
        self.host = dbconf['host']
        self.user = dbconf['username']
        self.passwd = dbconf['passwd']
        self.db = dbconf['dbname']
        self.port = dbconf['port']
        self.table = dbconf['table_name']
        self.charset = dbconf['charset']
        self.conn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db, port=self.port,
                                    charset=self.charset)
        self.cursor = self.conn.cursor()
        self.page_size = 100
        self.total_count = 1
        self.max_page = 1
        self.current_page = 1
        self.p_page = 0
        self.n_page = 2

    def start_autocommit(self):
        '''
        开启自动提交事务
        Returns:

        '''
        self.conn.autocommit(True)

    def stop_autocommit(self):
        '''
        关闭自动提交事务
        Returns:

        '''
        self.conn.autocommit(False)

    def get_count(self):
        '''
        查询表中数据总条数
        :return: long
        '''
        sql = 'select count(*) from {};'.format(self.table)
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        count = data[0]
        return count

    def delete_datas(self):
        '''
        清空表
        :return:
        '''
        sql = 'delete from {}'.format(self.table)
        self.cursor.execute(sql)

    def commit_transactions(self):
        '''提交'''
        self.conn.commit()

    def roll_back(self):
        '''回滚'''
        self.conn.rollback()

    def create_write_lock(self):
        '''添加写锁'''
        sql = 'lock tables {} write;'.format(self.table)
        self.cursor.execute(sql)

    def create_read_lock(self):
        '''添加读锁'''
        sql = 'lock tables {} read'.format(self.table)
        self.cursor.execute(sql)

    def release_lock(self):
        '''释放锁'''
        sql = 'unlock tables;'
        self.cursor.execute(sql)

    def close_conn(self):
        '''
        关闭连接
        :return:
        '''
        self.conn.close()

    def select_table(self, sql):
        '''
        查询数据
        :param sql:
        :return:
        '''
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        return datas

    def insert_data(self, col_keys, data):
        '''
        插入单行数据
        :param col_keys: 插入字段名list
        :param data: 数据list
        :return:
        '''
        insert_cols = '(' + ','.join(col_keys) + ')'
        placeholder_list = ['%s'] * len(col_keys)
        insert_placeholders = '(' + ','.join(placeholder_list) + ')'
        sql = 'insert into {}{} values{};'.format(self.table, insert_cols, insert_placeholders)
        try:
            self.cursor.execute(sql, data)
        except:
            pass

    def insert_datas(self, col_keys, datas):
        '''
        插入多行数据
        :param col_keys: 插入字段名list
        :param datas: 数据list
        :return:
        '''
        insert_cols = '(' + ','.join(col_keys) + ')'
        placeholder_list = ['%s'] * len(col_keys)
        insert_placeholders = '(' + ','.join(placeholder_list) + ')'
        sql = 'insert into {}{} values{};'.format(self.table, insert_cols, insert_placeholders)
        for data in datas:
            try:
                self.cursor.execute(sql, data)
            except Exception as e:
                with open('custom_tools/externalDb.py insert_datas.log', 'a')as f:
                    # f.write('cols:{}===placeholders:{}\n'.format(insert_cols, insert_placeholders))
                    f.write('insert datas error--->{}\n'.format(e, data))

    def replace_datas(self, col_keys, datas):
        '''
        替换多行数据
        :param col_keys: 插入字段名list
        :param datas: 数据list
        :return:
        '''
        replace_cols = '(' + ','.join(col_keys) + ')'
        placeholder_list = ['%s'] * len(col_keys)
        replace_placeholders = '(' + ','.join(placeholder_list) + ')'
        sql = 'replace into {}{} values{};'.format(self.table, replace_cols, replace_placeholders)
        for data in datas:
            try:
                self.cursor.execute(sql, data)
            except Exception as e:
                print(replace_cols, replace_placeholders)
                print('replace datas error:{}=={}'.format(str(e) + str(data)))

    def varify_page_num(self, varify_sql):
        '''
        验证页面是否可用，不可用重置页面信息
        :param sql:
        :param page_number:
        :return:
        '''
        self.cursor.execute(varify_sql)
        datas = self.cursor.fetchone()
        total_count = datas[0]
        max_page_number = int(math.ceil(total_count/self.page_size))
        self.total_count = total_count
        self.max_page = max_page_number
        if 1 <= self.current_page <= self.max_page:
            # 下一页
            self.n_page = self.current_page + 1 if self.current_page < self.max_page else 0
            # 上一页
            self.p_page = self.current_page - 1 if self.current_page >= 2 else 0
        else:
            self.current_page = 1
            self.p_page = 0
            self.n_page = 2 if self.max_page >= 2 else 0

    def format_raw_datas(self, datas, cols_list):
        '''
        将查询到的数据格式化为dict
        Args:
            datas: list
            cols_list: 表查询字段list

        Returns: [True/False],datas([{}.{}...]),message

        '''
        new_datas = []
        if len(datas) > 0:
            if len(datas[0]) != len(cols_list):
                return False, new_datas, '无法格式化'
            cols_len = len(cols_list)
            index_list = range(cols_len)
            for data in datas:
                data_dict = {}
                for i in index_list:
                    data_dict[cols_list[i]] = data[i]
                new_datas.append(data_dict)
        return True, new_datas, 'success'


def create_clinvar():
    clinvar_table = MysqlDbController(clinvar_conf)
    return clinvar_table


def select_clinvar_table(pms):
    '''
    获取clivar数据，分页
    :param page_number:
    :return:
    '''
    datas = {}
    clinvar_table = create_clinvar()
    gene_name = pms.get('gene_name')
    search_type = pms.get('search_type')
    search_value = pms.get('search_value')
    ClinicalSignificance = pms.getlist('checked_types')
    search_gene_name, search_chrom, search_pos = [False, False, False]
    if search_type == 'gene_name':
        search_gene_name = search_value.strip()
    elif search_type == 'pos':
        search_chrom, search_pos = search_value.strip().split(':')
    where_sql_list = []
    if gene_name:
        where_sql_list.append('genes_symbol="{}"'.format(gene_name))
    if search_gene_name:
        where_sql_list.append('genes_symbol="{}"'.format(search_gene_name))
    if search_chrom and search_pos:
        where_sql_list.append("chrom='{}' and pos={}".format(search_chrom, search_pos))
    if ClinicalSignificance:
        # 编码问题
        ClinicalSignificance = str(ClinicalSignificance).replace("u'", "'")
        ClinicalSignificance = '(' + ClinicalSignificance[1:-1] + ')'
        where_sql_list.append('ClinicalSignificance in {}'.format(ClinicalSignificance))
    if where_sql_list:
        where_sql = 'where ' + ' and '.join(where_sql_list)
    else:
        where_sql = ''
    clinvar_table.current_page = int(pms.get('page', 1))
    # datas = test.select_table(sql)
    select_sql = 'select searchpos, CHROM, POS, REF, ALT, ' \
                 'AlleleID, ClinicalSignificance, ClinSigSimple, LastEvaluated, Cytogenetic, ' \
                 'ReviewStatus, NumberSubmitters, type, name, genes_symbol, ' \
                 'hgnc_id ' \
                 'from clinvar_combine_GRCh37 ' \
                 ' {} ' \
                 'limit {}, {};'.format(where_sql, (clinvar_table.current_page - 1) * clinvar_table.page_size, clinvar_table.page_size)
    varify_sql = 'select count(*) ' \
                 'from clinvar_combine_GRCh37 ' \
                 ' {} ;'.format(where_sql)
    clinvar_table.varify_page_num(varify_sql)

    datas['results'] = clinvar_table.select_table(select_sql)
    clinvar_table.close_conn()
    datas['page_info'] = {
        'count': clinvar_table.total_count,
        'max_page': clinvar_table.max_page,
        'p_page': clinvar_table.p_page,
        'current_page': clinvar_table.current_page,
        'n_page': clinvar_table.n_page,
    }
    return datas


if __name__ == '__main__':
    # pms = {
    #     'page': '1',
    #     'gene_name': 'ENTPD1',
    #     'search_value': 'ENTPD1-AS1',
    #     'search_type': 'gene_name',
    # }
    # res = select_clinvar_table(pms)
    # print res
    res = create_clinvar()
    # res.delete_datas()
    res.create_write_lock()
    res.release_lock()
    res.close_conn()
