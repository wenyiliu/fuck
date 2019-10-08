# -*- coding: utf-8 -*-

"""
  @date  2019-09-30 
  @author  liuwenyi
  
"""
from pyhive import hive

conn = hive.Connection(host='114.55.103.110', port=10000, username='admin',
                       database='yibao_health')
cursor = conn.cursor()
cursor.execute('show tables')

for result in cursor.fetchall():
    print(result)
