import os
import shutil
import os.path

dir = 1
folder = 1
number_file = 3

cr = 'C:/Users/D.Gas/Desktop/Android1/core/cr/'
dcim = 'C:/Users/D.Gas/Desktop/Android1/core/dcim'


def list():
    list = os.listdir(cr + str(dir))
    list = len(list)
    return list


while True:
    if not os.path.exists(cr + str(dir)):
        os.makedirs(cr + str(dir))
    for item in os.listdir(dcim):
        shutil.move(os.path.join(dcim, item), cr + str(folder))
        list()
        if not list == number_list:
            shutil.move(os.path.join(dcim, item), cr + str(dir))
            list()
            if list == 2:
                os.rename(os.path.join(cr + str(dir), item), os.path.join(cr + str(dir), str(number_file) + '.jpg'))
                rename += 1
                dir += 1
                folder += 1
