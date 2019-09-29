import requests
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html,'lxml')
    trs = soup.find_all('tr')
    for tr in trs:
        name=tr.find('td', attrs={'class':'curAmount'})
        print(name)
 


def main():
    url ="http://www.nbrb.by/statistics/rates/ratesdaily.asp"
    print(get_data(get_html(url)))
        
        
        



if __name__ =='__main__':
    main()

input()

