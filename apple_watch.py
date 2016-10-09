
#coding=utf-8
import requests as r
import json
import time
from send_sms import sendsms
cishu = 0
cishu_flag = False
url='https://reserve.cdn-apple.com/CN/zh_CN/reserve/iPhone/availability.json'
def available_txt(urls):
    t = r.get(urls)
    return t.content.decode('utf-8')

def cq_data(at):
    at_tree = json.loads(at)
    return {"解放碑":at_tree["R480"],"万象城":at_tree["R573"],"北城天街":at_tree["R476"],}

def cq_7plus_128g_black(cq_data_tree):
    #result = {'解放碑':cq_data_tree["解放碑"]["MNFP2CH/A"],
    #          '解放碑':cq_data_tree["解放碑"]["MNFP2CH/A"],
    #}
    result = {}
    for i in cq_data_tree:
        result[i]=cq_data_tree[i]["MNFP2CH/A"]
    return result

def detect_apple(content):
    return len(content)

def cishu_duanxin(time_wait):
    global cishu
    
    cishu+=time_wait
    if cishu > (3600*3-1):
        cishu = 0
    if cishu == 300:   
        return True
    return False
def main():
    global cishu_flag
    #f=open('temp.txt','w')
    ats = available_txt(url)
    exists_flag = 0
    rstr=''
    if detect_apple(ats) > 10:
        print 'data available'
        cq_tr=cq_data(ats)
        cq_7p_b = cq_7plus_128g_black(cq_tr)
        for i in cq_7p_b:
            rstr+=cq_7p_b[i]
        if 'all' in rstr:
            print 'GO TO BUY!'
            sendsms(cq_7p_b["解放碑"].encode('utf-8'),cq_7p_b["万象城"].encode('utf-8'),cq_7p_b["北城天街"].encode('utf-8'))
            return 3600
        else:
            print '无存量'
            if cishu_flag:
               sendsms(cq_7p_b["解放碑"].encode('utf-8'),cq_7p_b["万象城"].encode('utf-8'),cq_7p_b["北城天街"].encode('utf-8')) 
            return 300
    else:
        if cishu_flag:
            sendsms('无数据','无数据','无数据')
        print 'data unavailable'
        return 300
    #print cq_7p_b[3]
    #f.write(ats)
    #f.close()    
if __name__ == '__main__':
    time_wait = 10
    #sendsms('开始','开始','开始')
    while True:
        time_wait=main()
        cishu_flag=cishu_duanxin(time_wait)
        time.sleep(time_wait)
