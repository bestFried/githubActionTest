import requests # requests 요청해서 텍스트 갖고오는 라이브러리
from bs4 import BeautifulSoup  # BeautifulSoup 갖고온 텍스트를 깔끔하게 가공해주는 라이브러리

url = 'https://ridibooks.com/category/new-releases/2200'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser') #xml파서 등도 있음

print('test test ')

bookservices = soup.select('.fig-rs5q24')
for no, book in enumerate(bookservices, 1):  #순회돌면서 넘버링해서 출력
    print(no, book.text.strip()) #strip은 trim
