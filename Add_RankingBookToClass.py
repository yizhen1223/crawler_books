#!/usr/bin/env python
# coding: utf-8
import requests
import csv
import os
import sys
import requests
import random
import pandas as pd
from bs4 import BeautifulSoup
from datetime import time, datetime, date, timedelta
from time import sleep
import urllib


# 直接進入書籍頁面找出分類
def getClassification(bookurl):
    try:
        book_class_li = []
        class_list = []
        html = requests.get(bookurl,headers=headers)
        html.encoding='utf-8' #使用utf-8方式編碼讀取網頁
        #使用BeautifulSoup解析原始碼
        sp=BeautifulSoup(html.text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding), 'html.parser')
        book_class_li = sp.select('span[itemprop="title"]')
        print("分類長度為 %s " % len(book_class_li))
        # 博客來>中文書>......>商品介紹，至少有3項是不被包留
        if len(book_class_li) > 2 :
            # 將書籍分類取出成List
            for i in book_class_li:
                class_list.append(i.text)
            # 從索引值2開始包留至倒數第二個值，只保留"博客來>中文書>......>商品介紹"中間的分類
            class_list = class_list[2:]
            class_list.pop(-1)
            print(class_list)
            if len(class_list) > 0 :
                class1.append(class_list[0])
        else:
            class1.append("找無分類")

    except:
        class1.append("請重新讀取")
    finally:
        book_class_li = []
        class_list = []



# 直接進入書籍頁面找出分類
def getOneClassification(bookurl):
    try:
        book_class_li = []
        class_list = []
        html = requests.get(bookurl,headers=headers)
        html.encoding='utf-8' #使用utf-8方式編碼讀取網頁
        #使用BeautifulSoup解析原始碼
        sp=BeautifulSoup(html.text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding), 'html.parser')
        book_class_li = sp.select('span[itemprop="title"]')
        print("分類長度為 %s " % len(book_class_li))
        # 博客來>中文書>......>商品介紹，至少有3項是不被包留
        if len(book_class_li) > 2 :
            # 將書籍分類取出成List
            for i in book_class_li:
                class_list.append(i.text)
            # 從索引值2開始包留至倒數第二個值，只保留"博客來>中文書>......>商品介紹"中間的分類
            class_list = class_list[2:]
            class_list.pop(-1)
            print(class_list)
            class1.append(class_list[0])
        else:
            class1.append("找無分類")
    except:
        class1.append("請重新讀取")
    finally:
        book_class_li = []
        class_list = []



# 僅以書名去搜尋，以第一筆當作結果進去連結找分類
def getResult(keyword):
    try:
        url = 'https://search.books.com.tw/search/query/key/'+keyword+'/cat/all'
        html = requests.get(url,headers=headers)
        html.encoding='utf-8' #使用utf-8方式編碼讀取網頁
        #使用BeautifulSoup解析原始碼
        sp=BeautifulSoup(html.text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding), 'html.parser')
        # 搜尋筆數不為0再繼續
        count = sp.select('span')[1].text
        print('筆數: %s' % count)
        count = int(count)
    except :
        count = 0
    finally:
        if int(count) > 0:
            # 取得第一個結果的連結
            link = sp.select('.searchbook')[0].select('.item')[0].select('h3 a')[0].get('href')
            intact_link = 'https:'+link
            print(intact_link)
            getClassification(intact_link)
        else :
            class1.append("未分類")





def starLoadFile(filename) :
    df_rank = pd.read_csv(filename, encoding='utf-8')
    for a in df_rank['連結']:
        getOneClassification(a)
        random_sec = random.randint(30,120)
        print("等待秒數: %s 秒" % random_sec)
        sleep(random_sec)


if__name__ == '__main__':

    #自訂網頁表頭，讓電腦模擬瀏覽器操作網頁
    # headers={'user-agent':'Mozilla/5.0'}
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
    fileLink = "2021-09-17-博客來30日暢銷榜.csv"

    class1=[]
    starLoadFile(fileLink)


    df = pd.read_csv(fileLink, encoding='utf-8')
    df['分類']=class1



    # 另存成新的csv，並去除索引值
    new_fileName = "(新增分類)"+fileLink
    df.to_csv(new_fileName, index=False)





