# coding=utf-8
'''
Created on 2020-4-2
@author: jiangao
Project: one piece 漫画爬取
'''
import requests
import threading
import sys
import io
import time
import os
import re
import socket


header = {
    'Content-Type': 'text/plain; charset=UTF-8',
    'User-Agent':'Chrome/80.0.3396.99 Safari/537.36'
    }
#下载海报
def save_image_file(url,path):
    jd = requests.get(url,headers = header)
    time.sleep(2)
    socket.setdefaulttimeout(20)
    if jd.status_code == 200:
        print('work')
        time.sleep(1)
        with open(path,'wb') as e:
            e.write(jd.content)
            e.close()
        return 0
    else:
        return 1

def save(op,ed):
    a = 'http://mhua.zerobyw4.com/manhua/ON9EP9IE6CE/'
    c = '.jpg'
    for j in range(op,op+1):
        path = 'D:/one/' + str(j) +'/'
        for i in range(ed+1,250):
            if i<10:
                print("第"+str(i)+"张"+"   "+"("+"第"+str(j)+"卷"+")")
                h = a + str(j) + '/' + '00' + str(i) +c
                b = save_image_file(h,path + '00' + str(i) +c)
                if b == 1:
                    break
            elif i>=10 and i<100:
                print("第"+str(i)+"张"+"   "+"("+"第"+str(j)+"卷"+")")
                h = a + str(j) + '/' + '0' + str(i) +c
                b = save_image_file(h,path + '0' + str(i) +c)
                if b == 1:
                    break
            else:
                print("第"+str(i)+"张"+"   "+"("+"第"+str(j)+"卷"+")")
                h = a + str(j) + '/'  + str(i) +c
                b = save_image_file(h,path  + str(i) +c)
                if b == 1:
                    break

   
def save1():
    listos = os.listdir('D:\\one')
    for i in range(94,95):
        listoss = os.listdir('D:\\one\\'+str(i))
        j = listoss[-1:]
        strinfo = re.compile('.jpg')
        one = strinfo.sub('',j[0])
        save(int(i),int(one))


    
if __name__ == '__main__':
    url = 'http://mhua.zerobyw4.com/manhua/O9NI9EC6E/94/001.jpg'
    path = 'D:\\one\\94\\001.jpg'
    save_image_file(url,path)
    