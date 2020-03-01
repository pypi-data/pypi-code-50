import os

hostcheck='www.goodfgdfgdfgl.com'
print(hostcheck, 'is down!')
tracecheck = os.system("traceroute " + hostcheck)
print("HELLO"+str(tracecheck))
print("Tracecheck ended")

