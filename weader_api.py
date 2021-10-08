import requests
from bs4 import BeautifulSoup


def getTempature():

    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=날씨"
    response =requests.get(url) #not json 

    naver_html = response.text #페이자를 통째로 받음 
    soup = BeautifulSoup(naver_html,'html_parser')

    temp = soup.select_one(".tdtemp")
    return temp
