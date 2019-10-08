# -*- coding: utf-8 -*-

"""
  @date  2019-09-26 
  @author  liuwenyi
  
"""
import datetime
from analysis import *
from apscheduler.schedulers.blocking import BlockingScheduler
from pyLog.logger_factory import *

yesterday = datetime.date.today() - datetime.timedelta(days=1)
log_name = f'/usr/local/pro/tomcat-dawn/logs/point.{yesterday}.log'
log_to_mysql = Log(log_name, **config)
logger = LoggerFactory("schedulers_job.class")


def insert_job():
    log_to_mysql.insert_data()


def delete_job():
    log_to_mysql.delete_data()


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(insert_job(), 'cron', hour=2, minute=5)
    scheduler.add_job(delete_job, 'cron', hour=2, minute=6)
    try:
        scheduler.start()
        logger.info(f"{log_name}日志数据写入数据库成功")
    except(KeyboardInterrupt, SystemExit):
        logger.error(f"{log_name}日志数据写入数据库失败")
