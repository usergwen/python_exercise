#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/6/3 10:00
# @Author  : wen
# @File    : pythonrepos.py
# @Software: PyCharm

import requests


import requests

cookies = {
    '_octo': 'GH1.1.103331299.1680345770',
    'logged_in': 'yes',
    'dotcom_user': 'usergwen',
    'color_mode': '%7B%22color_mode%22%3A%22light%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light_colorblind%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark_dimmed%22%2C%22color_mode%22%3A%22dark%22%7D%7D',
    'preferred_color_mode': 'light',
    'tz': 'Asia%2FShanghai',
    'fileTreeExpanded': 'true',
}

headers = {
    'authority': 'api.github.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'cache-control': 'no-cache',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_octo=GH1.1.103331299.1680345770; logged_in=yes; dotcom_user=usergwen; color_mode=%7B%22color_mode%22%3A%22light%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light_colorblind%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark_dimmed%22%2C%22color_mode%22%3A%22dark%22%7D%7D; preferred_color_mode=light; tz=Asia%2FShanghai; fileTreeExpanded=true',
    'dnt': '1',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}

res = requests.get('https://api.github.com/search/repositories?q=language:python&sort=stars', cookies=cookies, headers=headers)
print(f"Status code: {res.status_code}")
res_dict = res.json()
print(res_dict.keys())
