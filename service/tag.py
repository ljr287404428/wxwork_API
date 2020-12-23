# -*- coding:utf-8 -*-
# @Time   : 2020/12/22 23:05
# @Autor  : LL
# @File  :  tag.py
import json
import requests

corpid = "ww30a11017182cf656"
corpsecret = "Z5U9O_eZwXTO0cAyd28uz0BE6FMmEZX_6ZUZTZ0XFq0"


class Tag:
    # 构造方法，创建token变量
    def __init__(self):
        self.token = ""

    # 获取token的方法
    def get_token(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params={
                             "corpid": corpid,
                             "corpsecret": corpsecret
                         })
        print(json.dumps(r.json(), indent=2))
        self.token = r.json()["access_token"]

    # 获取列表的方法（查询）
    def list(self):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
                          params={"access_token": self.token},
                          json={
                              "tag_id": []  # id为空时，默认查询全部列表数据
                          }
                          )
        print(json.dumps(r.json(), indent=2))
        return r

    # 添加标签的方法
    def add(self, group_name, tags):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
                          params={"access_token": self.token},
                          json={
                              "group_name": group_name,
                              "tag": tags
                          }
                          )
        print(json.dumps(r.json(), indent=2))
        return r

    # 删除列表中标签的方法
    def delte(self, tag_id=None, group_id=None, agentid=None):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
                          params={"access_token": self.token},
                          json={
                              "tag_id": tag_id,
                              "group_id": group_id,
                              "agentid": agentid
                          })
        return r
