from .video      import Video
from .cmdline    import parse_args
from .downloader import Downloader
from .segments   import Segments


import sys
from tqdm import tqdm
from datetime import datetime


requests_headers = {'User-Agent' : 'Mozilla/5.0          \
                                    (X11; Linux x86_64)  \
                                    AppleWebKit/537.36   \
                                    (KHTML, like Gecko)  \
                                    Chrome/90.0.4430.212 \
                                    Safari/537.36'       \
                   }


def main():

    def requests_callback():
        bar.update(1)


    url = parse_args()


    print('\n')
    print('[INFO] ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


    print('[INFO] Collecting video informations ...')
    video = Video(url)
    video.get_metadata()


    bar = tqdm(total = len(video.segments), desc = '[INFO] Downloading ...', file = sys.stdout)
    downloader = Downloader(video.segments, requests_headers, requests_callback)
    downloader.download()
    bar.close()


    segments = Segments(len(video.segments))
    print('[INFO] Decrypting AES from M3U8 segments ...')
    segments.decrypt(video.aes_key, video.aes_iv)


    print('[INFO] Merging M3U8 segments ...')
    segments.merge()


    print('[INFO] Converting MPEG-2 to MP4 ...')
    segments.convert(video.car_number + '.mp4')

    print('[INFO] Removing M3U8 segments ...')
    segments.clean()


    print('[INFO] ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
