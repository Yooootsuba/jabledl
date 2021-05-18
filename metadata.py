import re
import m3u8
import requests
from bs4 import BeautifulSoup
from jabledl.request import requests_headers


def get_car_number(url):
    '''
    A standard format of Jable TV url should look like : 'https://jable.tv/videos/CAR-NUMBER/'
    '''
    return url[len('https://jable.tv/videos/'):-1]


def get_m3u8_url(url):
    response = requests.get(url)
    soup     = BeautifulSoup(response.text, 'html.parser')
    soup     = soup.find('link', attrs = {'rel' : 'preload'})
    return soup.get('href')


def get_m3u8(url):
    return m3u8.load(url)


def get_segments(m3u8_obj, url):
    url = re.sub('([^\/]+).$', '', url)
    return [url + uri for uri in m3u8_obj.segments.uri]


def m3u8_is_encrypted(m3u8_obj):
    return False if m3u8_obj.keys[0] == None else True


def get_aes_key(m3u8_obj, url):
    url = re.sub('([^\/]+).$', m3u8_obj.keys[0].uri, url)
    return requests.get(url, headers = requests_headers).content.hex()


def get_aes_iv(m3u8_obj):
    return m3u8_obj.keys[0].iv[2:]
