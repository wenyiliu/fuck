# -*- coding: utf-8 -*-

"""
  @date  2019-09-27 
  @author  liuwenyi
  
"""
import logging
from pyLog.logger import Logger


class Critical(Logger):
    def __init__(self, class_name, file_path):
        self.class_name = class_name
        Logger.__init__(self, file_path, logging.CRITICAL)

    def critical(self, message):
        self.logger.critical(self.class_name + self.pointer + message)


class Debug(Logger):
    def __init__(self, class_name, file_path):
        self.class_name = class_name
        Logger.__init__(self, file_path, logging.DEBUG)

    def debug(self, message):
        self.logger.debug(self.class_name + self.pointer + message)


class Error(Logger):
    def __init__(self, class_name, file_path):
        self.class_name = class_name
        Logger.__init__(self, file_path, logging.ERROR)

    def error(self, message):
        self.logger.error(self.class_name + self.pointer + message)


class Warn(Logger):
    def __init__(self, class_name, file_path):
        self.class_name = class_name
        Logger.__init__(self, file_path, logging.WARN)

    def warn(self, message):
        self.logger.warn(self.class_name + self.pointer + message)


class Info(Logger):
    def __init__(self, class_name, file_path):
        self.class_name = class_name
        Logger.__init__(self, file_path, logging.INFO)

    def info(self, message):
        self.logger.info(self.class_name + self.pointer + message)
