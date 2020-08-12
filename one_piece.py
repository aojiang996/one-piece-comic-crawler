# coding=utf-8
'''
Created on 2020-4-2
@author: jiangao
Project: one piece 漫画爬取
'''
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import re
import csv
import sys
import io
import time
  

headers = {
    'Content-Type': 'text/plain; charset=UTF-8',
    'Origin':'https://maoyan.com',
    'Referer':'https://maoyan.com/board/4',
    'User-Agent':'Chrome/80.0.3396.99 Safari/537.36'
    }
  
#爬取网页源代码
def get_one_page(url,headers):
    try:
        response =requests.get(url,headers=headers)
        if response.status_code == 200:
            response.encoding = "utf-8"
            print("worked")
            return response.text
        else:
            print("none")
            print(response.status_code)
            return None
    except RequestException:
        print("none2")
        print(response.status_code)
        return None

#提取正则表达式
def parse_one_page(html):
    pattern = re.compile('<img class="" src="(.*?)" alt="')
    p = re.findall(pattern,html)
    return p

def parse_image_page(html):
    pattern = re.compile('http://mhua.zerobyw4.com/manhua/.*?/.*?/(.*)')
    p = re.findall(pattern,html)
    return p

#下载海报
def save_image_file(url,path):
    jd = requests.get(url)
    if jd.status_code == 200:
        with open(path,'wb') as e:
            e.write(jd.content)
            e.close()

def main(k):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8') #改变标准输出的默认编码
    chrome_driver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'  #chromedriver的文件位置
    b = webdriver.Chrome(executable_path = chrome_driver)
    f = open('C:/Users/Desktop/all.txt','r')
    html = f.readlines()
    f.close()
    files = 'D:/one/'

    b.get(html[k-1])
    time.sleep(2)
    #输入账号
    username = b.find_element_by_name('username')
    username.send_keys('username')
    #输入密码
    password = b.find_element_by_name('password')
    password.send_keys('password')
    #点击登录
    login_button = b.find_element_by_class_name('vm')
    login_button.submit()

    p = parse_one_page(b.page_source.encode('utf-8').decode())

    one = p[0]
    strinfo = re.compile('002')
    one = strinfo.sub('001',one)
    p.reverse()#反向列表元素
    p.append(one)
    p.reverse()
    for j in p:
        num = parse_image_page(j)
        path = files+str(k)+'/'+ num[0]
        save_image_file(j,path)
    k += 1
    b.quit()



if __name__ == '__main__':
    url = 'http://mhua.zerobyw4.com/manhua/O9NI9EC6E/94/001.jpg'
    print(get_one_page(url,headers))