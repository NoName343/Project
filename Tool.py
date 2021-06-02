from GPSPhoto import gpsphoto
from crypt import *
from decrypt import *

import os
import shutil


dir = 1
rename = 1
folder = 'C:/Users/Desktop/Android/Crypt/'
dir_photo = 'C:/Users/Desktop/Android/File/'
while True:
    if not os.path.exists(folder + str(dir)):
        os.makedirs(folder + str(dir))
    for item1 in os.listdir(dir_photo):
        fol1 = os.listdir(folder + str(dir))
        fol1 = len(fol1)
        if not fol1 == 2:
            shutil.move(os.path.join(dir_photo, item1), folder + str(dir))
            fol1 = os.listdir(folder + str(dir))
            fol1 = len(fol1)
            if fol1 == 2:
                for item2 in os.listdir(folder + str(dir)):
                    os.rename(os.path.join(folder + str(dir), item2), os.path.join(folder + str(dir), str(rename) + '.jpg'))
                    rename += 1
                file_jpg = f'C:/Users/Desktop/Android/Crypt/{dir}/1.jpg'
                file_txt = f'C:/Users/Desktop/Android/Crypt/{dir}/1.txt'
                data = gpsphoto.getGPSData(file_jpg)
                with open(file_txt, 'w') as p:
                    p.write(str(data))
                    p.close()
                rename = 1
                dir += 1
