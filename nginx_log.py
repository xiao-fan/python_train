# -*- coding: utf-8 -*-

d = {}
with open('access.log') as f:
    try:
        for ip_http_url in f.readlines():  #line is list
            ip = ip_http_url.split(' ')[0]
            url = ip_http_url.split(' ')[6]
            http = ip_http_url.split(' ')[8]
            t = http,url,ip        #change line tulpe
            if t in d:
                d[t] = d[t] + 1 
            else:
                d[t] = 1 
    except IndexError:
        print '\033[1;31;40mindex error\033[0m'

l = []
for k,v in d.items():
    k_http =  k[0]
    k_url = k[1]
    k_ip_times = (k[2],v)
    if len(l) == 0:    
        l.append(list((k_http,k_url,k_ip_times)))
        continue
    elif len(l) == 11: 
        l.pop()
    for num in l:
        if v > num[2][1]:
            l.insert(l.index(num),list((k_http,k_url,k_ip_times)))
            break
for i in  l:  
    print i
