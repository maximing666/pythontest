#!/usr/bin/env python
# coding=utf8
import sys

from mq_http_sdk.mq_exception import MQExceptionBase
from mq_http_sdk.mq_producer import *
from mq_http_sdk.mq_client import *
import time

#初始化 client
mq_client = MQClient(
    #设置HTTP接入域名（此处以公共云生产环境为例）
    "http://1307181505511393.mqrest.cn-beijing.aliyuncs.com",
    #AccessKey 阿里云身份验证，在阿里云服务器管理控制台创建
    "LTAI4GAUGTi5FxyEjzcCkPGK",
    #SecretKey 阿里云身份验证，在阿里云服务器管理控制台创建
    "PMkNjhdhLGJHubQWJcCdK3ax7DQhBZ"
	)
#所属的 Topic
topic_name = "yfd-case"
#Topic所属实例ID，默认实例为空None
instance_id = "${INSTANCE_ID}"

producer = mq_client.get_producer(instance_id, topic_name)

# 循环发布多条消息
msg_count = 4
print("%sPublish Message To %s\nTopicName:%s\nMessageCount:%s\n" % (10 * "=", 10 * "=", topic_name, msg_count))

try:
    for i in range(msg_count):
        if i % 2 == 0:
            msg = TopicMessage(
                    # 消息内容
                    "I am test message %s.你好" % i,
                    # 消息标签
                    ""
                    )
            # 设置属性
            msg.put_property("a", "i")
            # 设置KEY
            msg.set_message_key("MessageKey")
            re_msg = producer.publish_message(msg)
            print("Publish Message Succeed. MessageID:%s, BodyMD5:%s" % (re_msg.message_id, re_msg.message_body_md5))
        else:
            msg = TopicMessage(
                    # 消息内容
                    "I am test message %s." % i,
                    # 消息标签
                    ""
                    )
            msg.put_property("a", i)
            # 定时消息,毫秒级绝对时间
            msg.set_start_deliver_time(int(round(time.time() * 1000)) + 5 * 1000)
            re_msg = producer.publish_message(msg)
            print("Publish Timer Message Succeed. MessageID:%s, BodyMD5:%s" % (re_msg.message_id, re_msg.message_body_md5))
        time.sleep(1)
except MQExceptionBase as e:
    if e.type == "TopicNotExist":
        print("Topic not exist, please create it.")
        sys.exit(1)
    print("Publish Message Fail. Exception:%s" % e)