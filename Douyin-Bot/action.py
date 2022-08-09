# import os
# import re
import random


import time
from common.auto_adb import auto_adb
from common import  config
adb = auto_adb()
config = config.open_accordant_config()
#
# os.system('adb version')
# os.system('adb devices') #os.system是不支持读取操作的
# out = os.popen('adb shell "dumpsys activity | grep "mFocusedActivity""').read() #os.popen支持读取操作
# print('out:',out)
#
# #下面的代码是获取当前窗口的component参数
# #i is 设备号
# def getFocusedPackageAndActivity(i):
#         pattern = re.compile(r".*\n(.*)\t.*")
#         out = os.popen("adb devices").read()
#         list = pattern.findall(out)
#         #print(list)
#         component = str('-s ')+list[i-1] #输出列表中的第一条字符串
#
#         return component
# #abd {}  *******************.format(getFocusedPackageAndActivity())
# print(getFocusedPackageAndActivity(1))
# print(os.popen("adb devices").read())


#全局使用
count = 0
class action():
    #动作基

    def clicked(self):
        """
        点击
        """
        cmd = 'shell input tap {x} {y}'.format(
            x=config[self]['x'], y=config[self]['y']
        )

        adb.run(cmd)
        print ('成功点击目标')
        time.sleep(2.5)


    def move(self):
        """
            滑动
        """
        cmd = 'shell input swipe {x1} {y1} {x2} {y2} '.format(
            x1=config[self]['x'],
            y1=config[self]['y'],
            x2=config[self]['x1'],
            y2=config[self]['y1'],
        )

        adb.run(cmd)
        print ('成功划过天边')
        time.sleep(3)

    def read_txt(self):
        file = self
        with open (file, 'r', encoding='UTF-8') as f:
            line = f.readlines ()
            return random.sample (line, 1) [0]
        
    def input(self):
        """
        输入文本
        """

        cmd = 'shell am broadcast -a ADB_INPUT_TEXT --es msg {s}'.format(
            s=action.read_txt(self)
        )

        adb.run (cmd)
        print('成功输入文本')
        time.sleep (3)

    def clicked_n(self, num, n, xory):
        """
        点击
        """
        global count

        n=n
        cmd = 'shell input tap {x} {y}'.format(
            x=config[self]['x'], y=config[self]['y']
        )

        adb.run(cmd)
        print(
            '*' * 20,
            "\n成功点击目标x:{0},y:{1}\n下移次数为{2}\n".format(
                config[self]['x'], config[self]['y'], count
            ),
            '*' * 20,
        )

        config[self][xory] += n
        count+=1
        if count>=num:
            config[self][xory] -= n*num
            count=0

        time.sleep(1.5)
