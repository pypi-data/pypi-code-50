"""Rate limiting primitives."""

__all__ = ['Throttle', 'throttle']

import asyncio
import collections
import fractions
import functools
import re
import time


class AwaitableMixin:
    """Awaitable object.

    This enables the idiom:

        await throttle

    as an alternative to:

        await throttle.acquire()

    """

    def __await__(self):
        return self.acquire().__await__()


class ContextManagerMixin:
    """Context manager.

    This enables the following idiom for acquiring and releasing a
    throttle around a block:

        async with throttle:
            <block>

    """

    async def __aenter__(self):
        await self.acquire()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.release()


class WrapperMixin(ContextManagerMixin):
    """Coroutine wrapper.

    This enables wrapping of a coroutine that always need
    acquiring and releasing a throttle:

    @throttle('3/s')
    async def coroutine():
        <block>

    """

    def __call__(self, coroutine):
        @functools.wraps(coroutine)
        async def wrapper(*args, **kwargs):
            async with self:
                return await coroutine(*args, **kwargs)
        return wrapper


class RateMixin:
    """Encapsulation of a rate limiting.

    This enables setting the limiting rate in the following formats:

        - {integer limit}/{unit time}
        - {limit's numerator}/{limit's denominator}{unit time}

    Examples:

        - rates with integer limits:
            - '1/s', '2/m', '3/h', '4/d'
            - '5/second', '6/minute', '7/hour', '8/day'
        - rates with rational limits:
            - '1/3s', '12/37m', '1/5h', '8/3d'

    """

    # time quantities in the base unit
    TIME_QUANTITIES = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
    RATE_MASK = re.compile(r'([0-9]+)/([0-9]*)([A-Za-z]+)')

    @property
    def rate(self):
        return '{numerator}/{denominator}{unit_time}'.format(
            numerator=self.limit.numerator,
            denominator=self.limit.denominator or '',
            unit_time=self.unit_time
        )

    @rate.setter
    def rate(self, value):
        n, d, self.unit_time = self.RATE_MASK.match(value).groups()
        self.limit = fractions.Fraction(int(n), int(d or 1))
        self.limited_interval = self.limit.denominator * self.time_quantity

    @property
    def time_quantity(self):
        return self.TIME_QUANTITIES[self.unit_time[0].lower()]

    @property
    def period(self):
        return self.limited_interval / self.limit.numerator

    __slots__ = ('limit', 'limited_interval', 'factor', 'unit_time')

    def __init__(self, rate):
        self.rate = rate


class Throttle(AwaitableMixin, WrapperMixin, RateMixin):
    """Primitive throttle objects.

    A primitive throttle is a synchronization primitive that manages
    an internal counter and has a trace. A primitive throttle is in
    one of two states, 'locked' or 'unlocked'. It is not owned
    by a particular coroutine when locked.

    Each acquire() call:

        i) appends the coroutine to a FIFO queue
        ii) blocks until the throttle is 'locked'
        iii) decrements the counter

    Each release() call:

        i) appends current timestamp at the and of the trace
        ii) increments the counter

    Each locked() call:

        i) removes expired timestamps from the trace
        ii) returns True if the length of the trace
            exceeds the limit or the counter is equal to zero

    Usage:

        throttle = Throttle()
        ...
        await throttle
        try:
            ...
        finally:
            throttle.release()

    Context manager usage:

        throttle = Throttle()
        ...
        async with throttle:
            ...

    Throttle objects can be tested for locking state:

        if not throttle.locked():
            await throttle
        else:
            # throttle is acquired
            ...

    """

    __slots__ = ('_loop', '_waiters', '_trace', '_value', '_bound_value')

    def __init__(self, rate, *, loop=None):
        super().__init__(rate)
        self._loop = loop or asyncio.get_event_loop()
        self._waiters = collections.deque()
        self._trace = collections.deque(maxlen=self.limit.numerator)
        self._value = self.limit.numerator
        self._bound_value = self.limit.numerator

    def locked(self):
        """Return True if throttle can not be acquired immediately."""
        now = time.time()
        while self._trace and now - self._trace[0] > self.limited_interval:
            self._trace.popleft()
        return len(self._trace) >= self.limit.numerator or self._value == 0

    async def acquire(self):
        """Acquire a throttle."""
        fut = self._loop.create_future()
        self._waiters.append(fut)
        while True:
            if fut.done():
                self._waiters.remove(fut)
                self._value -= 1
                break
            elif self.locked():
                delay = self.limited_interval - (time.time() - self._trace[0])
                await asyncio.sleep(delay)
            else:
                for fut in self._waiters:
                    if not fut.done():
                        fut.set_result(True)

    def release(self):
        """Release a throttle."""
        if self._value >= self._bound_value:
            raise ValueError('Throttle released too many times.')
        self._trace.append(time.time())
        self._value += 1


throttle = Throttle
