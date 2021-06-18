# Food_Linebot

This is a project using line-bot-sdk and scrape the information from website.

Before running the project:
1. Create an account on LINE : https://account.line.biz/login?redirectUri=https%3A%2F%2Fdevelopers.line.biz%2Fconsole%2Fchannel%2F1656105440%2Fmessaging-api
and fill in the information in Messanging API.
2. Install these:
    $ pip install django
    $ pip install line-bot-sdk
    $ pip install beautifulsoup4
    $ pip install requests
3. Create django
    $ django-admin startproject mylinebot .  #建立Django專案
    $ python manage.py startapp foodlinebot  #建立Django應用程式
    $ python manage.py migrate  #執行資料遷移(Migration)
4. Install ngrok:https://ngrok.com/
    And run
    $ngrok http 8000
5. You need to change:
   (i) Line secret key
   (ii) Line access token
   (iii) Ngrok webhook url
6. $python manage.py runserver #Connect to line server with your terminal
   

