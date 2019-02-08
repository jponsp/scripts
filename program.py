#!/usr/bin/env python
# First python program

import sys,os,time,subprocess
os.chdir("/tmp")
print "Current working dir is: %s" % os.getcwd()
print "Content:"
os.system("ls")
print "\n"
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



