# coding: utf8
# @Time    : 2019-11-14 17:22
# @Author  : llf
# @File    : read_file_demo.py
import os

import pandas as pd


def read_data(fpath):
    '''
    pandas读取文件
    Args:
        fpath: 文件路径

    Returns: dataframe对象

    '''
    file_type = os.path.splitext(fpath)[1]

    if file_type in ['xls', 'xlsx']:
        df = pd.read_excel(fpath)
    else:
        df = pd.read_csv(fpath, sep='\t')
    return df


def insert_searchpos_col(fpath):
    '''
    读取文件，并新增searchpos列，数据为：chr + '_' + Start
    Args:
        fpath: 文件路径

    Returns: 无

    '''
    file_type = os.path.splitext(fpath)[1]
    if file_type in ['xls', 'xlsx']:
        df = pd.read_excel(fpath, low_memory=False)
    else:
        df = pd.read_csv(fpath, sep='\t', low_memory=False)
    df['searchpos'] = df.apply(lambda x: str(x['chr']) + '_' + str(x['Start']), axis=1)

    df.to_csv('./output/new_data.csv', index=False, sep='\t')


if __name__ == '__main__':
    # df = read_data('clinvar.csv')
    # print(df.columns)
    # print(df.columns.tolist())
    # for i, lis in df.iterrows():
    #     print(i)
    #     lists = lis.values.tolist()

    ff = open('./clinvar.csv')
    df = pd.read_csv(ff, sep='\t')

    print(df)


