#!/usr/bin/env python
# First python program
dir="/tmp"
import sys,os,time,subprocess
print "System information: "
print
print(os.uname())
print "Current working dir is: %s" % os.getcwd()
print "Changing working directory to",dir 
os.chdir("/tmp")
os.getcwd()
print "Current working dir is: %s" % os.getcwd()
print
print "Content:"
os.system("ls")
print
print "Open ports:"
os.system("netstat -ant | grep -i LISTEN")
print "\n"

var = "boooop"
if var is None:
    print "Variable var not declared"
else:
    print "Variable var is declared and contain:",var,"sdaf"

tmp=os.popen('ls /var/tmp').read()
print("\n")
print("/tmp content")
print(tmp)



