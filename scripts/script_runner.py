#-*-coding:utf8;-*-
#qpy:2
#qpy:console

import os,sys

os.chdir('/sdcard/qpython/scripts/')
filelist = next(os.walk('.'))[2]
print "Python files in your scripts directory:"
for file in filelist:
    if file.endswith(".py"):
        print(os.path.join(file))
print("Input full name of your file:")
def modcmd(arg):
    arg2 = ('"{}"'.format(arg))
    os.system(sys.executable+' '+arg2)
while(True):
  cmd=raw_input("-->")
  if (cmd==""): break;
  modcmd(cmd)

