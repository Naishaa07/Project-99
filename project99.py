import time
import os
import shutil
time=time.time()
adress = input("Pls enter the directory")
if(os.path.exists(adress)):
    list = os.listdir(adress)
    for counter in list:
        adress2=adress+'/'+counter
        ctime=os.stat(adress2).st_ctime
        if(time-ctime>25,92,000):
             name, extension = os.path.splitext(counter)
             if(extension==''):
                 shutil.rmtree(adress2)
             else:
                 os.remove(adress2)
else:
    print("Path not found")