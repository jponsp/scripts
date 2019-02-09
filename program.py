#!/usr/bin/env python
# First python program
dir="/tmp"
import sys,os,sh

print ("System information: ", end='')
print(os.uname())
print ("User: %s" % os.getlogin())
print ()
print ("Current working dir is: %s" % os.getcwd())
print ("Changing working directory to")
os.chdir("/tmp")
os.getcwd()
print ("Current working dir is: %s" % os.getcwd())
print
print ("Content:")
os.system("ls")
print
print ("Open ports:")
os.system("netstat -ant | grep -i LISTEN| grep -v tcp6 | awk '{print $4}' | cut -f 2 -d: | sort -n")
print 

var = "boooop"
if var is None:
    print ("Variable var not declared")
else:
    print ("Variable var is declared and contain:",var,"sdaf")
print
tmp=os.popen('ls /var/tmp').read()
print("/tmp content")
print(tmp)



