#
# This code makes it easy to talk to the atm90e32 electricity monitor
# chip from a Rasp Pi python script.  It relies on Adafruit's nifty
# SPIDevice wrapper.  SPIDevice is a neat wrapper on SPI to handle
# locking/unlocking as well as when to set CS to HIGH/LOW.
#
# Copyright 2019, Margaret Johnson
# Please creded Margaret Johnson if you use in your code.  Thank you.
#
# Update 1/2020 - evolved micropython version to work on Rasp Pi.
#
import FHmonitor.meter.atm90_e32_registers as R


from adafruit_bus_device.spi_device import SPIDevice

import board
import busio
import digitalio
import math
import time
import struct
import logging
logger = logging.getLogger(__name__)
##########################################################
# error handling


def handle_exception(e):
    logger.exception(f'Exception...{e}')


SPI_WRITE = 0
SPI_READ = 1


class ATM90e32:
    ##########################################################################

    def __init__(self, linefreq, pgagain, ugain, igainA, igainB, igainC,
                 cs_pin=board.D5):
        # We'll need all the settings for the
        self._linefreq = linefreq
        self._pgagain = pgagain
        self._ugain = ugain
        self._igainA = igainA
        self._igainB = igainB
        self._igainC = igainC
        spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
        cs = digitalio.DigitalInOut(cs_pin)
        # How to use SPI
        # https://learn.adafruit.com/circuitpython-basics-i2c-and-spi/spi-devices
        # https://circuitpython.readthedocs.io/projects/busdevice/en/latest/_modules/adafruit_bus_device/spi_device.html
        self._device = SPIDevice(spi, cs, baudrate=200000, polarity=1, phase=1)
        #  TODO: DETERMINE SUCCESS/FAILURE of _init_config()
        try:
            self._init_config()
        except Exception as e:
            handle_exception(e)

    def _usleep(self, x): return time.sleep(x/(1e7))

    def _init_config(self):
        # CurrentGainCT2 = 25498  #25498 - SCT-013-000 100A/50mA
        if (self._linefreq == 4485 or self._linefreq == 5231):
            # North America power frequency
            FreqHiThresh = 61 * 100
            FreqLoThresh = 59 * 100
            sagV = 90
        else:
            FreqHiThresh = 51 * 100
            FreqLoThresh = 49 * 100
            sagV = 190

        # calculation for voltage sag threshold - assumes we do not want to
        # go under 90v for split phase and 190v otherwise sqrt(2) = 1.41421356
        fvSagTh = (sagV * 100 * 1.41421356) / (2 * self._ugain / 32768)
        # convert to int for sending to the atm90e32.
        vSagTh = self._round_number(fvSagTh)
        try:
            self._spi_rw(SPI_WRITE, R.SoftReset, 0x789A)   # Perform soft reset
            # enable register config access
            self._spi_rw(SPI_WRITE, R.CfgRegAccEn, 0x55AA)
            self._spi_rw(SPI_WRITE, R.MeterEn, 0x0001)   # Enable Metering

            # Voltage sag threshold
            self._spi_rw(SPI_WRITE, R.SagTh, vSagTh)
            # High frequency threshold - 61.00Hz
            self._spi_rw(SPI_WRITE, R.FreqHiTh, FreqHiThresh)
            # Lo frequency threshold - 59.00Hz
            self._spi_rw(SPI_WRITE, R.FreqLoTh, FreqLoThresh)
            self._spi_rw(SPI_WRITE, R.EMMIntEn0, 0xB76F)   # Enable interrupts
            self._spi_rw(SPI_WRITE, R.EMMIntEn1, 0xDDFD)   # Enable interrupts
            # Clear interrupt flags
            self._spi_rw(SPI_WRITE, R.EMMIntState0, 0x0001)
            # Clear interrupt flags
            self._spi_rw(SPI_WRITE, R.EMMIntState1, 0x0001)
            # ZX2, ZX1, ZX0 pin config
            self._spi_rw(SPI_WRITE, R.ZXConfig, 0x0A55)

            # Set metering config values (CONFIG)
            # PL Constant MSB (default) - Meter Constant
            # = 3200 - PL Constant = 140625000
            self._spi_rw(SPI_WRITE, R.PLconstH, 0x0861)
            # PL Constant LSB (default) - this is 4C68 in the application note,
            # which is incorrect
            self._spi_rw(SPI_WRITE, R.PLconstL, 0xC468)
            # Mode Config (frequency set in main program)
            self._spi_rw(SPI_WRITE, R.MMode0, self._linefreq)
            # PGA Gain Configuration for Current Channels - 0x002A (x4)
            # # 0x0015 (x2) # 0x0000 (1x)
            self._spi_rw(SPI_WRITE, R.MMode1, self._pgagain)
            # Active Startup Power Threshold - 50% of startup current
            # = 0.9/0.00032 = 2812.5
            # self._spi_rw(SPI_WRITE, PStartTh, 0x0AFC)
            # Testing a little lower setting...because readings aren't
            # happening if power is off then turned on....
            # Startup Power Threshold = .4/.00032 = 1250 = 0x04E2
            # Just checking with 0.
            self._spi_rw(SPI_WRITE, R.PStartTh, 0x0000)
            # Reactive Startup Power Threshold
            #  self._spi_rw(SPI_WRITE, QStartTh, 0x0AEC)
            self._spi_rw(SPI_WRITE, R.QStartTh, 0x0000)
            # Apparent Startup Power Threshold
            self._spi_rw(SPI_WRITE, R.SStartTh, 0x0000)
            # Active Phase Threshold = 10% of startup current
            # = 0.06/0.00032 = 187.5
            # self._spi_rw(SPI_WRITE, PPhaseTh, 0x00BC)
            self._spi_rw(SPI_WRITE, R.PPhaseTh, 0x0000)
            # Reactive Phase Threshold
            self._spi_rw(SPI_WRITE, R.QPhaseTh, 0x0000)
            # Apparent  Phase Threshold
            self._spi_rw(SPI_WRITE, R.SPhaseTh, 0x0000)

            # Set metering calibration values (CALIBRATION)
            # Line calibration gain
            self._spi_rw(SPI_WRITE, R.PQGainA, 0x0000)
            # Line calibration angle
            self._spi_rw(SPI_WRITE, R.PhiA, 0x0000)
            # Line calibration gain
            self._spi_rw(SPI_WRITE, R.PQGainB, 0x0000)
            # Line calibration angle
            self._spi_rw(SPI_WRITE, R.PhiB, 0x0000)
            # Line calibration gain
            self._spi_rw(SPI_WRITE, R.PQGainC, 0x0000)
            # Line calibration angle
            self._spi_rw(SPI_WRITE, R.PhiC, 0x0000)
            # A line active power offset
            self._spi_rw(SPI_WRITE, R.PoffsetA, 0x0000)
            # A line reactive power offset
            self._spi_rw(SPI_WRITE, R.QoffsetA, 0x0000)
            # B line active power offset
            self._spi_rw(SPI_WRITE, R.PoffsetB, 0x0000)
            # B line reactive power offset
            self._spi_rw(SPI_WRITE, R.QoffsetB, 0x0000)
            # C line active power offset
            self._spi_rw(SPI_WRITE, R.PoffsetC, 0x0000)
            # C line reactive power offset
            self._spi_rw(SPI_WRITE, R.QoffsetC, 0x0000)

            # Set metering calibration values (HARMONIC)
            # A Fund. active power offset
            self._spi_rw(SPI_WRITE, R.POffsetAF, 0x0000)
            # B Fund. active power offset
            self._spi_rw(SPI_WRITE, R.POffsetBF, 0x0000)
            # C Fund. active power offset
            self._spi_rw(SPI_WRITE, R.POffsetCF, 0x0000)
            # A Fund. active power gain
            self._spi_rw(SPI_WRITE, R.PGainAF, 0x0000)
            # B Fund. active power gain
            self._spi_rw(SPI_WRITE, R.PGainBF, 0x0000)
            # C Fund. active power gain
            self._spi_rw(SPI_WRITE, R.PGainCF, 0x0000)

            # Set measurement calibration values (ADJUST)
            # A Voltage rms gain
            self._spi_rw(SPI_WRITE, R.UgainA, self._ugain)
            # A line current gain
            self._spi_rw(SPI_WRITE, R.IgainA, self._igainA)
            self._spi_rw(SPI_WRITE, R.UoffsetA, 0x0000)    # A Voltage offset
            # A line current offset
            self._spi_rw(SPI_WRITE, R.IoffsetA, 0x0000)
            # B Voltage rms gain
            self._spi_rw(SPI_WRITE, R.UgainB, self._ugain)
            # B line current gain
            self._spi_rw(SPI_WRITE, R.IgainB, self._igainB)
            self._spi_rw(SPI_WRITE, R.UoffsetB, 0x0000)    # B Voltage offset
            # B line current offset
            self._spi_rw(SPI_WRITE, R.IoffsetB, 0x0000)
            # C Voltage rms gain
            self._spi_rw(SPI_WRITE, R.UgainC, self._ugain)
            # C line current gain
            self._spi_rw(SPI_WRITE, R.IgainC, self._igainC)
            self._spi_rw(SPI_WRITE, R.UoffsetC, 0x0000)    # C Voltage offset
            # C line current offset
            self._spi_rw(SPI_WRITE, R.IoffsetC, 0x0000)
            self._spi_rw(SPI_WRITE, R.CfgRegAccEn, 0x0000)  # end configuration
        except Exception as e:
            handle_exception(e)

        # In order to get correct results, I needed to insert
        # a 'significant' delay.
        time.sleep(1)
    ##########################################################################
    @property
    def lastSpiData(self):
        reading = self._spi_rw(SPI_READ, R.LastSPIData, 0xFFFF)
        return reading
    ##########################################################################
    @property
    def sys_status0(self):
        reading = self._spi_rw(SPI_READ, R.EMMIntState0, 0xFFFF)
        return reading
    ##########################################################################
    @property
    def sys_status1(self):
        reading = self._spi_rw(SPI_READ, R.EMMIntState1, 0xFFFF)
        return reading
    #########################################################################

    @property
    def meter_status0(self):
        reading = self._spi_rw(SPI_READ, R.EMMState0, 0xFFFF)
        return reading

    ##########################################################################
    @property
    def en_status0(self):
        reading = self._spi_rw(SPI_READ, R.ENStatus0, 0xFFFF)
        return reading
    #########################################################################
    @property
    def meter_status1(self):
        reading = self._spi_rw(SPI_READ, R.EMMState1, 0xFFFF)
        return reading
    #########################################################################
    @property
    def line_voltageA(self):
        reading = self._spi_rw(SPI_READ, R.UrmsA, 0xFFFF)
        return reading / 100.0
    #########################################################################
    @property
    def line_voltageB(self):
        reading = self._spi_rw(SPI_READ, R.UrmsB, 0xFFFF)
        return reading / 100.0
    #########################################################################
    @property
    def line_voltageC(self):
        reading = self._spi_rw(SPI_READ, R.UrmsC, 0xFFFF)
        return reading / 100.0
    #########################################################################
    @property
    def line_currentA(self):
        reading = self._spi_rw(SPI_READ, R.IrmsA, 0xFFFF)
        return reading / 1000.0
    #########################################################################
    @property
    def line_currentC(self):
        reading = self._spi_rw(SPI_READ, R.IrmsC, 0xFFFF)
        return reading / 1000.0
    #########################################################################
    @property
    def frequency(self):
        reading = self._spi_rw(SPI_READ, R.Freq, 0xFFFF)
        return reading / 100.0
    #########################################################################
    @property
    def total_active_power(self):
        reading = self._read32Register(R.PmeanT, R.PmeanTLSB)
        return reading * 0.00032
    #########################################################################

    @property
    def active_power_A(self):
        reading = self._read32Register(R.PmeanA, R.PmeanALSB)
        return reading * 0.00032
        #####################################################################

    @property
    def active_power_C(self):
        reading = self._read32Register(R.PmeanC, R.PmeanCLSB)
        return reading * 0.00032
        #####################################################################

    @property
    def total_reactive_power(self):
        reading = self._read32Register(R.QmeanT, R.PmeanTLSB)
        return reading * 0.00032
    #########################################################################

    @property
    def reactive_power_A(self):
        reading = self._read32Register(R.QmeanA, R.PmeanALSB)
        return reading * 0.00032
        #####################################################################

    @property
    def reactive_power_C(self):
        reading = self._read32Register(R.QmeanC, R.PmeanCLSB)
        return reading * 0.00032

    ######################################################
    # Return the value that is stored at the address.
    ######################################################

    def read(self, address):
        two_byte_buf = bytearray(2)
        results_buf = bytearray(2)
        # Let atm90e32 know want to read the register.
        address |= 1 << 15
        struct.pack_into('>H', two_byte_buf, 0, address)
        with self._device as spi:
            # send address w/ read request to the atm90e32
            spi.write(two_byte_buf)
            # Get the unsigned short register values sent from the atm90e32
            spi.readinto(results_buf)
        return struct.unpack('>H', results_buf)[0]
    ######################################################
    # Write the val to the address.
    ######################################################

    def write(self, address, val):
        # pack the address into a the bytearray.  It is an unsigned short(H)
        # that needs to be in MSB(>)

        four_byte_buf = bytearray(4)
        struct.pack_into('>H', four_byte_buf, 0, address)
        struct.pack_into('>H', four_byte_buf, 2, val)
        with self._device as spi:
            spi.write(four_byte_buf)
    ######################################################
    # Verify the right.
    ######################################################

    def verify(self, address, val):
        if address == R.SoftReset:
            return True
        result = self.read(R.LastSPIData)
        return True if result == val else False

    ######################################################
    # read or write to spi.
    # Writes are verified.  If we detect the value was not
    # registered to the address, we raise an exception.
    ######################################################

    def _spi_rw(self, rw, address, val):

        if(rw):  # read
            return self.read(address)
        else:
            self.write(address, val)
            if not self.verify(address, val):
                e = f'EXCEPTION: Write to address 0x{address:02x} Failed.'
                handle_exception(e)
    ######################################################

    def _round_number(self, f_num):
        if f_num - math.floor(f_num) < 0.5:
            return math.floor(f_num)
        return math.ceil(f_num)

    #########################################################################
    def _read32Register(self, regh_addr, regl_addr):
        val_h = self._spi_rw(SPI_READ, regh_addr, 0xFFFF)
        val_l = self._spi_rw(SPI_READ, regl_addr, 0xFFFF)
        val = val_h << 16
        val |= val_l  # concatenate the 2 registers to make 1 32 bit number
        if ((val & 0x80000000) != 0):  # if val is negative,
            val = (0xFFFFFFFF - val) + 1  # 2s compliment + 1
        return (val)
