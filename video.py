import re
import m3u8
import requests
from bs4 import BeautifulSoup


class Video:

    def __init__(self, url):
        ''' Video infomations '''
        self.url               = url
        self.car_number        = None

        ''' M3U8 infomations '''
        self.m3u8              = None
        self.m3u8_url          = None
        self.segments          = None
        self.aes_iv            = None
        self.aes_key           = None
        self.m3u8_is_encrypted = None

        ''' HTML parser '''
        self.soup              = None


    def get_metadata(self):
        response  = requests.get(self.url)
        self.soup = BeautifulSoup(response.text, 'html.parser')

        self.get_car_number()
        self.get_m3u8_url()
        self.get_m3u8()
        self.get_segments()
        self.get_m3u8_is_encrypted()

        if self.m3u8_is_encrypted == True:
            self.get_aes_key()
            self.get_aes_iv()


    def get_car_number(self):
        self.car_number = self.soup.title.text.split(' ')[0].upper()


    def get_m3u8(self):
        self.m3u8 = m3u8.load(self.m3u8_url)


    def get_m3u8_url(self):
        self.m3u8_url = self.soup.find('link', attrs = {'rel' : 'preload'}).get('href')


    def get_segments(self):
        prefix = re.sub('([^\/]+).$', '', self.m3u8_url)
        self.segments = [prefix + uri for uri in self.m3u8.segments.uri]


    def get_m3u8_is_encrypted(self):
        self.m3u8_is_encrypted = False if self.m3u8.keys[0] == None else True


    def get_aes_key(self):
        headers = {'User-Agent' : 'Mozilla/5.0 \
                    (X11; Linux x86_64)        \
                    AppleWebKit/537.36         \
                    (KHTML, like Gecko)        \
                    Chrome/90.0.4430.212       \
                    Safari/537.36'             \
                  }
        url = re.sub('([^\/]+).$', self.m3u8.keys[0].uri, self.m3u8_url)
        self.aes_key = requests.get(url, headers = headers).content.hex()


    def get_aes_iv(self):
        self.aes_iv = self.m3u8.keys[0].iv[2:]
