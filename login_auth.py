#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getpass

name = raw_input("�������û�����")
pwd = getpass.getpass('���������룺')

if name == "alex" and pwd == "cmd":
    print "��ӭalex!"
else:
    print "�û��������������"
	
if name == "alex":
    print name + "�ǳ�������Ա"
#else if error
#else if name == "eric":
elif name == "eric":
    print name + "����ͨ����Ա"
elif name == "tony":
	print name + "��ҵ������"
else:
	print name + "����ͨ�û�"