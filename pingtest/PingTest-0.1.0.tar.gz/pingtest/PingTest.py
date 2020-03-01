import os
import TkDisplay
import re
from subprocess import Popen, PIPE
import shlex
import time

from pingtest.GetDNS import DnsCheck
from pingtest.TkDisplay import TrafficLights
from pingtest.GetGateway import GatewayCheck

responselist = []
respomsems = []
responsetimedate = []
fixedhostlist = ["www.amazon.com","www.google.com","www.apple.com"]
hostlist = []
import mysql.connector

def CheckHost(hostcheck):

  #response = os.system("ping -c 1 " + hostcheck)

  pingbit = "ping -D -c 1 " + hostcheck
  args = shlex.split(pingbit)
  proc = Popen(args, stdout=PIPE, stderr=PIPE)
  out, err = proc.communicate()
  exitcode = proc.returncode
  print(str(out))

  matchms = re.findall("time=\d+.\d+",str(out))
  print('MATCH = ' + str(matchms))

  #and then check the response...
  if exitcode == 0:
    print(hostcheck, 'is up!')
    responselist.append("green")

    # Get response times from stdout
    matchms = re.findall("time=\d+.\d+\s\S\S",str(out))
    print('Match ms = ' + str(matchms))
    respomsems.append(matchms[0])

    # Get date/time stampe from stdout
    matchtd = re.findall("\d{10}",str(out))
    print('Match time/date = ' + str(matchtd))
    print(time.ctime(int(matchtd[0])))
    print(time.gmtime(int(matchtd[0])))
    responsetimedate.append(time.ctime(int(matchtd[0])))

  else:
    print(hostcheck, 'is down!')
    responselist.append("red")
    respomsems.append("N/A")
    responsetimedate.append(" ")


def main():

    dnsip = DnsCheck()
    print("RETURNED = "+dnsip)
    hostlist.append(dnsip)

    gatewayip = GatewayCheck()
    print("RETURNED = "+gatewayip)
    hostlist.append(gatewayip)

    hostlist.append("8.8.8.8")
    hostlist.append("www.google.com")
#    hostlist.append("www.apple.com")

    print(hostlist)

    for hostcheck in hostlist:
        print(hostcheck)
        CheckHost(hostcheck)

    print("TEST1")
    lightup = TrafficLights
    lightup.DispLight(responselist, hostlist, respomsems, responsetimedate)
    print("RESPONSE LIST")
    print(responselist)

    mydb = mysql.connector.connect(
        host="localhost",
        user="colin",
        passwd="colin"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)

    print("TEST2")
    print(responselist)

if __name__ == '__main__':
    main()

