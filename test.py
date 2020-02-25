import os, time
from glob import glob
from datetime import date
import time,datetime, sys
import shutil
from pathlib import Path
CurrentDate = datetime.datetime.today().strftime('%d-%m-%Y')
file_name = (r'/home/alexh/PycharmProjects/auto_delete_file/1111.txt')
now = time.time()
os.rename(file_name, file_name[:-4] + " " + str(CurrentDate) + '.txt')
search_fold = "/home/alexh/PycharmProjects/auto_delete_file/"
os.chdir(search_fold)
folders = filter(os.path.isdir,os.listdir(search_fold))
folders = [os.path.join(search_fold, f) for f in folders]
folders.sort(key=lambda x: os.path.getmtime(x))
print(folders[0])
stt = folders[0]
stat=os.stat(stt).st_ctime
cr_date=datetime.datetime.fromtimestamp(stat).strftime('%d-%m-%Y %H:%M')
print(cr_date)

backup_dir =Path(r'/home/alexh/PycharmProjects/skjsdlkgj/COPY_DATA_MED'+str(CurrentDate))
try:
    backup_dir.mkdir()
except FileExistsError as exc:
    print(exc)
dest = backup_dir
#for filename in os.listdir(search_fold):
#    if os.path.getmtime(os.path.join(search_fold, filename)) <now  - 7*86400:
#        if os.path.isdir(os.path.join(search_fold,filename)):
#            print(filename)
#            shutil.move(filename, dest)


src = folders[0]
shutil.move(src,dest)
#d = '.'
#folders = list(filter(lambda x: os.path.isdir(os.path.join(d,x)), os.listdir(d)))