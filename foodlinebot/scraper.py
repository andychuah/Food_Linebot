from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
import requests
from urllib.request import urlretrieve
 
 
# 美食抽象類別
class Food(ABC):
 
    def __init__(self, area):
        self.area = area  # 地區
 
    @abstractmethod
    def scrape(self):
        pass

# 愛食記爬蟲
class IFoodie(Food):
 
    def scrape(self):
        response = requests.get("https://ifoodie.tw/explore/" + self.area + "/list/?sortby=popular/" )

        soup = BeautifulSoup(response.content, "html.parser")

         # 爬取前五筆餐廳卡片資料
        cards = soup.find_all(
            'div', {'class': 'jsx-4282820896 restaurant-info'}, limit=5)
 
        content = ""
        for card in cards:
 
            title = card.find(  # 餐廳名稱
                "a", {"class": "jsx-4282820896 title-text"}).getText()
 
            stars = card.find(  # 餐廳評價
                "div", {"class": "jsx-1207467136 text"}).getText()
 
            address = card.find(  # 餐廳地址
                "div", {"class": "jsx-4282820896 address-row"}).getText()
 
 
            #將取得的餐廳名稱、評價及地址連結一起，並且指派給content變數
            content += f"{title} \n{stars}顆星 \n{address} \n\n"
 
        return content

class yahooMovie:

    def scrape():
        '''
        response = requests.get("https://movies.yahoo.com.tw/" )

        soup = BeautifulSoup(response.content, "html.parser")

         # 爬取前十筆即將上映電影資料
        cards = soup.find_all(
            'div', {'class': 'movielist-info'}, limit=10)
 
        content = ""
        for card in cards:
 
            title = card.find(  # 電影名稱
                "a", {"class": "gabtn text_truncate_1"}).getText()
 
            date = card.find(  # 上映日期
                "div h3").getText()
 
            percent = card.find(  # 期待度
                "div span", {"class": "percent"}).getText()
 
            #將取得的餐廳名稱、評價及地址連結一起，並且指派給content變數
            content += f"電影：{title} \n上映日期：{date} \n期待度：{percent} \n\n"
 
        return content

        target_url = 'https://movies.yahoo.com.tw/'
        rs = requests.session()
        res = rs.get(target_url, verify=False)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')   
        content = ""
        for index, data in enumerate(soup.select('div.movielist_info h1 a')):
            if index == 20:
                return content       
            title = data.text
            link =  data['href']
            content += '{}\n{}\n'.format(title, link)
        return content
        '''


