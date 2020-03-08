Ans="""

packets not equal to port number
!(tcp.port==18)
analysis of tcp
tcp.analysis.flags
packets containing ipaddr 192.168.0.1 with a particular http request
http.request==192.168.0.1
Display packet containing content of tcp protocol
TCP->  Apply as columns of tcp protocol
To display http protocol with respcode200
http.response.code==200
reset tcp protocol
tcp.flags.reset==1

"""
