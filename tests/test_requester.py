import pytest
from jabledl import Requester


def test_get_car_number():
    assert requester.get_car_number() == 'ipx-104-c'


def test_get_m3u8_url():
    assert requester.get_m3u8_url().endswith('.m3u8')


requester = Requester('https://jable.tv/videos/ipx-104-c/')
