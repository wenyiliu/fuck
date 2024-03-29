# -*- coding: utf-8 -*-

"""
  @date  2019-09-27 
  @author  liuwenyi
  
"""
import os
from os import path
from pyLog.Log import *


class LoggerFactory:
    log_dir = None

    def __init__(self, class_name):
        if LoggerFactory.log_dir is None:
            cur_path = path.dirname(__file__)
            parent_path = os.path.dirname(cur_path)  # 获得d所在的目录,即d的父级目录
            LoggerFactory.log_dir = parent_path + "/logs"

        self.debug_path = LoggerFactory.log_dir + "/debug.pyLog"
        self.info_path = LoggerFactory.log_dir + "/info.pyLog"
        self.warn_path = LoggerFactory.log_dir + "/warn.pyLog"
        self.error_path = LoggerFactory.log_dir + "/error.pyLog"
        self.critical_path = LoggerFactory.log_dir + "/critical.pyLog"

        self.__debug = Debug(class_name, self.debug_path)
        self.__info = Info(class_name, self.info_path)
        self.__warn = Warn(class_name, self.warn_path)
        self.__error = Error(class_name, self.error_path)
        self.__critical = Critical(class_name, self.critical_path)

    def debug(self, msg):
        self.__debug.debug(msg)

    def info(self, msg):
        self.__info.info(msg)

    def warn(self, msg):
        self.__warn.warn(msg)

    def error(self, msg):
        self.__error.error(msg)

    def critical(self, msg):
        self.__critical.critical(msg)
