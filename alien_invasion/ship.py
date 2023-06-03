#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/6/3 00:25
# @Author  : wen
# @File    : ship.py
# @Software: PyCharm

import pygame

from settings import Settings


class Ship:
    """飞船管理"""

    def __init__(self, ai_game):
        self.settings = Settings()
        """初始化飞船"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 绘制飞船
        self.rect.midbottom = self.screen_rect.midbottom

        # 存储飞船坐标
        self.x = float(self.rect.x)

        # 飞船移动标记
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """更新飞船坐标和移动标记"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """在当前屏幕绘制飞船"""
        self.screen.blit(self.image, self.rect)


