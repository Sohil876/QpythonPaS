#-*-coding:utf8;-*-
#qpy:2
#qpy:console

import os,os.path,sys
#sys.dont_write_bytecode = True

def modcmd(arg):
  os.system(sys.executable+" ""/sdcard/qpython/scripts/"+arg)

print("Input full script name placed in scripts directory.")
while(True):
  cmd=raw_input("-->")
  if (cmd==""): break;
  modcmd(cmd)

