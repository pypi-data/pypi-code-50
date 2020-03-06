import time
from functools import wraps

def tick_tock(debug=False):
    """ Function decorator to compute runtime of a particular method.
        use @tick_tock in front of a function definition
        tick_tock should include a boolean argument 'debug' to suppress or display runtime data
    """
    def tick_tock_decorator(method):

        @wraps(method)
        def timed(*args, **kwargs):
            if debug == True:
                ts = time.time()
                result = method(*args, **kwargs)
                te = time.time()

                print ('%r.%r --- %2.6f seconds ---' % \
                    (method.__module__, method.__name__, te-ts))
                return result
            else:
                result = method(*args, **kwargs)
                return result
        return timed
    return tick_tock_decorator
