import requests # requests 요청해서 텍스트 갖고오는 라이브러리
from bs4 import BeautifulSoup # BeautifulSoup 갖고온 텍스트를 깔끔하게 가공해주는 라이브러리

url = 'https://ridibooks.com/category/new-realeases/2200'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser') #html파서, xml파서 등도 있음.

bookservices = soup.select('.title_text') #특정 클래스 텍스트 짚어내는 코드
for no, book in enumerate(bookservices, 1): #순회돌면서 넘버링해서 출력해주겠다
  print(no, book.text.strip()) #strip은 trim
