import time
import jabledl
from tqdm import trange
from datetime import datetime


jabledl.parse_args()


print('\n')
print('[INFO] ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print('[INFO] Collecting video informations ...')


for i in trange(100, desc = '[INFO] Downloading ...'):
    time.sleep(0.01)


print('[INFO] Decrypting AES from M3U8 segments ...')
print('[INFO] Merging M3U8 segments ...')
print('[INFO] Converting MPEG-2 to MP4 ...')
print('[INFO] Removing M3U8 segments ...')
print('[INFO] ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
