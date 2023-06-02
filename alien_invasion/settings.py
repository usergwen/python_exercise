#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/6/3 00:19
# @Author  : wen
# @File    : settings.py
# @Software: PyCharm

class Settings:
    """存储游戏系所有设置"""
    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)