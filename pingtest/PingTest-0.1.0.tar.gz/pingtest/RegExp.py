import re

string101="PING www.google.com (216.58.213.100) 56(84) bytes of data.\n64 bytes from lhr25s02-in-f100.1e100.net (216.58.213.100): icmp_seq=1 ttl=53 time=22.4 ms\n\n--- www.google.com ping statistics ---\n1 packets transmitted, 1 received, 0% packet loss, time 0ms\nrtt min/avg/max/mdev = 22.402/22.402/22.402/0.000 ms"

matchms = re.match("(time\w+)", string101)
print('MATCH = ' + str(matchms))

match2 = re.findall("time=\d+.\d+",string101)
print(match2)

#match3 = re.search("time=",string101)
#print(match3)
#print(match3.string)

match4 = re.search(r"\time\bS\w+",string101)
print(match4)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
