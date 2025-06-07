import logging
import os
from datetime import datetime


class Log():
    # 获取当前日期
    date = datetime.now().strftime('%Y-%m-%d')

    # 获取当前文件的目录
    current_path = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(current_path, 'log')

    # 如果log文件夹不存在，创建它
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    # 设置日志文件的路径
    log_file = os.path.join(log_path, f'console_{date}.txt')

    # 配置日志设置
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        filename=log_file)

    logger = logging.getLogger(__name__)
    logger.info('This is a log info')


if __name__ == "__main__":
    Log()
