#!/usr/bin/env python
import subprocess
hostcall='www.goobdbfdbgle.com'
print(hostcall)
pingbit="ping -c 4"
allstring= pingbit + " " + hostcall
print(allstring)
#s = subprocess.check_output(["ping", "-c 4", "google.com"])
s = subprocess.check_output(allstring, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
output = s.decode("utf-8")
lines = output.split('\n')
for line in lines:
    print(line)
print("END")
