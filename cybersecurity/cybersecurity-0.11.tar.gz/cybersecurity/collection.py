class InfoCollect():
    def __init__(self, ip):
        self.ip = ip
        self.packet = 'No data found'
    def arpPing(self):
        from scapy.all import srp, Ether, ARP
        ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = self.ip), timeout=2)
        packet = ''
        for snd,rcv in ans:
            print "Tarfet is alive"
            print rcv.sprintf("%Ether.src% - %ARP.psrc%")
            packet += Ether.src + '-' + ARP.psrc + '\n'
        return packet
