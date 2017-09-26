#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getpass

name = raw_input("请输入用户名：")
pwd = getpass.getpass('请输入密码：')

if name == "alex" and pwd == "cmd":
    print "欢迎alex!"
else:
    print "用户名或者密码错误！"
	
if name == "alex":
    print name + "是超级管理员"
#else if error
#else if name == "eric":
elif name == "eric":
    print name + "是普通管理员"
elif name == "tony":
	print name + "是业务主管"
else:
	print name + "是普通用户"