# !/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import argparse
import signal




def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f",'--follow', help="持续输出",action='store_true')
    parser.add_argument('path', help="日志文件路径")
    args = parser.parse_args()
    follow = args.follow
    path = args.path

    return follow,path

# 退出
def os_quit(signum, frame):
    os._exit(0)

# 一次性全部输出
def follow_file_no(file_path):
    try:
        with open(file_path,'r',encoding='UTF-8') as f:
            for i in f.readlines():
                print(str(i).strip())

    # 出现文件临时被占用情况休眠 0.1 秒
    except:
        time.sleep(0.1)
        follow_file(file_path)



# 持续输出
def follow_file(file_path):
    try:
        with open(file_path,'r',encoding='UTF-8') as f:
            signal.signal(signal.SIGINT, os_quit)                                
            signal.signal(signal.SIGTERM, os_quit)
            while True:
                for i in f.readlines():
                    print(str(i).strip())
    
    # 出现文件临时被占用情况休眠 0.1 秒
    except :
        signal.signal(signal.SIGINT, os_quit)                                
        signal.signal(signal.SIGTERM, os_quit)
        time.sleep(0.1)
        follow_file(file_path)

if __name__ == "__main__":
    follow,path = parse_args()
    file_path = path
    if file_path:
        if follow:
            follow_file(file_path)
        else:
            follow_file_no(file_path)
