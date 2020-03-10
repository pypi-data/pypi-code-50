Ans="""

13.2 STANDARD ETHERNET
We refer to the original Ethernet technology with the data rate of 10 Mbps as the Stan-
dard Ethernet. Although most implementations have moved to other technologies in
the Ethernet evolution, there are some features of the Standard Ethernet that have not
changed during the evolution. We discuss this standard version to pave the way for
understanding the other three technologies. 
13.2.1 Characteristics
Let us first discuss some characteristics of the Standard Ethernet.
Connectionless and Unreliable Service
Ethernet provides a connectionless service, which means each frame sent is independent
of the previous or next frame. Ethernet has no connection establishment or connection
termination phases. The sender sends a frame whenever it has it; the receiver may or may
not be ready for it. The sender may overwhelm the receiver with frames, which may result
in dropping frames. If a frame drops, the sender will not know about it. Since IP, which is
using the service of Ethernet, is also connectionless, it will not know about it either. If the
transport layer is also a connectionless protocol, such as UDP, the frame is lost and
salvation may only come from the application layer. However, if the transport layer is
TCP, the sender TCP does not receive acknowledgment for its segment and sends it again. 
Ethernet is also unreliable like IP and UDP. If a frame is corrupted during trans-
mission and the receiver finds out about the corruption, which has a high level of prob-
ability of happening because of the CRC-32, the receiver drops the frame silently. It is
the duty of high-level protocols to find out about it.

"""
