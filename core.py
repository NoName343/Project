import os
import shutil
import pyAesCrypt
import subprocess
import pyperclip


#------------------------
def encryption(file, password):
    buffer_size = 512 * 1024
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )
    os.remove(file)
#------------------------
def walking_by_dirs(Dir_ForEncryption, password):
    for name in os.listdir(Dir_ForEncryption):
        path = os.path.join(Dir_ForEncryption, name)
        if os.path.isfile(path):
            if name.endswith(".jpg"):
                encryption(path, password)
            if name.endswith(".txt"):
                encryption(path, password)
#------------------------
def decryption(file, password):
    buffer_size = 512 * 1024
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )
    os.remove(file)
#------------------------
def walking_by_dir(dir, password):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        else:
            walking_by_dirs(path, password)
#------------------------
def correct():
    geo = input('Geo: ')
    pyperclip.copy('Text')
    subprocess.call('cls', shell=True)
    with open(folder + str(num_dir) + '/11.txt', 'w') as w:
        w.write(str(geo))
        w.close()
#------------------------
folder = 'C:/Users/Mr.Gas/Desktop/test/crypt/'
dcim = 'C:/Users/Mr.Gas/Desktop/test/DCIM'
#------------------------
def core(password, num):
    global num_dir
    num_dir = 1

    global remane_file
    remane_file = 0

    global remane_file_txt
    remane_file_txt = '11'

    while True:
        if not os.path.exists(folder + str(num_dir)):
            os.makedirs(folder + str(num_dir))
#---------------------------------------
        for item in os.listdir(dcim):
            shutil.move(os.path.join(dcim, item), folder + str(num_dir))
            walking_by_dirs(folder + str(num_dir), password)
            for item1 in os.listdir(folder + str(num_dir)):
                if item1.endswith(".crp"):
                    os.rename(os.path.join(folder + str(num_dir), item1), os.path.join(folder + str(num_dir), str(remane_file)))
                    remane_file += 1
            fol = os.listdir(folder + str(num_dir))
            fol = len(fol)
            if fol == num:
                remane_file = 0
                correct()
                walking_by_dirs(folder + str(num_dir), password)
                #------------------------
                for item2 in os.listdir(folder + str(num_dir)):
                    if item2.endswith(".crp"):
                        os.rename(os.path.join(folder + str(num_dir), item2), os.path.join(folder + str(num_dir), remane_file_txt))
                #------------------------
                num_dir += 1
#---------------------------------------
