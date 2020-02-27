#
#-*- coding:utf-8 -*-
"""
A module to support Tektronix TDS3000 series OSC. Mostly work with other OSC from Tektronix, with minor modification.
(C) Noboru Yamamoto,2017. KEK, Ibaraki, JAPAN

"""
import struct

try:
    import numpy
    _has_numpy=True
except ImportError:
    _has_numpy=False

#
# data objects
#
class waveform(object):
    enc={"ASCII":"%d","RIBINARY":">h",'RPBINARY':">H",'SRIBINARY':"<h",'SRPBINARY':"<H"}
    BFMT={'RI':"h",'RP':"H"}
    BORD={"MSB":">","LSB":"<"}
    
    def __init__(self, data):
        self.rdata=data.split(b";")
        wf_params=dict((e.split() for e in self.rdata if len(e.split()) == 2))
        self.descriptions=[e.split() for e in self.rdata if (len(e.split()) !=2)]
        
        self.points=int(wf_params[b":WFMPRE:NR_PT"])
        self.byte_width=int(wf_params[b':WFMPRE:BYT_NR'])
        self.bit_width=int(wf_params[b'BIT_NR'])
        self.ENC=wf_params[b'ENCDG']
        self.BIN_FMT=wf_params[b"BN_FMT"]
        self.BYTE_ORDER=wf_params[b'BYT_OR']
        self.Data_Num=int(wf_params[b'NR_PT']) #:WFMPRE:NR_PT
        #self.wfid=self.rdata[6]
        self.point_fmt=wf_params[b'PT_FMT']
        self.X_Incr=float(wf_params[b'XINCR'])
        self.Point_Offset=int(wf_params[b'PT_OFF'])
        self.X_Zero=float(wf_params[b'XZERO'])
        self.X_Unit=wf_params[b'XUNIT']
        self.Y_Mult=float(wf_params[b'YMULT'])
        self.Y_Zero=float(wf_params[b'YZERO'])
        self.Y_Offset=float(wf_params[b'YOFF'])
        self.Y_Unit=wf_params[b'YUNIT']
        self.v_offset=float(wf_params[b'VOFFSET'])
        self.v_pos=float(wf_params[b'VPOS'])
        self.v_scale=float(wf_params[b'VSCALE'])
        self.h_scale=float(wf_params[b'HSCALE'])
        self.h_delay=float(wf_params[b'HDELAY'])
        self.TS=None
        wfdata=wf_params[b":CURVE"]
        if (self.ENC == b"ASCII" or self.ENC == b"ASC"):
            self.conv_fmt=float
            self.wfsize=b""
            if (wfdata[0] == b":"):
                self.raw=wfdata[len(b":CURVE "):-1]
            else:
                self.raw=wfdata[:-1]
        else:
            self.conv_fmt = self.BORD[ self.BYTE_ORDER ] + self.BFMT[self.BIN_FMT]
            if ( wfdata[0] == b"#" ):#
               sz=int(wfdata[1])
               self.wfsize=dsz=int(wfdata[2:][:sz])
               self.raw=wfdata[2:][sz:][:self.wfsize]
            else:
                self.raw=wfdata[:-1]
        self._convert()
        
    def update(self,curve):
        if (self.ENC == b"ASCII" or self.ENC == b"ASC"):
            self.wfsize=b""
            if (curve[0] == b":"):
                self.raw=curve[len(":CURVE "):-1]
            else:
                self.raw=curve[:-1]
        else:
            if (curve[0] == b"#"):
                sz=2+int(curve[1])
                self.wfsize=dsz=int(curve[2:sz])
                self.raw=curve[sz:][:self.wfsize]
            else:
                self.raw=curve[:-1]
        self._convert()

    def _convert(self):
        if (self.ENC == b"ASCII" or self.ENC == b"ASC"):
            self.wf=[float(x) for x in self.raw.split(b",")]
        else:# binary
            # consider to use scipy.fromstring if scipy is avaialble
            #if _use_numpy_fromstring:
            #    self.wf=numpy.fromstring(self.raw[i:i+self.byte_width],
            #           dtype=np.uint,count=len(self.raw)/self.byte_width,sep='')
            #else
            self.wf=[struct.unpack(self.conv_fmt,
                                   self.raw[i:i+self.byte_width])[0]
                     for i in range(0,len(self.raw),self.byte_width)]

        self.y=[((y-self.Y_Offset)*self.Y_Mult+self.Y_Zero) for y in self.wf]
        self.x=[ (x*self.X_Incr+self.X_Zero) for x in range(len(self.y))]
        
    def trace(self):
        return zip(self.x,self.y)

    

if __name__ == "__main__":
    test()
