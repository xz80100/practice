from selenium import webdriver
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import time

#設定webdriver及網址  F12可查找網頁的程式碼
driver = webdriver.Chrome('./chromedriver')
url = 'https://www.dcard.tw/f'
driver.get(url)

#在搜尋的輸入框內輸入文字
inputElement = driver.find_element_by_tag_name('input') #找到輸入框
inputElement.send_keys('python')  #輸入要搜尋的關鍵字

#點擊搜尋按鈕
driver.find_element_by_css_selector('button.sc-1ehu1w3-2').click() #找到符合要搜尋的元件名稱
time.sleep(2)  #休息2秒鐘

#擷取網站內容，並解析成html結構樹
html = driver.page_source
soup = bs(html, 'html.parser')

#獲得文章的看板、作者、時間
meta_datas = []
for x in soup.find_all('span', {'class': 'sc-6oxm01-2 hiTIMq'}):
    meta_datas.append(x.text.strip())
print(meta_datas)

#從meta_datas裡面挑出看板
forums = []
for i in range(len(meta_datas)):
    if i % 3 == 0:
        forums.append(meta_datas[i])

#獲得文章標題
titles = []
for x in soup.find_all('h2', {'class': 'sc-1v1d5rx-3 eih0FJ'}):
    titles.append(x.text)
print(titles)

#獲得文章連結
hrefs = []
for x in soup.find_all('a', {'classa': 'sc-1v1d5rx-4' 'gCVegi'}):
    hrefs.append(x['href'])

#從相對連結及url組成絕對連結
links = []
for href in hrefs:
    links.append(urljoin(url, href))
    print(links)

for i in range(len(forums)):
    print(forums[i], titles[i], links[i])