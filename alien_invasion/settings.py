#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/6/3 00:19
# @Author  : wen
# @File    : settings.py
# @Software: PyCharm

class Settings:
    """游戏配置管理"""

    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
