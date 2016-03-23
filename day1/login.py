#!/usr/bin/env python
#-*- coding:utf-8 -*-


file_obj = file('/root/python_train/day1/user_passwd.txt','r+')
line_list = file_obj.readlines()

input_times = 0
while input_times < 3:
    name = raw_input("please input your name>>>")
    tmp_list = []
    input_times += 1
    for line in  line_list:
        line_one = line.strip()#.split(';')
        ele_list = line_one.split(';')
        if ele_list[0]  != name:
            str_ele=';'.join(ele_list)
            tmp_list.append(str_ele)
        else:
            ele_list[2] = str(input_times)
            str_ele=';'.join(ele_list)
            tmp_list.append(str_ele)
            print "haha! you are right!"
    for i in tmp_list:
        file_obj.write(i)


file_obj.close()
