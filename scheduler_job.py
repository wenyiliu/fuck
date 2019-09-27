# -*- coding: utf-8 -*-

"""
  @date  2019-09-26 
  @author  liuwenyi
  
"""
import datetime
from analysis import *
from apscheduler.schedulers.blocking import BlockingScheduler
from log.logger_factory import *


def run_job():
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    log_name = f'a/b/c/point.{yesterday}.log'
    log_to_mysql = Log(log_name, **config)
    log_to_mysql.insert_data()
    log_to_mysql.delete_data()


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(run_job, 'cron', hour=11, minute=22)
    logger = LoggerFactory("schedulers_job.class")
    try:
        scheduler.start()
        logger.info("定时将日志数据写入数据库成功")
    except(KeyboardInterrupt, SystemExit):
        logger.error("定时将日志数据写入数据库失败")
