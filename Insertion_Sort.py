# -*- coding: utf-8 -*-


Insert_List = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]   #插入算法:循环遍历,将最小的放到左边,剩余的继续遍历
#Insert_List = [0,1,2,3,4]
#Insert_List = [4,3,2,1,0]
sorted_list = []

print '原始列表内容是:%s' % Insert_List
print '实际排序应该是:%s' % sorted(Insert_List)

for i in range(len(Insert_List)):
    min = Insert_List[i]
    for j in range(i+1,len(Insert_List)):
        if Insert_List[j] < min:
            min = Insert_List[j]
            Insert_List[i],Insert_List[j] = Insert_List[j],Insert_List[i]
    sorted_list.append(min)

print '我的脚本结果是:\033[1;31;40m%s\033[0m' % sorted_list    #输出插入算法的结果  


#程序有bug,比如最小的之后 将换一下位置
