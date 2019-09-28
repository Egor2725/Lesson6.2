import requests
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html,'lxml')
    hs = soup.find_all('h2', attrs={'class':'post__title'})
    for h in hs:
        title = h.find('a', attrs={'class':'post__title_link'}).text
        print(title)
 


def main():
    n=1
    for n in range(50):
        
        url = ("https://habr.com/ru/all/page"+str(n))
        print(get_data(get_html(url)))
        n=int(n)+1
        
        
        



if __name__ =='__main__':
    main()

input()

