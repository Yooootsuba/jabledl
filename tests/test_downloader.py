import pytest
import requests
import responses
from jabledl import Downloader


@responses.activate
def test_download():
    responses.add(responses.GET, 'http://example.com', status = 200)
    downloader.download()


downloader = Downloader(['http://example.com'] * 200, {})
