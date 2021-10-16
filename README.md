# crawler_books
對博客來網站的暢銷榜進行資料爬取後存成csv，並讀取其書籍於網站的分類。

## crawler_book.py
爬取"博客來-中文書>暢銷榜"內容，取得其書名；作者；URL

**事前安裝套件**
```
pip install BeautifulSoup
pip install requests
```

**輸出**
`2019-12-01-博客來30日暢銷榜.csv`

## Add_RankingBookToClass.py
根據crawler_book.py所輸出csv檔案逐一取得其圖書分類，此範例只取主分類（Ex.文學小說>華文創作>散文，取得"文學小說"為分類）

**事前安裝套件**
```
pip install BeautifulSoup
pip install requests
pip install pandas
pip install time
```


**輸入**
`2019-12-01-博客來30日暢銷榜.csv`


**輸出**
`(新增分類)2019-12-01-博客來30日暢銷榜.csv`
