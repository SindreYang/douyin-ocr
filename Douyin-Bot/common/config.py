# -*- coding: utf-8 -*-
"""
调取配置文件和屏幕分辨率的代码
"""
import os
import sys
import json
import re

from common.auto_adb import auto_adb

adb = auto_adb()


def open_accordant_config():
    """
    调用配置文件
    """
    screen_size = _get_screen_size()
    config_file = "{path}/config/{screen_size}/config.json".format(
        path=sys.path[0],
        screen_size=screen_size
    )

    # 优先获取执行文件目录的配置文件
    here = sys.path[0]
    for file in os.listdir(here):
        if re.match(r'(.+)\.json', file):
            file_name = os.path.join(here, file)
            with open(file_name, 'r') as f:
                print(f"Load config file from {file_name}")
                return json.load(f)

    # 根据分辨率查找配置文件
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            print(f"正在从 {config_file} 加载配置文件")
            return json.load(f)
    else:
        with open(f'{sys.path[0]}/config/default.json', 'r') as f:
            print("Load default config")
            return json.load(f)


def _get_screen_size():
    """
    获取手机屏幕大小
    """
    size_str = adb.get_screen()
    if m := re.search(r'(\d+)x(\d+)', size_str):
        return "{height}x{width}".format(height=m[2], width=m[1])
    return "1920x1080"
