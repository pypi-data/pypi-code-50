from bluepy.btle import Scanner, DefaultDelegate

def scanBLE():
    class ScanDelegate(DefaultDelegate):
        def __init__(self):
            DefaultDelegate.__init__(self)

        def handleDiscovery(self, dev, isNewDev, isNewData):
            if isNewDev:
                print ("Discovered device:{}".format(dev.addr))
            elif isNewData:
                print ("Received new data from {}".format(dev.addr))

    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.scan(10.0)

    for dev in devices:
        print ("Device {} ({}), RSSI={} dB".format(dev.addr, dev.addrType, dev.rssi))
        for (adtype, desc, value) in dev.getScanData():
            print ("  {} = {}".format(desc, value))
        
if __name__ == "__main__":
    scanBLE()
        
