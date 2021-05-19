from jabledl import decrypter
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def test_decrypt():
    key    = 'd41d8cd98f00b204e9800998ecf8427e'
    iv     = 'c4ca4238a0b923820dcc509a6f75849b'
    aes    = AES.new(bytes.fromhex(key), AES.MODE_CBC, bytes.fromhex(iv))
    cipher = aes.encrypt(pad(b'text', AES.block_size))
    assert unpad(decrypter.decrypt(cipher, key, iv), AES.block_size) == b'text'


def test_decrypt_segments(segment_size, key, iv):
    key    = 'd41d8cd98f00b204e9800998ecf8427e'
    iv     = 'c4ca4238a0b923820dcc509a6f75849b'
    aes    = AES.new(bytes.fromhex(key), AES.MODE_CBC, bytes.fromhex(iv))
    cipher = aes.encrypt(pad(b'text', AES.block_size))
    assert unpad(decrypter.decrypt(cipher, key, iv), AES.block_size) == b'text'
