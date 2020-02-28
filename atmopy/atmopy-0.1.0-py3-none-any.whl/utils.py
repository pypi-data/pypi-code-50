""" Holds general package utilities """


class AltitudeValueError(ValueError):
    def __init__(self, min_alt, max_alt):
        """ Custom exception when altitude checking

            Parameters
            ----------
            min_alt: float
                Minimum altitude for the model
            max_alt: float
                Maximum altitude for the model
            """

        # Call Exception.__init__(message)
        # to use the same Message header as the parent class
        super().__init__(f"Altitude must be within range [{min_alt}, {max_alt}] meters")


def check_altitude(alt, min_alt, max_alt):
    """ Checks if altitude within proper range

    Parameters
    ----------
    alt: float
        Current altitude
    min_alt: float
        Minimum altitude for the model
    max_alt: float
        Maximum altitude for the model
    """

    if alt < min_alt or alt > max_alt:
        # Altitude is out of bounds
        raise AltitudeValueError(min_alt, max_alt)
