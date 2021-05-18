import pytest
import requests
import responses
from jabledl import downloader


def callback():
    pass


@responses.activate
def test_download():
    download = downloader.Downloader(['http://example.com'] * 200, {}, callback)
    responses.add(responses.GET, 'http://example.com', status = 200)
    download.download()
