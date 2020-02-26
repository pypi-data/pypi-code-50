# -*- coding: utf-8 -*-
# Copyright (c) 2017 RS Components Ltd
# SPDX-License-Identifier: MIT License

"""
Interface for PmodMIC3 (ADCS7476 + Knowles Acoustics SPA2410LR5H-B).
"""

import spidev
CAP = 'SPI'
PHY = '1x6'


class PmodMIC3:
    MIC3_NO_BITS = 12
    dReference = 3.3
    
    def __init__(self, DSPMod6):
        self.port = DSPMod6
        
        self.cs = self.port.pin1
        self.nc = self.port.pin2
        self.miso = self.port.pin3
        self.sclk = self.port.pin4
        
        self.spi = spidev.SpiDev()
        self.__startSPI()
        
    def __startSPI(self):
        if self.cs == 7: #CE1
            self.spi.open(0,1)
        elif self.cs == 8: #CE0
            self.spi.open(0,0)
        else:
            #throw exception here
            return
        self.spi.max_speed_hz = 100000
        self.spi.mode = 0b00
        
    def __stopSPI(self):
        self.spi.close()
    
    def __spiRead16(self):
        resp = self.spi.xfer2([0x00, 0x00])
        w = resp[0] 
        w <<= 8
        w |= resp[1]
        return w
    
    def readIntegerValue(self):
        return self.__spiRead16()
        
    def readPhysicalValue(self):
        
        wIntVal = self.readIntegerValue()
        dVal = wIntVal* (self.dReference/((1<<self.MIC3_NO_BITS)-1))
        return dVal
        
    def cleanup(self):
        self.__stopSPI()
       
