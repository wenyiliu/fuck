# -*- coding: utf-8 -*-

"""
  @date  2019-09-26 
  @author  liuwenyi
  
"""
import datetime
import json
import pymysql
from log import *


class LogToMysql(object):
    def __init__(self, log_name, **kwargs):
        self.logger = LoggerFactory('LogToMysql.class')
        self.__log_name = log_name
        self.__mysql = Mysql(**kwargs)

    def __get_log(self):
        log_data = []
        try:
            file = open(self.__log_name, 'r')
            for line in file.readlines():
                log_data.append(json.loads(line))
            return log_data
        except IOError as e:
            print(f"{self.__log_name}文件不存在")
            self.logger.error(f"读取日志文件 {self.__log_name} 失败,原因:{e}")
            return log_data

    def insert_data(self):
        data_list = self.__get_log()
        list_ = []
        for data_dic in data_list:
            dict_ = dict(data_dic)
            user_id = dict_.get('userId', '')
            patient_id = dict_.get('patientId', '')
            if user_id == '':
                user_id = 0
            if patient_id == '':
                self.logger.info(f"患者ID为空,跳过写入数据库,日志:{data_dic}")
                continue
            value = (
                int(user_id), int(patient_id), dict_.get('methodName', ''),
                dict_.get('path', ''), dict_.get('referer', ''),
                dict_.get('timestamp', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
                dict_.get('ip', ''), dict_.get('params', ''))
            list_.append(value)
        sql = 'INSERT INTO yb_point_log_data(`user_id`, `patient_id`, `method_name` , `path`, `referer` ,' \
              ' `timestamp`, `ip`, `params`)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
        self.__mysql.batch_insert(sql, list_)
        self.logger.info(f"日志写入成功,count:{len(list_)}")

    def delete_data(self):
        delete_date = datetime.date.today() - datetime.timedelta(days=7)
        sql = f"DELETE FROM yb_point_log_data where date(`timestamp`)={delete_date}"
        self.__mysql.delete(sql)
        self.logger.info(f"删除 {delete_date} 数据成功")


class Mysql(object):
    def __init__(self, **kwargs):
        self.__config = kwargs
        self.logger = LoggerFactory("Mysql.class")

    def __connect(self):
        conn = None
        cursor = None
        try:
            conn = pymysql.connect(**self.__config)
        except pymysql.Error as e:
            print("MySQL 连接异常", e)
            self.logger.error(f"MySQL 连接异常,原因:{e}")
            conn.rollback()
        if conn is not None:
            cursor = conn.cursor()
        return conn, cursor

    @staticmethod
    def __close(conn, cursor):
        conn.commit()
        cursor.close()
        conn.close()

    def insert(self, sql):
        pass

    def batch_insert(self, sql, values=None):
        conn, cursor = self.__connect()
        if values is None or values == []:
            self.__close(conn, cursor)
            return
        cursor.executemany(sql, values)
        self.__close(conn, cursor)

    def delete(self, sql):
        conn, cursor = self.__connect()
        cursor.execute(sql)
        self.__close(conn, cursor)
