import pytest
from jabledl import Video


def test_video():
    assert video.car_number == 'SSIS-070'
    assert video.m3u8
    assert video.m3u8_url.endswith('.m3u8')
    assert video.segments
    assert video.m3u8_is_encrypted == True
    assert len(video.aes_key) == 32
    assert len(video.aes_iv)  == 32


video = Video('https://jable.tv/videos/ssis-070/')
video.get_metadata()
