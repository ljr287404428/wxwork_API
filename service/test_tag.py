# -*- coding:utf-8 -*-
# @Time   : 2020/12/22 22:24
# @Autor  : LL
# @File  :  test_tag.py
import pytest

from service.tag import Tag


# todo:代码冗余
# todo:与底层框架耦合太多
# todo：封装层次不足，不利于管理

class TestTag:
    def setup_class(self):
        self.tag = Tag()
        self.tag.get_token()
        ## todo:数据清理的过程,把测试数据清空或者还原
        # 先查询现有的列表数据
        r = self.tag.list()
        # 取出返回结果中所有标签的group_id
        list_group_id = [group_id.get("group_id") for group_id in r.json()["tag_group"]]
        r = self.tag.delte(group_id=list_group_id)

    # def test_tag_del(self):
    #     #先查询现有的列表数据
    #     r = self.tag.list()
    #     #取出返回结果中所有标签的group_id
    #     list_group_id = [group_id.get("group_id") for group_id in r.json()["tag_group"]]
    #
    #     r = self.tag.delte(group_id = list_group_id )
    #     print(json.dumps(r.json(), indent=2))

    # 测试查询标签列表的方法
    def test_tag_list(self):
        # todo:完善功能测试
        r = self.tag.list()
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

    @pytest.mark.parametrize("group_name,tag_names", [
        ["group_demo_1222", [{"name": "tag_demo_1222"}]],
        ["group_demo_1223", [{"name": "tag_demo_1223"}, {"name": "tag_demo_1224"}]]

    ])
    def test_tag_add(self, group_name, tag_names):  # 测试添加标签的方法
        r = self.tag.add(group_name, tag_names)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

        r = self.tag.list()
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

        group = [group for group in r.json()["tag_group"] if group["group_name"] == group_name][0]
        tags = [{"name": tag["name"]} for tag in group["tag"]]
        print(group)
        print(tags)
        assert group["group_name"] == group_name
        assert tags == tag_names
