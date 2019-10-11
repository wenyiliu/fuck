# -*- coding: utf-8 -*-

"""
  @date  2019-09-26 
  @author  liuwenyi

"""
import datetime
from analysis import *
from apscheduler.schedulers.blocking import BlockingScheduler
from pyLog.logger_factory import *

log_to_mysql = Log(**config)
logger = LoggerFactory("schedulers_job.class")


def insert_job():
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    log_name = f'/usr/local/pro/tomcat-dawn/logs/point.{yesterday}.log'
    try:
        log_to_mysql.insert_data(log_name)
    except Exception as e:
        logger.error(f"{log_name} 日志数据写入数据库失败,原因:{e}")


def delete_job():
    delete_date = datetime.date.today() - datetime.timedelta(days=7)
    try:
        log_to_mysql.delete_data(delete_date)
    except Exception as e:
        logger.error(f"{delete_date} 数据删除失败,原因:{e}")


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(insert_job, 'cron', hour=1, minute=5)
    scheduler.add_job(delete_job, 'cron', hour=1, minute=6)
    try:
        scheduler.start()
    except(KeyboardInterrupt, SystemExit) as e:
        logger.error(f"日志数据写入数据库失败,原因:{e}")
