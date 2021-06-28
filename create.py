import os
import time
import shutil
import subprocess
import random
import zipfile

from core import *


dir1 = '/storage/emulated/0/DCIM/Camera/'
dir2 = '/storage/emulated/0/DCIM/Camera1/'
container = '/storage/emulated/0/Music/data'
rename_container = '/storage/emulated/0/Books/Base_linux.pdf'
pas1 = ''

subprocess.call('clear', shell=True)
print('1. on program')
print('2. packing')
print('3. decrypt folder')
print('4. rename')
print('5. delete folder')
ch = int(input(': '))
if ch == 1:
    subprocess.call('clear', shell=True)
    pas1 = ''
    list = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz123456789'
    subprocess.call('clear', shell=True)
    for item in range(20):
        pas1 += random.choice(list)
    print()
    print()
    print('---------->', pas1)
    time.sleep(10)
    subprocess.call('clear', shell=True)
    # !----
    core(pas1)
    # !----


if ch == 2:
    subprocess.call('clear', shell=True)
    for item in os.listdir(dir1):
        shutil.move(os.path.join(dir1, item), dir2)


if ch == 3:
    subprocess.call('clear', shell=True)
    folder = '/storage/emulated/0/Android/data/com.rarlab.rar/files/new/cr/'
    for item in os.listdir(folder):
        print(item)
    cho = int(input('Choice folder: '))
    subprocess.call('clear', shell=True)
    pas3 = input('Password: ')
    dir3 = f'/storage/emulated/0/Android/data/com.rarlab.rar/files/new/cr/{cho}'
    walking_by_dir(dir3, pas3)


if ch == 4:
    folder = '/storage/emulated/0/Android/data/com.rarlab.rar/files/new/cr/'
    zip = '/storage/emulated/0/Books/data,zip'
    z = zipfile.ZipFile(zip, 'a')
    for root, dirs, files in os.walk(folder):
        for file in files:
            z.write(os.path.join(root,file))
    z.close()
    for item in os.listdir(folder):
        shutil.rmtree(os.path.join(folder, item))
    os.rename(zip, rename_container)



if ch == 5:
    subprocess.call('clear', shell=True)
    dir4 = f'/storage/emulated/0/Android/data/com.rarlab.rar/files/new/cr/'
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), dir4)
    shutil.rmtree(path)
