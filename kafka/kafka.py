# -*- coding: utf-8 -*-

"""
  @date  2019-10-03 
  @author  liuwenyi
  
"""
from pykafka import KafkaClient

host = 'hadoop01:9092, hadoop02:9092, hadoop03:9092'
client = KafkaClient(hosts=host)

print(client.topics)

# 消费者
topic = client.topics['flume-pyLog']
consumer = topic.get_simple_consumer(consumer_group='test', auto_commit_enable=True, auto_commit_interval_ms=1,
                                     consumer_id='test')
for message in consumer:
    if message is not None:
        print(message.offset, message.value)
