from Anapass.TModule import *


#TDevice 객체 생성 

device = TDevice(TDevice.TMonitor)

print("Connect...")
isConnect = device.Connect()
if isConnect != True :
    print("Connect Fail")
    quit()
print("Connect to TMoniot....OK")

regAddr=0xD6 # ChipID
level2Offset=0 # Level2Offset
readCount=5  # read count
regValueArray=bytes(readCount)  #ctypes.create_string_buffer(readCount) 

print("Read ChipID....")
isOK = device.ReadReg(regAddr, level2Offset, readCount, regValueArray)
if isOK != True :
    print("FAIL: ReadReg,  Check the connection between TMonitor and T4/T5 Device")
    quit()

for regValue in regValueArray :
    print(hex(regValue))
    
device.Disonnect()



