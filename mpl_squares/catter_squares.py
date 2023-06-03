#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/6/3 09:48
# @Author  : wen
# @File    : catter_squares.py
# @Software: PyCharm

import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=200)

ax.set_title("square number", fontsize=16)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("square of value", fontsize=14)

ax.tick_params(axis="both", which="major", labelsize=14)

plt.show()
plt.savefig("images/squares_plot.png", bbox_inches="tight")