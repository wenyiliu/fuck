# -*- coding: utf-8 -*-

"""
  @date  2019-09-27 
  @author  liuwenyi
  
"""
from pyLog.xml.xml_parser import level_config, log_backup_count, log_max_size_config
import logging.handlers
import logging
import os
import sys


class Logger:
    def __init__(self, file_path, level):
        self.log_file_path = file_path
        self.pointer = " :  "
        self.logger = logging.getLogger(self.log_file_path)
        self.logger.setLevel(level)

        # 当self.log_file_path相同时，会重复添加handler 导致多次写入
        if not self.logger.handlers:
            self.add_handler()

        self.package_name = self.get_package_name()

    def add_handler(self):

        # 设置文件日志大小、备份个数
        back_count = int(log_backup_count())
        log_max_size = int(log_max_size_config()) * 1024 * 1024
        fh = logging.handlers.RotatingFileHandler(self.log_file_path, maxBytes=log_max_size, backupCount=back_count)

        # 设置输出格式
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        fh.setFormatter(fmt)

        # 配置level 默认输出notset以上的
        fh.setLevel(level_config(default="NOTSET"))
        self.logger.addHandler(fh)

    @staticmethod
    def get_package_name():
        p_name = os.getcwd().split("\\")[-1]
        f_name = os.path.basename(sys.argv[0]).replace("fuck", "class")
        if p_name:
            return "%s-%s" % (p_name, f_name)
        else:
            return f_name
