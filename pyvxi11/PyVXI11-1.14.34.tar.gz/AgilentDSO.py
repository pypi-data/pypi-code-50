#
#-*- coding:utf-8 -*-
"""
A module to support
for Algilent DSO
(C) Noboru Yamamoto,2009. KEK, Ibaraki, JAPAN
Reference:
jkjblad04.14: vxi11scan 

 Get RPC info
   program vers proto   port
    100000    2   udp    111  portmapper
    100000    2   tcp    111  portmapper
    395180    1   tcp   1024
    395183    1   tcp   1024

link created to gpib0,7 
	 Error code:0
	 LinkID:22529568
	 port 999
	 MaxRecvSize:16384
Device is remote. RC:0
wrote *IDN?;

	 Error code:0
	 Size:7
start to read
52 bytes data read:AGILENT TECHNOLOGIES,DSO6014L,MY47090019,05.10.0284

#DSO6014A  on 2013/08/19 by NY
rpcinfo -p 169.254.254.254
   program vers proto   port
    100000    2   udp    111  portmapper
    100000    2   tcp    111  portmapper
    395180    1   tcp   1024  #???
    395183    1   tcp   1024  #VXI11_CORE 0x0607AF

% python vxi11scan.py 169.254.254.254 "gpib0,7"
link created to gpib0,7 

	 Error code:0
	 LinkID:33536912
	 port 1012
	 MaxRecvSize:16384

Device is remote. RC:0

wrote *IDN?

52 bytes data read:AGILENT TECHNOLOGIES,DSO6014A,MY48260329,05.26.0001

# DSO6014A
[noboru-mbookpro:python/VXI11/PyVXI11-Current] noboru% rpcinfo -p 192.168.2.10
   program vers proto   port
    100000    2   udp    111  portmapper
    100000    2   tcp    111  portmapper
    395180    1   tcp   1024
    395183    1   tcp   1024

% sudo /usr/local/bin/nmap -sS 192.168.2.10

Starting Nmap 6.40-2 ( http://nmap.org ) at 2013-12-17 11:34 JST
Nmap scan report for 192.168.2.10
Host is up (0.00044s latency).
Not shown: 994 closed ports
PORT     STATE SERVICE
21/tcp   open  ftp
80/tcp   open  http
111/tcp  open  rpcbind
1024/tcp open  kdm -> vxi11-core
5810/tcp open  unknown :vxWorks login(telnet)
5900/tcp open  vnc 
MAC Address: 00:30:D3:10:85:98 (Agilent Technologies)

Nmap done: 1 IP address (1 host up) scanned in 7.40 seconds

web interface also shows:
5025 for SCPI TCP/IP socket port
5024 SCPI telnet port

LXI class C/ver.1.1: Web Interface
"""

#import vxi11Device
import cVXI11
import time,types,struct,sys

if sys.version_info < (3,):
    from  exceptions import ValueError
    
import numpy as np
    
try:
    import numpy
    _use_numpy_frombuffer=True
except:
    _use_numpy_frombuffer=False

class AglDSO(cVXI11.Vxi11Device):
    def __init__(self,host, device=b"gpib0,7", proto=b"tcp"):
        cVXI11.Vxi11Device.__init__(self, host, device, proto)
        self.IDN_Str=self.qIDN()
        self.write(b"VERBOSE ON;")
        self.write(b"HEADER OFF;")
        ID=self.IDN_Str[:-1].split(b",")
        self.Make=ID[0]
        self.Model=ID[1]
        self.Option=ID[3]

    def respToDict(self, lables,resp):
        v=resp[:-1].split(b";")
        d={}
        d.update(list(zip(lables,v)))
        return d
    
    def qAckState(self):
        return self.ask(b"")

    def qAcqStopAfter(self,cmd=b""):
        return self.ask(b"")

    def set_AcqStopAfter(self,stopafter):
        pass

    def set_AcqState(runstate):
        pass

    def qACQMODE(self):
        return self.qAcqMode()

    def qAcqMode(self):
        "<mode> ::= {RTIMe | ETIMe | SEGMented}"
        self.write(b"ACQ:MODE?;")
        return self.read()

    def qAcqType(self):
        self.write(b"ACQ:TYPE?;")
        return self.read()

    def AcqType(self,atype=b"HRES"):
        """
        <type> ::= {NORMal | AVERage | HRESolution | PEAK}
        """
        self.write(b"ACQ:TYPE %s;"%atype)

    def qBusy(self):
        return self.ask(b":ACT?;")

    def qActivity(self):
        return self.ask(b":ACT?;")

    def Activity(self):
        " Clears the cumulative edge variables. "
        return self.write(b":ACT;")

    def qOPC(self,io_timeout=10000):
        self.write(b"*OPC?;")
        return self.read(io_timeout=io_timeout)

    def Run(self):
        self.write(b"RUN;")

    def Single(self):
        self.write(b"SINGLE;")

    def Stop(self):
        self.write(b"STOP;")

    def Status(self,disp=b"CHAN1"):
        """
        <display> ::= {CHANnel<n>
        |DIGital0,..,DIGital15
        | POD{1 |2}
        | BUS{1 | 2}
        | FUNCtion
        | MATH| SBUS}
        <n> ::= 1-2 or 1-4 in NR1 format
        """
        return self.ask(b":STAT? %s ;"%disp)

    def qTER(self):
        return self.ask(b":TER?;")

    def clear(self):
        self.write(b"*CLS;")
        
    def wait(self):
        self.write(b"*WAI;")
        
    def device_clear(self,flags=0,lock_timeout=0,io_timeout=5):
        cVXI11.Vxi11Device.clear(self, flags, lock_timeout, io_timeout)

    def clear_all(self):
        self.clear()
        self.device_clear()
        
    def get_cursor_mode(self):
        return self.ask(b":MARK:MODE?;")

    def set_cursor_mode(self,mode=b"OFF"):
        return self.write(b":MARK:MODE %s;"%mode)

    def get_cursor_x1pos(self):
        return self.ask(b":MARK:X1P?;")

    def set_cursor_x1pos(self,pos=b"0"):
        return self.write(b":MARK:X1P %s;"%mode)

    def get_cursor_x2pos(self):
        return self.ask(b":MARK:X2P?;")

    def set_cursor_x2pos(self,pos=b"0"):
        return self.write(b":MARK:X2P %s;"%mode)

    def get_cursor_xdelta(self):
        return self.ask(b":MARK:XDEL?;")
    
    def get_cursor_y1pos(self):
        return self.ask(b":MARK:Y1P?;")

    def set_cursor_y1pos(self,pos=b"0"):
        return self.write(b":MARK:Y1P %s;"%mode)

    def get_cursor_y2pos(self):
        return self.ask(b":MARK:Y2P?;")

    def set_cursor_y2pos(self,pos=b"0"):
        return self.write(b":MARK:Y2P %s;"%mode)

    def get_cursor_ydelta(self):
        return self.ask(b":MARK:YDEL?;")
    #
    def set_wf_ByteOrder(self,order=b"LSBF"):
        "Byte order = LSBF | MSBF"
        self.write(b":WAV:BYT %s;"%order)

    def get_wf_ByteOrder(self):
        "Byte order = LSBF | MSBF"
        return self.ask(b":WAV:BYT?;")
        
    def get_wf_format(self):
        "fmt = ASCII|WORD | BYTE"
        return self.ask(b":WAV:FORM?;")

    def set_wf_format(self,fmt=b"ASCII"):
        "fmt = ASCII|WORD | BYTE"
        self.write(b":WAV:FORM %s;"%fmt)

    def set_wf_binary(self,fmt=b"BYTE"):
        "fmt = WORD | BYTE"
        self.write(b":WAV:FORM %s;"%fmt)

    def set_wf_ascii(self):
        self.write(b":WAV:FORM ASCII;")
        
    def get_wf_point(self):
        return self.ask(b":WAV:POIN?;")

    def set_wf_point(self,point=b"1000"):
        """
        <# points> ::= {100 | 250 | 500 |1000 | <points_mode>} if waveformpoints mode is NORMal
        <# points> ::= {100 | 250 | 500 |1000 | 2000 ... 8000000 in 1-2-5sequence | <points_mode>} if waveform points mode is MAXimum or RAW
        <points_mode> ::= {NORMal |MAXimum | RAW}
        The raw acquisition record can only be transferred when the oscilloscope is not running and can only be retrieved from the analog or digital sources.
        """
        self.write(b":WAV:POIN %s;"%point)

    def get_wf_point_mode(self):
        return self.ask(b":WAV:POIN:MODE?;")

    def set_wf_point_mode(self,mode=b"NORM"):
        """
        mode=NORM | MAAX| RAW
        """
        self.write(b":WAV:POIN:MODE %s;"%mode)

    def get_wave_preamble(self):
        return wpreamble(self.ask(b":WAV:PRE?;"))
    
    def get_waveform(self,ch=1,io_timeout=5,requestSize=4096):
        """
        it is better to stop scanning before get waveform data on TDS.
        """
        if (type(ch) == bytes):
            self.write(b":WAV:SOUR %s;\n"%ch)
        else:
            self.write(b":WAV:SOUR CHAN%d;\n"%ch)
        import time
        header=self.get_wave_preamble()
        enc=self.get_wf_format().strip()
        byteo=self.get_wf_ByteOrder().strip()
        self.write(b":WAV:DATA?;\n")
        r=self.readResponce(io_timeout=io_timeout,requestSize=requestSize)
        wf=waveform(r,encformat=enc,byteo=byteo,preamble=header)
        return wf

    def get_curve(self,ch=1,io_timeout=5,requestSize=4096):
        self.write(b":WAV:SOUR CHAN%d;\n"%ch)
        self.write(b":WAV:DATA?")
        return self.readResponce(io_timeout=io_timeout,requestSize=requestSize)

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

    def SERIAL(self):
        return self.ask(b":SER?")

    def VIEW(self,source=b"CHAN1"):
        self.write(b":VIEW %s"%srouce)

    def BLANK(self,source=b"CHAN1"):
        self.write(b":BLANK %s"%srouce)
    
    def AUT(self,*sources):
        """
        Root Autoscale command
        """
        if sources:
            self.write(b":AUT %s"%", ".join(sources))
        else:
            self.write(b":AUT")
    
    def check_SRQ_source(self):
    # after SRQ occured, srq source registers should be examined to reset
        TER=int(self.ask(b"TER?"))
        STB=int(self.ask(b"*STB?"))
        ESR=int(self.ask(b"*ESR?"))
        OPR=int(self.ask(b":OPER?"))
        OPRC=int(self.ask(b":OPER:COND?"))
        AER=int(self.ask(b":AER?"))
        OVLR=int(self.ask(b":OVLR?"))
        return dict(TER=TER, STB=STB, ESR=ESR, 
                    OPR=OPR, OPRC=OPRC, AER=AER, OVLR=OVLR
                    )

def bit(n,d):
    return (d>>n)&1
    
class Register:
    def __init__(self,ini_data):
        self.val=int(ini_data)
    def __str__(self):
        s=""
        for item in list(self.__dict__.items()):
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
class wpreamble:
    """
        <preamble_block> ::= <formatNR1>, <type NR1>,<pointsNR1>,<count NR1>,
        <xincrementNR3>, <xorigin NR3>, <xreferenceNR1>,
        <yincrement NR3>, <yoriginNR3>, <yreference NR1>
        <format> ::= an integer in NR1format:
          0 for BYTE format
          1 for WORD format
          2 for ASCii format
        <type> ::= an integer in NR1format:
          0 for NORMal type
          1 for PEAK detect type
          2 for AVERage type
          3 for HRESolution type
        <count> ::= Average count, or 1 if PEAK detect type or NORMal; an integer in NR1 format
    """

    pre_block=(
        ("encformat",int),  # encoding  BYTE/WORD/ASCII
        ("type", int),   # Normal/PEAK/Averag/HRES
        ("points",int),  # number of points
        ("count", int),  # average count or 1
        ("xincrement",float), 
        ("xorigin",float),
        ("xreference",int),
        ("yincrement",float),
        ("yorigin",float),
        ("yreference",int)
        )
    PRE_FMT={0:b"BYTE",1:b"WORD",2:b"ASCII"}
    PRE_TYP={0:b"Normal", 1:b"Peak", 2:b"Average",3:b"HighResolution"}
    
    def __init__(self, data):
        """
        sample preamble
        b'+0,+0,+1000,+1,+2.00000000E-010,-1.00000000E-007,+0,+3.12500000E-002,+1.25000000E-002,+128\n'
        """
        self.str=data
        plist=data.split(b",")
        for i in range(len(plist)):
            key,conv=self.pre_block[i]
            self.__dict__[key]=conv(plist[i])
        self.FMT=self.PRE_FMT[self.encformat]
        
class waveform:
    PRE_FMT={0:"BYTE", 1:"WORD", 2:"ASCII"}
    #BFMT={b"ASCII":"%d","ASC":"%d","BYTE":"B","WORD":"H"}
    BFMT={b"ASCII":"%d", b"ASC":"%d", b"BYTE":"u1", b"WORD":"u2"}
    BORD={b"MSBF":">", b"LSBF":"<"}
    DWIDTH={b"ASCII":0, b"ASC":0, b"BYTE":1, b"WORD":2}
    DTYPE={b"ASCII":None, b"ASC":None, b"BYTE":np.byte, b"WORD":np.uint16}
    
    def __init__(self,data=None, encformat=b"ASC",byteo=b"LSBF",preamble=None):
        if preamble:
            if type(preamble) == type(b""):
                self.preamble=wpreamble(preamble)
            elif isinstance(preamble,wpreamble):
                self.preamble=preamble
            else:
                raise TypeError("invalid preamble")
        else:
            self.preamble=None
        self.ENC=encformat.strip() # ASC|BYTE|WORD
        self.point_fmt=encformat.strip()
        self.BYTE_ORDER=byteo.strip()
        self.BIN_FMT=encformat.strip()
        if self.preamble:
            self.points=self.preamble.points
            
            self.X_Incr=self.preamble.xincrement
            self.Point_Offset=self.preamble.xreference
            self.X_Zero=self.preamble.xorigin
            if (self.ENC == b"ASC"):
                self.Y_Mult=1
                self.Y_Zero=0
                self.Y_Offset=0
            else:
                self.Y_Mult=self.preamble.yincrement
                self.Y_Zero=self.preamble.yorigin
                self.Y_Offset=self.preamble.yreference
        else:
            self.points=0
            self.X_Incr=1
            self.Point_Offset=0
            self.X_Zero=0
            #self.X_Unit=self.rdata[11]
            self.Y_Mult=1
            self.Y_Zero=0
            self.Y_Offset=0
            #self.Y_Unit=self.rdata[15]
        if (self.ENC == b"ASCII" or self.ENC == b"ASC"):
            self.conv_fmt=float
        else:
            self.conv_fmt=np.dtype(self.BORD[self.BYTE_ORDER.decode()]+self.BFMT[self.BIN_FMT.decode()])

        if not data:
            return
        
        if data[:1] == b"#":
            hdsize=int(data[1:2])
        else:
            raise ValueError("invalid format")
        self.dsize=int(data[2:][:hdsize])
        # use number of points from premble, othewise calculate from data size
        if (self.points == 0 and (self.ENC == b"BYTE" or self.ENC == b"WORD")):
            self.points=self.dsize/DWIDTH[self.ENC.decode()]

        self.rdata=data[2:][hdsize:][:self.dsize]
        
        if (len(self.rdata) < self.dsize):
            raise ValueError("Not enough data %d of %d "%(self.dsize,len(self.rdata)))
        self.Data_Num=self.dsize
        #self.wfid=self.rdata[6]
        if (self.ENC == "ASCII" or self.ENC == "ASC"):
            self.wfsize=len(self.rdata.split(b","))
        else:
            self.wfsize=self.dsize

        self._convert()

        
    def update(self,curve):
        if (self.ENC == "ASCII" or self.ENC == "ASC"):
            self.wfsize=b""
            if (curve[0] == ":"):
                self.rdata=curve[len(b":CURVE "):-1]
            else:
                self.rdata=curve[:-1]
        else:
            if (curve[0] == "#"):
                sz=2+int(curve[1])
                self.wfsize=dsz=int(curve[2:sz])
                self.rdata=curve[sz:-1]
            else:
                self.rdata=curve[:-1]
        self._convert()

    def _convert(self):
        if (self.ENC == "ASCII" or self.ENC == "ASC"):
            self.wf=[float(x) for x in self.rdata.split(b",")]
        else:
            self.byte_width=self.DWIDTH[self.ENC]
            if _use_numpy_frombuffer:
                self.wf=np.frombuffer(self.rdata,
                                      dtype=self.conv_fmt,
                                      count=self.points) #, sep=''
            else:
                self.wf=[struct.unpack(self.conv_fmt,
                                       self.raw[i:i+self.byte_width])[0]
                         for i in range(0,len(self.raw),self.byte_width)]
                
        self.y=[((y-self.Y_Offset)*self.Y_Mult+self.Y_Zero) for y in self.wf]
        self.x=[ (x*self.X_Incr+self.X_Zero) for x in range(len(self.y))]
        
    def trace(self):
        return list(zip(self.x,self.y))

class AglCursor:
    def __init__(self,data):
        ent=data.split(b";")
        self.function=ent[0]
        self.mode=ent[1]
        self.unit=ent[2]
        self.vpos=(float(ent[3]),float(ent[4]),float(ent[5]))
        self.hdelta=float(ent[6])
        self.select=ent[7]
        self.hpos=(float(ent[8]),float(ent[9]))
        self.hbarspos=(float(ent[10]),float(ent[11]),float(ent[12]))

def test(hostip=b"10.8.47.30"):
    import Gnuplot
    agl=AglDSO(hostip)
    #agl.set_fulldata()
    gp=Gnuplot.Gnuplot()
    return test_run(agl,gp)

def test_run(agl,gp):
    #runstate=agl.qAcqState()
    #stopafter=agl.qAcqStopAfter()
    agl.Stop()
    #agl.set_AcqStopAfter(b"SEQ")
    agl.Run();
    while( agl.qOPC()[0] != "1"):
        continue
    agl.Stop()
    wf1,wf2=test_update(agl,gp)
    #agl.set_AcqStopAfter(stopafter)
    #agl.set_AcqState(runstate)
    return (agl,wf1,wf2,gp)

def test_update(agl,gp):
    agl.Run();
    while( agl.qOPC()[0] != "1"):
        continue
    agl.Stop()
    wf1=agl.get_waveform(b"CH1")
    wf2=agl.get_waveform(b"CH2")
    gp.title("Python VXI-11 module example \\n from %s"%agl.Model)
    gp.plot(wf1.trace()[:-1],wf2.trace()[:-1])
    return (wf1,wf2)

if __name__ == "__main__":
    test(b"10.8.46.23")
    """
    host:osc-mon-01.mr.jkcont
    ip:10.64.105.65
    MAC:00-30-d3-10-55-18

    host:osc-mon-02.mr.jkcont
    ip:10.64.105.66
    MAC:00-30-d3-10-55-19
    
    """
    messages=(
#        "*RST;*CLS;\n", 
        ":ACQUIRE:TYPE NORMAL;\n", 
        ":ACQUIRE:MODE SEGMENTED;\n", 
        ":ACQUIRE:SEGMENTED:COUNT 10;\n", 
        ":TRIGGER:SWEEP NORMAL;\n", 
        ":TRIGGER:EDGE:SOURCE CHANNEL1;\n", 
        ":TRIGGER:EDGE:SLOPE NEGATIXOVE;\n", 
        ":TRIGGER:EDGE:LEVEL 1E+0;\n", 
        ":TIMEBASE:SCALE 1E-4;\n", 
        ":CHANNEL1:SCALE 1E+0;\n", 
        ":CHANNEL1:OFFSET 1E+0;\n", 
        ":CHANNEL1:DISPLAY ON;\n", 
        ":DISPLAY:CLEAR;\n", 
        ":WAVEFORM:FORMAT ASCII;\n", 
        )

def test_segment(ip=b"10.8.47.30"):
    dso=AglDSO(ip)
    messages=(
        "*RST;*CLS;\n", 
        ":ACQUIRE:TYPE NORMAL;\n", 
        ":ACQUIRE:MODE SEGMENTED;\n", 
        ":ACQUIRE:SEGMENTED:COUNT 10;\n", 
        ":TRIGGER:SWEEP NORMAL;\n", 
        ":TRIGGER:EDGE:SOURCE CHANNEL1;\n", 
        ":TRIGGER:EDGE:SLOPE NEGATIVE;\n", 
        ":TRIGGER:EDGE:LEVEL 1E+0;\n", 
        ":TIMEBASE:SCALE 1E-4;\n", 
        ":CHANNEL1:SCALE 1E+0;\n", 
        ":CHANNEL1:OFFSET 1E+0;\n", 
        ":CHANNEL1:DISPLAY ON;\n", 
        ":DISPLAY:CLEAR;\n", 
        ":WAVEFORM:FORMAT ASCII;\n", 
#        "*OPC?;\n", 
        )

    for message in messages:
        sys.stdout.write(message)
        time.sleep(0.2)
        dso.write(message)
    sys.stdout.write("%s"%dso.ask(b"*OPC?\n", io_timeout=30000))
    dso.write(b":SINGLE;\n")
    return dso

def get_segment(dso,n):
    dso.write(b":ACQuire:SEGMented:INDex %d ;\n"%n)
    dso.write(b":WAVEFORM:DATA?;\n")
    r=dso.readResponce()
    return r
