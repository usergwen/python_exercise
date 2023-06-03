#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/6/3 09:15
# @Author  : wen
# @File    : bullet.py
# @Software: PyCharm
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """子弹管理"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed

        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
