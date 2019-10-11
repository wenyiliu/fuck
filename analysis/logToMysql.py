# -*- coding: utf-8 -*-

"""
  @date  2019-09-26 
  @author  liuwenyi

"""
import datetime
import json
import pymysql
from pyLog import *


class LogToMysql(object):
    def __init__(self, **kwargs):
        self.__logger = LoggerFactory('LogToMysql.class')
        self.__mysql = Mysql(**kwargs)

    def __get_log(self, log_name):
        log_data = []
        try:
            file = open(log_name, 'r')
            for line in file.readlines():
                log_data.append(json.loads(line))
            return log_data
        except IOError as e:
            self.__logger.error(f"读取日志文件 {log_name} 失败,原因:{e}")

    def insert_data(self, log_name):
        data_list = self.__get_log(log_name)
        list_ = []
        count = 0
        for data_dic in data_list:
            dict_ = dict(data_dic)
            user_id = dict_.get('userId', '')
            patient_id = dict_.get('patientId', '')
            try:
                if user_id == '' or user_id == 'null':
                    user_id = 0
                if patient_id == '' or patient_id == 'null':
                    count += 1
                    continue
            except Exception as e:
                self.__logger.error(f"{data_dic} 数据转化失败:{e}")
                continue

            try:
                value = (
                    int(user_id), int(patient_id), dict_.get('methodName', ''),
                    dict_.get('path', ''), dict_.get('referer', ''),
                    dict_.get('timestamp', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
                    dict_.get('ip', ''), dict_.get('params', ''))
                list_.append(value)
            except Exception as e:
                self.__logger.error(f"获取字典 {data_dic} 值失败:{e}")
                continue

        sql = 'INSERT INTO yb_point_log_data(`user_id`, `patient_id`, `method_name` , `path`, `referer` ,' \
              ' `timestamp`, `ip`, `params`)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
        self.__mysql.batch_insert(sql, list_)
        self.__logger.info(f"{log_name}日志写入成功,count:{len(list_)},跳过{count}条数据")

    def delete_data(self, delete_date):
        sql = f"DELETE FROM yb_point_log_data WHERE DATE(`timestamp`)<='{delete_date}'"
        self.__mysql.delete(sql)
        self.__logger.info(f"删除 {delete_date} 数据成功")


class Mysql(object):
    def __init__(self, **kwargs):
        self.__config = kwargs
        self.__logger = LoggerFactory("Mysql.class")

    def __connect(self):
        conn = None
        cursor = None
        try:
            conn = pymysql.connect(**self.__config)
        except pymysql.Error as e:
            self.__logger.error(f"MySQL 连接异常,原因:{e}")
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
            self.__logger.info(f"values={values},跳过写入数据库")
            return
        cursor.executemany(sql, values)
        self.__close(conn, cursor)

    def delete(self, sql):
        conn, cursor = self.__connect()
        cursor.execute(sql)
        self.__close(conn, cursor)
