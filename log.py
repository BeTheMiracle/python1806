#日志的简单使用
#1 导入logging模块
import logging
import sys
#设置日志记录级别 debug <info <warning <error
print(logging.DEBUG,logging.INFO,logging.WARNING,logging.ERROR)
logging.basicConfig(level=logging.DEBUG,
                 format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                 datefmt='%a, %d %b %Y %H:%M:%S',
                 filename='myapp.log',
                 filemode='a')

logging.debug('这是一个debug级别的日志')

logging.info('这是一个info级别的日志')

logging.warning('这是一个warning级别的日志')

logging.error('这是一个error级别的日志')
try:
     num = input('请输入一个数字')
     num = float(num)
except Exception as e:
     logging.error(e)
date
