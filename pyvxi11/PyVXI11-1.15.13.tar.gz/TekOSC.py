#
#-*- coding:utf-8 -*-
"""
A module to support Tektronix TDS3000 series OSC. Mostly work with other OSC from Tektronix, with minor modification.
(C) Noboru Yamamoto,2009. KEK, Ibaraki, JAPAN

Referenc:
 "TDS3000,TDS3000B, and TDS3000C series Digital Phosphor Oscilloscopes", 071--381-03,Tektronix

 RPC server info on TDS300
  Get RPC info
   program vers proto   port
    395183    1   tcp   1008
    395184    1   tcp   1005
"""

#import vxi11Device
import cVXI11
import time,types,struct,sys
#exceptions

try:
    import numpy
    _use_numpy_fromstring=True
except:
    _use_numpy_fromstring=False
    
class TekOSC(cVXI11.Vxi11Device):
    def __init__(self,host,device="inst0,0",proto="tcp"):
        cVXI11.Vxi11Device.__init__(self, host,device,proto)
        self.IDN_Str=self.qIDN()
        self.write(b"VERBOSE ON;")
        self.write(b"HEADER OFF;")
        ID=self.IDN_Str[:-1].split(",")
        self.Make=ID[0]
        self.Model=ID[1]
        self.Option=ID[3]

    def respToDict(self, lables,resp):
        v=resp[:-1].split(";")
        d={}
        d.update(zip(lables,v))
        return d
        
    def qIDN(self):
        self.write(b"*IDN?;")
        return self.read()

    def qACQ(self):
        self.write(b"ACQ?;")
        return self.read()

    def qACQMODE(self):
        self.write(b"ACQ:MODE?;")
        return self.read()

    def qNUMAVG(self):
        self.write(b"ACQ:NUMAV?;")
        return int(self.read())

    def qNUMENV(self):
        self.write(b"ACQ:NUMENV?;")
        return int(self.read())

    def qAcqState(self):
        self.write(b"ACQ:STATE?;")
        return self.read()

    def qStopAfter(self):
        self.write(b"ACQ:STOPA?;")
        return self.read()

    def qAcqStopAfter(self):
        self.write(b"ACQ:STOPA?;")
        return self.read()

    def qAllEv(self):
        self.write(b"ALLE?;")
        return self.read()
        
    def qBusy(self):
        self.write(b"BUSY?;")
        return int(self.read())

    def qCH(self,ch=1):
        self.write(b"CH%d?;"%ch)
        return self.read()
        
    def qDESE(self):
        self.write(b"DESE?")
        return self.read()

    def qENC(self):
        self.write(b"DATA:ENC?")
        return self.read()

    def qVERBOSE(self):
        return self.ask(b":VERBOSE?")

    def qHEADER(self):
        return self.ask(b":HEADER?")

    def CLS(self):
        self.write(b"*CLS;\n")

    def OPC(self):
        self.write(b"*OPC;")

    def qOPC(self,io_timeout=10000):
        self.write(b"*OPC?;")
        return self.read(io_timeout=io_timeout)

    def Run(self):
        self.write(b":ACQ:STATE RUN;")

    def Stop(self):
        self.write(b":ACQ:STATE STOP;")

    def set_AcqState(self,state):
        if state in ("ON", "OFF","RUN","STOP","0","1"):
            self.write(b"ACQ:STATE %s;"%state)
        elif state[:-1] in ("ON", "OFF","RUN","STOP","0","1"):
            self.write(b"ACQ:STATE %s;"%state[:-1])

    def set_AcqStopAfter(self,state):
        if state in ("RUNST", "SEQ", "RUNSTOP","SEQUENCE"):
            self.write(b":ACQ:STOPA %s;"%state)
        elif state[:-1] in ("RUNST", "SEQ","RUNSTOP","SEQUENCE"):
            self.write(b":ACQ:STOPA %s;"%state[:-1])
        
    def clear(self):
        self.write(b"*CLS;")
        
    def wait(self):
        self.write(b"*WAI;")
        
    def device_clear(self,flags=0,lock_timeout=0,io_timeout=5):
        cVXI11.Vxi11Device.clear(self, flags, lock_timeout, io_timeout)

    def clear_all(self):
        self.clear()
        self.device_clear()
        
    def get_cursor(self):
        self.write(b":CURS?;")
        resp=self.read(4096)[:-1]
        return TekCursor(resp)
    
    def get_waveform(self,ch=1,requestSize=4096,io_timeout=3000):
        """
        it seems better to stop scanning before getting waveform data from TDS.
        """
        self.lock()
        try:
            if (type(ch) ==types.StringType):
                self.write(b":DAT:SOU %s;"%ch)
            else:
                self.write(b":DAT:SOU CH%d;"%ch)
            ts=time.time()
            self.write(b":WAVFRM?;");time.sleep(0.2) #0.2 sec seems a magic number for TDS3K
            r=self.readResponce(io_timeout=io_timeout,
                                requestSize=requestSize)
        finally:
            self.unlock()
        wf=waveform(r)
        wf.TS=ts
        return wf

    def get_curve(self,ch=1,requestSize=4096,io_timeout=3000):
        self.write(b":DAT:SOU CH%d;:CURV?;"%ch)
        return self.readResponce(io_timeout=io_timeout,
                                requestSize=requestSize)

    def set_fulldata(self):
        self.write(b"HOR:RECORDL 10000")
        self.write(b":DATA:START 1;")
        self.write(b":DATA:STTOP 10000;")

    def set_wf_binary(self,fmt="RIBIN"):
        self.write(b":DATA:ENC %s;"%fmt)
        
    def set_wf_ascii(self):
        self.write(b":DATA:ENC ASCI;")

    def set_ENC(self, mode):
        enc=("ASCIi","FAStest","RIBinary","RPBinary","SRIbinary","SRPbinary")
        enc=("ASCI","RIB","RPB","SRI","SRP")
        if (mode in enc):
            self.write(b":DATA:ENC %s;"%mode)
        elif type(mode) is types.StringType:
            self.write(b":DATA:ENC %s;"%mode)
        else:
            self.write(b":DATA:ENC %s;"%enc[mode])

    def select_data_source(self,source):
        if type(source) == type(1):
            self.write(b":DATA:SOU CH%d;"%source)
        else:
            self.write(b":DATA:SOU %s;"%source)

    def get_SESR(self):
        self.write(b"*ESR?;")
        return SESR(int(self.read()))

    def get_SBR(self):
        self.write(b"*STB?;")
        return SBR(int(self.read()))

    def get_DESER(self):
        self.write(b":DESE?;")
        return DESER(self.read())

    def get_ESER(self):
        self.write(b"*ESE?;")
        return ESER(self.read())

    def get_SRER(self):
        self.write(b"*SRE?;")
        return SRER(self.read())

    def get_measurement(self):
        self.write(b":MEASU?;")
        return self.readResponce()

    def reset_PSC(self): # reset Enable Registers (DESER/ESER/SRER)
        self.write(b"*PSC 1")

    def save_PSC(self): # reset Enable Registers (DESER/ESER/SRER)
        self.write(b"*PSC 0")


    def check_SRQ_source(self):
        # after SRQ occured, srq source registers should be examined to reset
        sbr=int(self.ask(b"*STB?"))
        # -/RQS(MSS)/ESB/MAV/-/-/-/-
        sesr=int(self.ask(b"*ESR?")) # Standard Event Status Register
        #SESR:PON/URQ/CME/EXE/DDE/QYE/RQC/OPC
        evnt=self.ask(b"ALLEV?")
        return dict(SBR=sbr, SESR=sesr,EVNT=evnt)

def bit(n,d):
    return (d>>n)&1
    
class Register:
    def __init__(self,ini_data):
        self.val=int(ini_data)
        
    def __str__(self):
        s=""
        for item in self.__dict__.items():
            if item[0] == "val":
                continue
            s+="%s:%d, "%item
        return s

class SESR(Register):
    """Standard Event Status Register
    bit7...................................bit.0
    PON | URQ | CME | EXE | DDE| QYE| RQC | OPC
    """
    def __init__(self,ini_data):
        Register.__init__(self,ini_data)
        self.pon=bit(7,self.val)
        self.urq=bit(6,self.val)
        self.cme=bit(5,self.val)
        self.exe=bit(4,self.val)
        self.dde=bit(3,self.val)
        self.qye=bit(2,self.val)
        self.rqc=bit(1,self.val)
        self.opc=bit(0,self.val)
        
class SBR(Register):
    """Status Byte Register
    bit7..................................bit.0
    - | RQS/MSS | ESB| MAV | - |  - |  - |  - 
    """
    def __init__(self,ini_data):
        Register.__init__(self,ini_data)
        self.rqs=bit(6,self.val)
        self.mss=bit(6,self.val)
        self.esb=bit(5,self.val)
        self.mav=bit(4,self.val)

class DESER(Register):
    """ Device Event Status Enable Register"
    bit7..................................bit.0
    PON | URQ | CME | EXE | DDE | QYE | RQC | OPC
    """
    def __init__(self,ini_data):
        Register.__init__(self,ini_data)
        self.pon=bit(7,self.val)
        self.urq=bit(6,self.val)
        self.cme=bit(5,self.val)
        self.exe=bit(4,self.val)
        self.dde=bit(3,self.val)
        self.qye=bit(2,self.val)
        self.rqc=bit(1,self.val)
        self.opc=bit(0,self.val)

class ESER(Register):
    """ Event Status Enable Register"
    bit7..................................bit.0
    PON | URQ | CME | EXE | DDE | QYE | RQC | OPC
    """
    def __init__(self,ini_data):
        Register.__init__(self,ini_data)
        self.pon=bit(7,self.val)
        self.urq=bit(6,self.val)
        self.cme=bit(5,self.val)
        self.exe=bit(4,self.val)
        self.dde=bit(3,self.val)
        self.qye=bit(2,self.val)
        self.rqc=bit(1,self.val)
        self.opc=bit(0,self.val)

class SRER(Register):
    """ Service Request Enable Register"
    bit7...........................bit.0
    - | - | ESB | MAV | - | - | - | -
    """
    def __init__(self,ini_data):
        Register.__init__(self,ini_data)
        self.esb=bit(5,self.val)
        self.mav=bit(4,self.val)
#
# data objects
#
class waveform:
    enc={"ASCII":"%d","RIBINARY":">h",'RPBINARY':">H",'SRIBINARY':"<h",'SRPBINARY':"<H"}
    BFMT={'RI':"h",'RP':"H"}
    BORD={"MSB":">","LSB":"<"}
    def __init__(self,data):
        """
        make sure "VERBOSE" is off before getting preamble of waveform data.
        """
        self.rdata=data.split(";")
        if (len(self.rdata) < 17):# avoide the magick number  for future models.
            sys.stderr.write(self.rdata[:16],len(self.rdata))
            raise ValueError("Not enough data")
        # shuld search for ":CURVE" for ascii "#" for binary data
        wfdata=";".join(self.rdata[16:])
        #Bug. Order of data may differenc in the recent models.  
        self.byte_width=int(self.rdata[0])
        self.bit_width=int(self.rdata[1])
        self.ENC=self.rdata[2]
        self.BIN_FMT=self.rdata[3]
        self.BYTE_ORDER=self.rdata[4]
        self.Data_Num=int(self.rdata[5])
        self.wfid=self.rdata[6]
        self.point_fmt=self.rdata[7]
        self.X_Incr=float(self.rdata[8])
        self.Point_Offset=int(self.rdata[9])
        self.X_Zero=float(self.rdata[10])
        self.X_Unit=self.rdata[11]
        self.Y_Mult=float(self.rdata[12])
        self.Y_Zero=float(self.rdata[13])
        self.Y_Offset=float(self.rdata[14])
        self.Y_Unit=self.rdata[15]
        self.TS=None
        if (self.ENC == "ASCII" or self.ENC == "ASC"):
            self.conv_fmt=float
            self.wfsize=""
            if (wfdata[0] == ":"):
                self.raw=wfdata[len(":CURVE "):-1]
            else:
                self.raw=wfdata[:-1]
        else:
            self.conv_fmt=self.BORD[self.BYTE_ORDER]+self.BFMT[self.BIN_FMT]
            if (wfdata[0] == "#"):
                sz=2+int(wfdata[1])
                self.wfsize=dsz=int(wfdata[2:sz])
                self.raw=wfdata[sz:-1]
            else:
                self.raw=wfdata[:-1]
        self._convert()
        
    def update(self,curve):
        if (self.ENC == "ASCII" or self.ENC == "ASC"):
            self.wfsize=""
            if (curve[0] == ":"):
                self.raw=curve[len(":CURVE "):-1]
            else:
                self.raw=curve[:-1]
        else:
            if (curve[0] == "#"):
                sz=2+int(curve[1])
                self.wfsize=dsz=int(curve[2:sz])
                self.raw=curve[sz:-1]
            else:
                self.raw=curve[:-1]
        self._convert()

    def _convert(self):
        if (self.ENC == "ASCII" or self.ENC == "ASC"):
            self.wf=[float(x) for x in self.raw.split(",")]
        else:# binary
            # consider to use scipy.fromstring if scipy is avaialble
            #if _use_numpy_fromstring:
            #self.wf=numpy.fromstring(self.raw[i:i+self.byte_width],dtype=np.uint,count=len(self.raw)/self.byte_width,sep='')
            #else
            self.wf=[struct.unpack(self.conv_fmt,
                                   self.raw[i:i+self.byte_width])[0]
                     for i in range(0,len(self.raw),self.byte_width)]

        self.y=[((y-self.Y_Offset)*self.Y_Mult+self.Y_Zero) for y in self.wf]
        self.x=[ (x*self.X_Incr+self.X_Zero) for x in range(len(self.y))]
        
    def trace(self):
        return zip(self.x,self.y)

class TekCursor:
    def __init__(self,data):
        ent=data.split(";")
        self.function=ent[0]
        self.mode=ent[1]
        self.unit=ent[2]
        self.vpos=(float(ent[3]),float(ent[4]),float(ent[5]))
        self.hdelta=float(ent[6])
        self.select=ent[7]
        self.hpos=(float(ent[8]),float(ent[9]))
        self.hbarspos=(float(ent[10]),float(ent[11]),float(ent[12]))

def test(hostip="10.9.16.20"):
    import Gnuplot
    tek=TekOSC(hostip)
    tek.set_fulldata()
    # for SRQ
    sys.stdout.write(b"%s"%tek.check_SRQ_source())
    tek.write(b":DESE 1")
    tek.write(b"*ESE 1")
    tek.write(b"*SRE 32")
    tek.createSVCThread()
    tek.enable_srq()
    gp=Gnuplot.Gnuplot()
    return test_run(tek,gp)

def test_run(tek,gp):
    runstate=tek.qAcqState()
    stopafter=tek.qAcqStopAfter()
    tek.Stop()
    tek.set_AcqStopAfter("SEQ")
    tek.Run();tek.qOPC()
    wf1,wf2=test_update(tek,gp)
    tek.set_AcqStopAfter(stopafter)
    tek.set_AcqState(runstate)
    return (tek,wf1,wf2,gp)

def test_update(tek,gp):
    wf1=tek.get_waveform(1)
    wf2=tek.get_waveform(2)
    gp.title("Python VXI-11 module example from %s"%tek.Model)
    gp.plot(wf1.trace(),wf2.trace())
    return (wf1,wf2)

if __name__ == "__main__":
    test()
