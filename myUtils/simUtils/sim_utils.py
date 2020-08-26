'''
工具方法
'''
import difflib

from hashes.simhash import simhash



def content_similarity_difflib(content1, content2):
    '''
    difflib相似度比较
    比较纯文本文章内容相似度
    :param content1: 文章1
    :param content2: 文章2
    :return: 相似度值
    '''
    ratio = 0
    if content1 and content2:
        if 0.8 < len(content1) / len(content2) < 1.2:
            ratio = difflib.SequenceMatcher(None, content1, content2).ratio()
    return ratio


def content_similarity_simhash(content1, content2):
    '''simhash相似度'''
    # start1 = datetime.datetime.now()
    hash1 = simhash(content1)
    hash2 = simhash(content2)
    similar = hash1.similarity(hash2)
    return similar

