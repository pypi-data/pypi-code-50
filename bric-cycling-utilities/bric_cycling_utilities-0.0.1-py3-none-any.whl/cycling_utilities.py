#!/usr/bin/env python
# coding: utf-8

# # Cycling Utilities

# In[1]:


import os
import math
import time
import logging
from datetime import datetime as dt

from bric_solar_simulator.controller import solar_simulator_controller as ssc


# In[2]:


def log( msg, time = True, show = True, file = 'data/log.txt' ):
    """
    Logs a message.
    :param msg: Message to log.
    :param time: Include time stamp in print. [Default: True]
    :param show: Print message to console. [Default: True]
    :param file: Log file path. [Default: 'log.txt']
    """
    time_stamp = str( dt.now() ) # yyyy-mm-dd hh:mm:ss.xxxxxx 
    time_stamp = time_stamp.split( '.' )[ 0 ] # remove time resolution smaller than seconds
    
    if show:
        if time:
            # add time stamp to print
            msg = '[{}] '.format( time_stamp ) + msg

        print( msg, flush = True )

    if not time:
        # add time stamp for logging if not already
        msg = '[{}] '.format( time_stamp ) + msg

    # create file if needed
    file_path = os.path.basename( file )
    if not os.path.exists( file_path ):
        os.makedirs( file_path )
    
    # write to log file
    try:
        with open( file, 'a+' ) as f:
            f.write( msg + '\n' )

    except Exception as err:
        reason = 'Could not write to log file.'

        if show:
            print( reason, flush = True )
            print( err,    flush = True )

        else:
            logging.debug( reason )
            logging.debug( err )


# In[ ]:


def jump_vmpp( v_mpp, jump, direction ):
    """
    Modifies a dictionary of v_mpp.

    :param v_mpp: Dictionary of v_mpps.
    :param jump: Jump size.
    :param direction: Jump direction.
    :returns: Dictionary of modified v_mpp.
    """
    return { 
        ch: ( ch_vmpp + jump* direction ) 
        for ch, ch_vmpp in v_mpp.items() 
    }


# In[ ]:


def scan( 
    prg,
    turn,
    end   = None,
    rate  = 100,
    step  = 5,
    hold  = 0
):
    """
    Holds voltage for a time, then jumps the voltage.

    All parameters can be single values aplied to all channels, or a dictionary keyed by channel.
    :param turn: Voltage to turn scan at.
    :param end: Voltage to end scan at, or None to return to starting positions.
        [Default: None]
    :param rate: Scan rate in mV/s. [Default: 100]
    :param step: Scan step in mV. [Default: 5]
    :param hold: Hold time at turn in seconds.
    """

    if end is None:
        end = prg.v_mpp

    elif not isinstance( voltages, dict ):
        voltages = { ch: voltages for ch in prg.channels }

    log( 'Holding voltage on channels {}.'.format( prg.channels ) )

    # hold voltage
    prg.update_voltages( voltages )
    time.sleep( rest )

    # jump voltage
    log( 'Jumping voltage on channels {}.'.format( prg.channels ) )
    if jump is not None:
        jump      *= 1e-3
        jump_step *= 1e-3

        if rate is None:
            # no rate, jump immediately
            prg.v_mpp = jump_vmpp( prg.v_mpp, jump, direction )
            prg.update_voltages( prg.v_mpp )

        else:
            rate *= 1e-3

            # jump with rate
            remainder, jumps = math.modf( jump / jump_step )
            step_time = abs( jump / rate ) / jumps
            step_time = 0.5
            curr_jump = 0 
            while curr_jump < jumps:
                curr_jump += 1

                prg.v_mpp = jump_vmpp( prg.v_mpp, jump, direction )
                prg.update_voltages( prg.v_mpp )
                time.sleep( step_time )

            if remainder > 0:
                prg.v_mpp = jump_vmpp( prg.v_mpp, jump, direction )
                prg.update_voltages( prg.v_mpp )

    log( 'Restarting MPP on channels {}.'.format( prg.channels ) )


# In[3]:


def hold_jump( 
    prg, 
    rest, 
    voltages = None, 
    jump     = None, 
    rate     = None,
    jump_step = 5,
    direction = 1
):
    """
    Holds voltage for a time, then jumps the voltage.

    :param rest: Hold time in seconds.
    :param voltages: Dictionary of hold voltage in volts keyed by channel,
        a single voltage for all channels, or None to use MPP voltage.
        [Default: None]
    :param jump: Voltage jump after hold in mV, or None for no jump.
        [Default: None]
    :param rate: Jump rate in mV/s, or None for an immediate jump.
    :param jump_step: Jump step in mV. [Default: 5]
    :param direction: Direction of jump.
    """   
    if voltages is None:
        voltages = prg.v_mpp

    elif not isinstance( voltages, dict ):
        voltages = { ch: voltages for ch in prg.channels }

    log( 'Holding voltage on channels {}.'.format( prg.channels ) )

    # hold voltage
    prg.update_voltages( voltages )
    time.sleep( rest )

    # jump voltage
    log( 'Jumping voltage on channels {}.'.format( prg.channels ) )
    if jump is not None:
        jump      *= 1e-3
        jump_step *= 1e-3

        if rate is None:
            # no rate, jump immediately
            prg.v_mpp = jump_vmpp( prg.v_mpp, jump, direction )
            prg.update_voltages( prg.v_mpp )

        else:
            rate *= 1e-3

            # jump with rate
            remainder, jumps = math.modf( jump / jump_step )
            step_time = abs( jump / rate ) / jumps
            step_time = 0.5
            curr_jump = 0 
            while curr_jump < jumps:
                curr_jump += 1

                prg.v_mpp = jump_vmpp( prg.v_mpp, jump, direction )
                prg.update_voltages( prg.v_mpp )
                time.sleep( step_time )

            if remainder > 0:
                prg.v_mpp = jump_vmpp( prg.v_mpp, jump, direction )
                prg.update_voltages( prg.v_mpp )

    log( 'Restarting MPP on channels {}.'.format( prg.channels ) )


# In[ ]:


class SolarSimulatorCommander( ssc.SolarSimulatorController ):
    """
    Simplified Solar Simulator controller.
    """
    
    def __init__( self, port, spectra = None, intensities = None ):
        """
        Creates a new SolarSimulatorCommander.
        
        :param port: Port of the Solar Simulator.
        :param spectra: Dictionary keyed by [ 'red', 'green', 'blue', 'uv' ]
            with spectral percentages. Values applied to both channels.
            [Default: None]
        :param intensities: Dictionary keyed by channel of spectral current
            from 0 to 1. Only used if spectra is None.
            [Default: None]
        """
        super().__init__( port )
        
        if spectra is not None:
            self.set_spectra( spectra )
            
        elif intensities is not None:
            self.set_intensities( intensities )

        
    def on( self ):
        if not self.connected:
            self.connect()
            
        for ch, inten in self.intensities.items():
            self.set_current_percent( inten, ch )
            
        for ch, inten in self.intensities.items():
            if inten > 0:
                self.enable( ch )
        
        
    def off( self ):
        if not self.connected:
            self.connect()
            
        self.disable_all()
        
        
    def set_spectra( self, spectra ):
        self.spectra = spectra
        
        intensities = { 
            # group 1
            0: spectra[ 'red'   ], 
            1: spectra[ 'green' ],
            2: spectra[ 'blue'  ],

            # group 2
            3: spectra[ 'red'   ],
            4: spectra[ 'green' ], 
            5: spectra[ 'blue'  ],

            # uv
            6: spectra[ 'uv' ],
            7: spectra[ 'uv' ]
        }

        self.intensities = {
            ch: s_int* 1e-2
            for ch, s_int in intensities.items()
        }
        
        
    def set_intensities( self, intensities ): 
        self.intensities = intensities
        
        spectra = {
            'red':   ( self.intensities[ 0 ] + self.intensities[ 3 ] ),
            'green': ( self.intensities[ 1 ] + self.intensities[ 4 ] ),
            'blue':  ( self.intensities[ 2 ] + self.intensities[ 5 ] ),
            'uv':    ( self.intensities[ 6 ] + self.intensities[ 7 ] )
        }
        
        self.spectra = {
            color: ( inten* 1e2/ 2 ) for color, inten in spectra.items()
        }
        

