'''
工具方法
'''
import re

#########################################################################
#           re
########################################################################
def clear_html_re(src_html):
    '''
    正则清除HTML标签
    :param src_html:原文本
    :return: 清除后的文本
    '''
    content = re.sub(r"</?(.+?)>", "", src_html)  # 去除标签
    dst_html = re.sub(r"\s+", "", content)  # 去除空白字符
    return dst_html


def get_content(url):
    '''
    从url中获取网页，返回文本内容
    :param url:
    :return: 文本内容
    '''
    # 处理编码
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
    res = requests.get(url, headers=header_dict).content
    a = res.decode('utf-8')
    # 去标签
    the_content = clear_html_re(a)
    return the_content


