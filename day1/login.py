#!/usr/bin/env python
#-*- coding:utf-8 -*-


file_obj = file('/root/python_train/day1/user_passwd.txt','r+')
line_list = file_obj.readlines()

input_times = 0
while input_times < 3:
    name = raw_input("please input your name>>>")
    input_times += 1
    for line in  line_list:
        line_one = line.strip().split(';')
        if line_one[0] == name:
            print "haha! you are right!"
            break


file_obj.close()
