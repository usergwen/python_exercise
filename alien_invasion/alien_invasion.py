#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/6/3 00:09
# @Author  : wen
# @File    : alien_invasion1.py
# @Software: PyCharm

import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """游戏资源管理"""

    def __init__(self):
        """初始化游戏资源"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """开始游戏循环"""
        while True:
            # 监控鼠标和键盘事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # 重绘屏幕
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # 最近屏幕可见
            pygame.display.flip()


if __name__ == '__main__':
    # 运行游戏
    ai = AlienInvasion()
    ai.run_game()



