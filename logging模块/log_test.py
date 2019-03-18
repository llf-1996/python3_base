'''
+++ 实现增量更新
'''
import datetime
import logging
from logging.handlers import RotatingFileHandler

log_path = "./res/a.log"
logger = logging.getLogger("a")
logger.setLevel(logging.DEBUG)
# 输出到文件
# fh = logging.FileHandler("./res/a.log", encoding='utf8')
fh = RotatingFileHandler(log_path, maxBytes=200000, backupCount=7, encoding="utf-8")
'''
RotatingFileHandler函数参数说明：
log_path     日志路径，程序可自动创建
maxBytess    单个日志文件的大小
backupCount  最多保留几个日志文件
encoding     指定日志文件的编码格式
'''
fh.setLevel(logging.INFO)
# 设置日志格式
fomatter = logging.Formatter('%(asctime)s\t%(module)s\t%(message)s', '%Y-%m-%d %H:%M:%S')
fh.setFormatter(fomatter)
logger.addHandler(fh)


def main():
    for i in range(10):
        logger.info("this is a test!")


if __name__ == "__main__":
    t1 = datetime.datetime.now()
    print(t1)
    main()
    tt = datetime.datetime.now()
    cost_time = tt - t1
    print(t1, tt, cost_time)
    logger.info('run_time:%s' % cost_time)




