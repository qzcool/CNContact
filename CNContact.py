#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""CNContact: 从包含联系方式的中文字符串中提取结构化数据。"""

__author__ = 'Qiao Zhang'

class CNContact:
    def __init__(self, content):
        self.content = content

    def phone(self):
        """
        提取手机号码/固定电话。
        :return: 手机号码/固定电话，格式为Str。
        """
        pass