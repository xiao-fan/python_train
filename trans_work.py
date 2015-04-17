list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
max_two,max_one = sorted(list)[len(list)-2:len(list)]

print "最大数字是%s,第二大数字是%s!"%(max_one,max_two)
