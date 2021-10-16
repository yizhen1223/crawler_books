#!/usr/bin/env python
# coding: utf-8
import csv
import os
import sys
import requests
from bs4 import BeautifulSoup
from datetime import time, datetime, date, timedelta
# 擷取榜單日期
date = datetime.now() - timedelta(days=30)
dateStr = date.strftime("%Y-%m-%d").lstrip('0')
print(dateStr)

# 博客來30日暢銷榜-總榜
url_total = 'https://www.books.com.tw/web/sys_saletopb/books/?attribute=30&loc=P_0002_001'
# 博客來30日暢銷榜-文學小說開始各分類
url_kind = 'https://www.books.com.tw/web/sys_saletopb/books/01/?attribute=30&loc=P_0002_002'

#使用get方式向網頁發送請求
html=requests.get(url_total)
#使用utf-8方式編碼讀取網頁
html.encoding='utf-8'

#自訂網頁表頭，讓電腦模擬瀏覽器操作網頁
headers={'user-agent':'Mozilla/5.0'}



#使用BeautifulSoup解析原始碼
sp=BeautifulSoup(html.text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding), 'html.parser')

#取得分類名
all_kind = sp.select('.mod_b')[0].select('li')
kind_tag=[]
for k in all_kind:
    kind_tag.append(k.select('a')[0].text)

    
#讀取網頁內容，找到博客來即時榜的位置範圍
ranking=[]
book_name=[]
author=[]
bookurl=[]
m=sp.select('.mod_a')[0].select('.item')
for i in m:
    #讀取榜單排名
    print("%s"%i.find_all('strong')[0].text,end=' ')
    #讀取書名
    bookStr = i.find_all('h4')[0].text
    print(bookStr,end=' ')
    #讀取作者名
    print(i.select('.msg li a')[0].text)
    #url of book
    book_buy_url = i.select('h4 a')[0].get('href')
    print(book_buy_url)
    #add to list
    ranking.append("%s"%i.find_all('strong')[0].text)
    book_name.append(bookStr)
    author.append(i.select('.msg li a')[0].text)
    bookurl.append(book_buy_url)
# print(len(ranking))
# print(len(book_name))
# print(len(author))




# 輸入至CSV檔案
totalLength = len(ranking) #各列表長度
with open(dateStr+'-博客來30日暢銷榜.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['排名', '書籍名稱', '作者','連結'])
    for w in range(totalLength):
        csvwriter.writerow([ranking[w], book_name[w], author[w], bookurl[w]])






