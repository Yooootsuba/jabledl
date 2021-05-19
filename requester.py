import requests
from bs4 import BeautifulSoup


class Requester:

    def __init__(self, url):
        self.url = url


    def get_car_number(self):
        '''
        A standard format of Jable video url should look like : 'https://jable.tv/videos/CAR-NUMBER/'
        '''
        return self.url[len('https://jable.tv/videos/'):-1]


    def get_m3u8_url(self):
        response = requests.get(self.url)
        soup     = BeautifulSoup(response.text, 'html.parser')
        soup     = soup.find('link', attrs = {'rel' : 'preload'})
        return soup.get('href')
