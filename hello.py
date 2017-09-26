#!/usr/bin/env  python
# -*- coding: utf-8 -*-

import sys

print "hello"
print "你好，世界"

#！系统参数
print sys.argv

#！变量
name = "hvlic"
#！name和name2是在内存中的数据相同，地址相同
#！难道是引用方式传值
name2 = name

#！用户输入
name = raw_input("请输入用户名：")
print name


#！getpass 模块
import getpass
pwd = getpass.getpass("请输入密码：")
print pwd






