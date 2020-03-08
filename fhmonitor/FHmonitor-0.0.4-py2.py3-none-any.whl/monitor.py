#####################################################
# Read active and reactive power from the atm90e32 then
# store within mongodb.
#
# copyright Margaret Johnson, 2020.
# Please credit when evolving your code with this code.
########################################################


from FHmonitor.error_handling import handle_exception
from FHmonitor.atm90_e32_pi import ATM90e32
from FHmonitor.store import MongoDB
import threading  # for blinking LED.
import board  # for blinking LED.
import digitalio  # for blinking LED.
import logging
logger = logging.getLogger(__name__)


class Monitor:
    """Take active and reactive power readings
    from an atm90e32 and store the readings in
    the Rasp Pi's mongodb.

    Example::

        m = Monitor()
        m.init_sensor()

    Make sure to read all the parameters that can be input to
    :meth:`~FHmonitor.monitor.Monitor.init_sensor`.
    The values depend on the Power Transformer and CTs being used.

    The :meth:`~FHmonitor.monitor.Monitor.blink` method is useful
    to turn on and off the LED (for debugging purposes).

    """

    def __init__(self, led_pin=None):
        self.db = None
        self.energy_sensor = None
        if led_pin is None:
            led_pin = board.D18  # We always wire to GPIO 18.
        self.led = digitalio.DigitalInOut(board.D18)
        self.led.direction = digitalio.Direction.OUTPUT
    ####################################################
    # Initialize the energy sensor.  The properties are
    # are written to atm90e32 registers during initialization.
    # They are specific to the Power and Current Transformers
    # being used.  An exception occurs if the write cannot
    # be verified.
    ####################################################

    def init_sensor(self, lineFreq=4485, PGAGain=21, VoltageGain=36650,
                    CurrentGainCT1=25368, CurrentGainCT2=25358):
        """
        Initialize the atm90e32 by setting the calibration registry properties.
        Calibration is discussed within our
        `FitHome wiki <https://github.com/BitKnitting/FitHome/wiki/ElectricityMonitor#calibration>`_ .

        :param lineFreq: 4485 for 60 Hz (North America, Default), 389 for 50 Hz (rest of world)
        :param PGAGain: Programmable Gain -  0 for 10A (1x), 21 for 100A (2x, Default), 42 for 100A - 200A (4x)
        :param VoltageGain: Dependent on transformer being used.  Should be measured prior to taking readings.
            See the Calibration discussion linked to above.
        :param CurrentGainCT1: Dependent on the CTs being used.  Should be measured prior to taking readings.
            See the Calibration discussion linked to above.
        :param CurrentGainCT2: Similar to CurrentGainCT1, but for the second CT.

        :return: True if meter is initialized.
            False if meter could not be initialized.
        """  # noqa

        try:
            self.energy_sensor = ATM90e32(lineFreq, PGAGain, VoltageGain,
                                          CurrentGainCT1, 0, CurrentGainCT2)
            logger.info('Energy meter has been initialized.')
            # We have an instance of the atm90e32.  Let's check if we get
            # sensible readings.
            sys0 = self.energy_sensor.sys_status0
            if (sys0 == 0xFFFF or sys0 == 0):
                e = 'EXCEPTION: Cannot connect to the energy meter.'
                handle_exception(e)
            logger.info('Energy meter is working.')
            return True
        except Exception as e:
            handle_exception(e)
            return False

    def open_db(self, mongodb="mongodb://localhost:27017/", db="FitHome",
                collection="aggregate"):
        """Opens and maintains an instance to the mongo database where
        the power readings will be stored.

        :param mongodb: URI to the mongo database running on the Raspberry Pi
        :param db: Database within mongodb that holds the readings.
        :param collection: name of the collection where the readings are held.

        :return: True if the database can be opened.
        """
        try:
            self.db = MongoDB(mongodb, db, collection)
        except Exception as e:
            self.db = None
            handle_exception(e)
            return False
        return True

    def close_db(self):
        """It is more efficient to keep the mongodb open while
        using it.  However, if you know you will not be doing
        any more transactions, it is good to clean up the
        connections.
        """
        if self.db is not None:
            self.db.close()

    ####################################################
    # Get the current active and reactive power readings.
    ####################################################

    def take_reading(self):
        """Read the active and reactive power readings from
        the atm90e32 registers.

        :return: (Pa, Pr) Where Pa is the float value for the
            active power reading and Pr is the float value for
            the reactive power reading.
        """
        Pa = self.energy_sensor.total_active_power
        Pr = self.energy_sensor.total_reactive_power
        logger.info(
            f'Active Power reading: {Pa}  Reactive Power Reading: {Pr}')
        return Pa, Pr

    ####################################################
    # Store the reading into mongo db.
    ####################################################

    def store_reading(self, Pa, Pr):
        """Store the active and reactive power readings into
        the mongodb database.

        :param Pa: A floating value representing the active power reading.
            Obtained through a call to take_reading().
        :param Pr: A floating value representing the reactive power reading.
            As with Pa, use take_reading() to retrieve the value from the
            energy meter.

        Returns True if the readings could be stored.
        """
        if self.db is None:
            # Try opening with the defaults.
            db_opened = self.open_db()
            if db_opened is False:
                handle_exception('Cannot open the mongo database.')
                return False
        reading = {"Pa": Pa, "Pr": Pr, }
        reading_saved = self.db.save(reading)
        if reading_saved is False:
            handle_exception('Cannot store the readings.')
            return False

        return True
    ####################################################
    # Blink the LED
    ####################################################

    def blink(self, ntimes=1):
        """Blink the monitor's LED.  Uses Python's Timer object
        so that blinking does not pause data capture and
        storage.

        :param ntimes: Number of times to blink, defaults to 1
        :type ntimes: int, optional
        """
        def turn_led_on(n):
            self.led.value = True
            t = threading.Timer(0.5, turn_led_off, [n])
            t.start()

        def check_led(n):
            n -= 1
            if n > 0:
                turn_led_on(n)

        def turn_led_off(n):
            self.led.value = False
            t = threading.Timer(0.5, check_led, [n])
            t.start()
        # Start blinking.
        assert ntimes > 0
        turn_led_on(ntimes)
