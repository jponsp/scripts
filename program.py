#!/usr/bin/env python
# First python program
dir="/tmp"
import sys,os,time,subprocess
sys.stdout.flush()

print "System information: ",
print(os.uname())
print "User: %s" % os.getlogin()
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
os.system("netstat -ant | grep -i LISTEN| grep -v tcp6 | awk '{print $4}' | cut -f 2 -d: | sort -n")
print 

var = "boooop"
if var is None:
    print "Variable var not declared"
else:
    print "Variable var is declared and contain:",var,"sdaf"

tmp=os.popen('ls /var/tmp').read()
print("\n")
print("/tmp content")
print(tmp)



