import os
import shutil
import pyAesCrypt
import time
import subprocess


def core(password1):
    dir = 1
    rename = 1
    folder = '/storage/emulated/0/Android/data/com.rarlab.rar/files/new/cr/'
    dir_photo = '/storage/emulated/0/DCIM/Camera/'
    while True:
        if not os.path.exists(folder + str(dir)):
            os.makedirs(folder + str(dir))
        for item1 in os.listdir(dir_photo):
            fol1 = os.listdir(folder + str(dir))
            fol1 = len(fol1)
            if not fol1 == 2:
                time.sleep(1)
                shutil.move(os.path.join(dir_photo, item1), folder + str(dir))
                fol1 = os.listdir(folder + str(dir))
                fol1 = len(fol1)
                if fol1 == 2:
                    for item2 in os.listdir(folder + str(dir)):
                        # Gq1N22U8LkYa5RxKHyIR
                        os.rename(os.path.join(folder + str(dir), item2), os.path.join(folder + str(dir), str(rename) + '.jpg'))
                        rename += 1
                    geo = input('Geo: ')
                    with open(folder + str(dir) + '/1.txt', 'w') as w:
                        w.write(str(geo))
                        w.close()
                    subprocess.call('clear', shell=True)
                    walking_by_dirs(folder + str(dir), password1)
                    file_jpg = f'/storage/emulated/0/Android/data/com.rarlab.rar/files/new/cr/{dir}/1.jpg'
                    rename = 1
                    dir += 1


def encryption(file, password):
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
            if name.endswith(".jpg"):
                encryption(path, password)
            if name.endswith(".txt"):
                encryption(path, password)

# __________________

def decryption(file, password):
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
            except Exception as ex:
                print(ex)
        else:
            walking_by_dirs(path, password)
