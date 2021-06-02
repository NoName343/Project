import pyAesCrypt
import os

from crypt import *

def decryption(file, password):
    """For decryption"""
    buffer_size = 512 * 1024
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )
    os.remove(file)

def walking_by_dir(dir, password):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            try:
                decryption(path, password)
                print('[-] - File decryption')
            except Exception as ex:
                print(ex)
        else:
            walking_by_dirs(path, password)
