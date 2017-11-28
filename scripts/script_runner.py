#-*-coding:utf8;-*-
#qpy:2
#qpy:console

import os,os.path,sys

#sys.dont_write_bytecode = True
os.chdir('/sdcard/qpython/scripts/')
filelist = next(os.walk( '.' ))[2]
print "Python files in your scripts directory:"
for file in filelist:
    if file.endswith( ".py" ):
        print(os.path.join(file))
print("Input full name of your file:")
def modcmd(arg):
  os.system(sys.executable+" "+arg)
while(True):
  cmd=raw_input("-->")
  if (cmd==""): break;
  modcmd(cmd)

