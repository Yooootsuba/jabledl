import pytest
import requests
from jabledl import metadata


def test_get_car_number():
    assert metadata.get_car_number('https://jable.tv/videos/ipx-104-c/') == 'ipx-104-c'


def test_get_m3u8_url():
    assert metadata.get_m3u8_url('https://jable.tv/videos/ipx-104-c/').endswith('.m3u8')


def test_get_m3u8():
    m3u8_url = metadata.get_m3u8_url('https://jable.tv/videos/ipx-104-c/')
    m3u8_obj = metadata.get_m3u8(m3u8_url)
    assert m3u8_obj


def test_get_segments():
    m3u8_url = metadata.get_m3u8_url('https://jable.tv/videos/ipx-104-c/')
    m3u8_obj = metadata.get_m3u8(m3u8_url)
    segments = metadata.get_segments(m3u8_obj, m3u8_url)
    assert m3u8_obj


def test_m3u8_is_encrypted():
    m3u8_url = metadata.get_m3u8_url('https://jable.tv/videos/ipx-104-c/')
    m3u8_obj = metadata.get_m3u8(m3u8_url)
    assert metadata.m3u8_is_encrypted(m3u8_obj) == False

    m3u8_url = metadata.get_m3u8_url('https://jable.tv/videos/ssis-070/')
    m3u8_obj = metadata.get_m3u8(m3u8_url)
    assert metadata.m3u8_is_encrypted(m3u8_obj) == True


def test_get_aes_key():
    m3u8_url = metadata.get_m3u8_url('https://jable.tv/videos/ssis-070/')
    m3u8_obj = metadata.get_m3u8(m3u8_url)
    assert len(metadata.get_aes_key(m3u8_obj, m3u8_url)) == 32


def test_get_aes_iv():
    m3u8_url = metadata.get_m3u8_url('https://jable.tv/videos/ssis-070/')
    m3u8_obj = metadata.get_m3u8(m3u8_url)
    assert len(metadata.get_aes_iv(m3u8_obj)) == 32
