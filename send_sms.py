#coding=utf-8
import requests as r
import urllib

def sendsms(j,w,b):
    u='http://utf8.sms.webchinese.cn/?Uid=aniu&Key=&smsMob=&smsText='#key and mobile phone number has been deleted
    text='7+黑色版预约存量： 解放碑：%s、 万象城：%s、 北城天街：%s'
    text = text%(j,w,b)
    text = urllib.quote(text)
    u = u+text
    x=r.get(u)
    if x.content == '1':
        print 'sms success'
    else:
        print 'sms failed'
