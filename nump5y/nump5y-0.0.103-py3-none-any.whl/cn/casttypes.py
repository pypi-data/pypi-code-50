Ans="""

Define the type of the following destination addresses:
a. 4A:30:10:21:10:1A
b. 47:20:1B:2E:08:EE
c. FF:FF:FF:FF:FF:FF
Solution
To find the type of the address, we need to look at the second hexadecimal digit from the left. If it
is even, the address is unicast. If it is odd, the address is multicast. If all digits are Fs, the address
is broadcast. Therefore, we have the following:
a. This is a unicast address because A in binary is 1010 (even). 
b. This is a multicast address because 7 in binary is 0111 (odd).
c. This is a broadcast address because all digits are Fs in hexadecimal

"""
