# coding: utf8
# @version : 2
# @Time    : 2020/3/26 3:26 下午
# @Author  : llf
# @File    : argparse_demo.py

import argparse

arg = argparse.ArgumentParser('this is a test!')


def main(arg):
    print 'name:', arg.name
    print 'age', arg.age


if __name__ == '__main__':
    arg.add_argument('--name', '-n', default='llf', type=str, help='your name')
    arg.add_argument('--age', '-a', default=25, type=int, help='your age')
    args = arg.parse_args()
    main(args)


'''
➜  command_line_development git:(master) ✗ python argparse_demo.py --help
usage: this is a test! [-h] [--name NAME] [--age AGE]

optional arguments:
  -h, --help            show this help message and exit
  --name NAME, -n NAME  your name
  --age AGE, -a AGE     your age
➜  command_line_development git:(master) ✗ python argparse_demo.py -a 12 -n wangwu
name: wangwu
age 12
➜  command_line_development git:(master) ✗

'''
