import os
from tqdm import tqdm
from Crypto.Cipher import AES


class Segments:

    def __init__(self, size, filename):
        self.size = size


    def decrypt(self, key, iv):
        if key == None and iv == None : return
        aes = AES.new(bytes.fromhex(key), AES.MODE_CBC, bytes.fromhex(iv))
        for i in range(self.size):
            with open('%d.ts' % i, 'rb+') as f:
                plain = aes.decrypt(f.read())
                f.seek(0)
                f.write(plain)
                f.truncate()


    def merge(self):
        with open('in.ts', 'ab') as f:
            for i in range(self.size):
                with open(str(i) + '.ts', 'rb') as r:
                    f.write(r.read())


    def convert(self, filename):
        os.system('ffmpeg -hide_banner -loglevel error -i in.ts -c copy ' + filename)


    def clean(self):
        os.remove('in.ts')
        for i in range(self.size):
            os.remove(str(i) + '.ts')

