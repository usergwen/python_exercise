#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/6/3 00:25
# @Author  : wen
# @File    : ship.py
# @Software: PyCharm

import pygame

import pygame


class Ship:
    """飞船管理"""

    def __init__(self, ai_game):
        """初始化飞船"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 绘制飞船
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """在当前屏幕绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
