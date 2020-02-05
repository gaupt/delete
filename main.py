import os
import glob
import time, sys

now = time.time()
path = r"/home/alexh/PycharmProjects/auto_delete_file/"
h= input("Enter day after delete information: \n")
for filename in os.listdir(path):
    if os.path.getmtime(os.path.join(path, filename))< - h * 86400:
        if os.path.isfile(os.path.join(path, filename)):
            print(filename)
            os.remove(os.path.join(path, filename))
#os.rmdir("suares")
#print("directory removed!")

#files = glob.glob('/home/alexh/PycharmProjects/auto_delete_file/*.txt')
#for f in files:
#    os.remove(f)