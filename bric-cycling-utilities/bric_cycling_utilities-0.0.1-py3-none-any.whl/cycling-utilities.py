#!/usr/bin/env python
# coding: utf-8

# # Cycling Utilities

# In[ ]:


def log( msg, time = True, show = True, file = 'data/log.txt' ):
    """
    Logs a message.
    :param msg: Message to log.
    :param time: Include time stamp in print. [Default: True]
    :param show: Print message to console. [Default: True]
    :param file: Log file path. [Default: 'log.txt']
    """
    if show:
        if time:
            # add time stamp to print
            msg = '[{}] '.format( dt.now() ) + msg

        print( msg, flush = True )

    if not time:
        # add time stamp for logging if not already
        msg = '[{}] '.format( dt.now() ) + msg

    # write to log file
    try:
        with open( file, 'a' ) as f:
            f.write( msg + '\n' )

    except Exception as err:
        reason = 'Could not write to log file.'

        if show:
            print( reason, flush = True )
            print( err, flush = True )

        logging.debug( reason )
        logging.debug( err )


# In[ ]:


def hold_jump( 
    prg, 
    rest, 
    voltages = None, 
    jump 	 = None, 
    rate 	 = None,
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
    # convert to mV

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

