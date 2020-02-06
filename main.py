import os
import glob
import time, sys, datetime
import shutil
from pathlib import Path
from stat import S_ISREG, ST_CTIME, ST_MODE

now = datetime.datetime.today()
Current_Date = datetime.datetime.today().strftime('%d-%m-%Y')
path1=(r'/home/alexh/PycharmProjects/auto_delete_file/MD 88348_50063520_QSG_DE.pdf')
os.rename(path1, path1+str(Current_Date)+'.pdf')
backup_dir=Path(r'/home/alexh/PycharmProjects/auto_delete_file/DATA_MED_'+str(Current_Date))
try:
    backup_dir.mkdir()
except FileExistsError as exc:
    print(exc)

dir_path = sys.argv[1] if len (sys.argv) == 2 else r'.'

data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)

data = ((stat[ST_CTIME], path)
        for stat, path in data if S_ISREG(stat[ST_MODE]))
for cdate, path in sorted(data):
    print(time.ctime(cdate), os.path.basename(path))

#shutil.copytree()

#now = time.time()
#path = r"/home/alexh/PycharmProjects/auto_delete_file/"
#h= input("Enter day after delete information: \n")
#for filename in os.listdir(path):
#    if os.path.getmtime(os.path.join(path, filename)) < - float(h) * 86400:
#        if os.path.isfile(os.path.join(path, filename)):
#            print(filename)
#            os.remove(os.path.join(path, filename))
#os.rmdir("suares")
#print("directory removed!")

#files = glob.glob('/home/alexh/PycharmProjects/auto_delete_file/*.txt')
#for f in files:
#    os.remove(f)