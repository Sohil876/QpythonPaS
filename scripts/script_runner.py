#-*-coding:utf8;-*-
#qpy:2
#qpy:console

import os,sys

dir = '/sdcard/qpython/scripts/'
os.chdir(dir)
filelist = list(os.listdir('.'))
theDict = dict()
print "Python files in your scripts directory:"
for file in filelist:
    if file.endswith(".py"):
        theStats = os.stat(file)
        theDict[file] = theStats
for item in theDict:
    print("File: {:30s} Size: {:.2f} KB" .format(item,theDict[item].st_size/1024.0))
print("Input full name of your file:")
def modcmd(arg):
    filename = ('"{}"'.format(arg))
    os.system(sys.executable+' '+filename)
while(True):
  cmd=raw_input("-->")
  if (cmd==""): break;
  modcmd(cmd)

