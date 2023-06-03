#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/6/3 09:23
# @Author  : wen
# @File    : game_status.py
# @Software: PyCharm

class GameStatus:
    """状态管理"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = True

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
