import os
import time
import shutil
import subprocess
import random
import zipfile
import pyperclip

from core import *


subprocess.call('cls', shell=True)
print('1. On toll')
print('2. Rename')
print('3. Decrypt files')
print('4. Archive')

choice = input(': ')
subprocess.call('cls', shell=True)

if choice == '1':
    list = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890'
    password = ''
    num_choice = int(input('Number of files in one package: '))
    for item in range(25):
        password += random.choice(str(list))
    print()
    print()
    print('Cope password ----------------->   ', password)
    time.sleep(10)
    subprocess.call('cls', shell=True)
    core(password, num_choice)

if choice == '2':
    num = 1
    path = f'C:/Users/Mr.Gas/Desktop/test/crypt/{num}'

    number_of_files = f'C:/Users/Mr.Gas/Desktop/test/crypt/'
    num_dir_file = len(os.listdir(number_of_files))

    for item in range(num_dir_file):
        path = f'C:/Users/Mr.Gas/Desktop/test/crypt/{num}'
        for item1 in os.listdir(path):
            if item1 == str(11):
                os.rename(os.path.join(path, item1), os.path.join(path, str(item1) + '.txt.crp'))
            else:
                os.rename(os.path.join(path, item1), os.path.join(path, str(item1) + '.jpg.crp'))
        num += 1

if choice == '3':
    password1 = input('Enter password: ')
    num = 1
    path = f'C:/Users/Mr.Gas/Desktop/test/crypt/{num}'
    number_of_files = f'C:/Users/Mr.Gas/Desktop/test/crypt/'
    num_dir_file = len(os.listdir(number_of_files))
    for item in range(num_dir_file):
        path = f'C:/Users/Mr.Gas/Desktop/test/crypt/{num}'
        walking_by_dir(path, password1)
        num += 1

if choice == '4':
    dir_file = 'C:/Users/Mr.Gas/Desktop/test/zipfille/crypt'
    for folder, subfolders, files in os.walk(dir_file):
        for file in files:
            fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), dir_file), compress_type = zipfile.ZIP_DEFLATED)
            os.remove(os.path.join(folder, file))
    fantasy_zip.close()
