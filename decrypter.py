from Crypto.Cipher import AES


def decrypt(cipher, key, iv):
    aes = AES.new(bytes.fromhex(key), AES.MODE_CBC, bytes.fromhex(iv))
    return aes.decrypt(cipher)


def decrypt_segments(segment_size, key, iv):
    for i in range(segment_size):
        with open('%d.ts' % i, 'rb+') as f:
            plain = decrypt(f.read(), key, iv)
            f.seek(0)
            f.write(plain)
            f.truncate()
