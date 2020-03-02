"""
    Author: Allen B. Downey, Matus Jokay, Roderik Ploszek

    This file contains an example program from The Little Book of
    Semaphores, available from Green Tea Press, greenteapress.com

    This code is in the public domain.
"""

import os
import signal
import sys
import _thread
import threading

from random import randint

_allocate_lock = _thread.allocate_lock


class Thread(threading.Thread):
    """Wrapper for the Thread class in the threading module."""
    def __init__(self, target, *args):
        """Create and start a thread.

        target: callable
        args: passed along to target
        """
        threading.Thread.__init__(self, target=target, args=args)
        self.start()


class FifoSemaphore(threading.Semaphore):
    """Wrapper for the Semaphore class in the threading module."""
    wait = threading.Semaphore.acquire
    down = wait

    def signal(self, n=1):
        """Signal the semaphore.
        n: how many times to signal
        """
        for i in range(n):
            self.release()

    up = signal

    def value(self):
        """Returns the current value of the semaphore.

        Note: asking for the value of a semaphore is almost always
        a bad idea.  If you do anything based on the result, it is
        likely to be a mistake.
        """
        return self._value


class CustomCondition(threading.Condition):
    """Condition where the insertion function can be modified """
    def wait(self, timeout=None):
        """Wait until notified or until a timeout occurs.

        If the calling thread has not acquired the lock when this method is
        called, a RuntimeError is raised.

        This method releases the underlying lock, and then blocks until it is
        awakened by a notify() or notify_all() call for the same condition
        variable in another thread, or until the optional timeout occurs. Once
        awakened or timed out, it re-acquires the lock and returns.

        When the timeout argument is present and not None, it should be a
        floating point number specifying a timeout for the operation in seconds
        (or fractions thereof).

        When the underlying lock is an RLock, it is not released using its
        release() method, since this may not actually unlock the lock when it
        was acquired multiple times recursively. Instead, an internal interface
        of the RLock class is used, which really unlocks it even when it has
        been recursively acquired several times. Another internal interface is
        then used to restore the recursion level when the lock is reacquired.

        """
        if not self._is_owned():
            raise RuntimeError("cannot wait on un-acquired lock")
        waiter = _allocate_lock()
        waiter.acquire()
        self._insert(waiter)
        saved_state = self._release_save()
        gotit = False
        try:  # restore state no matter what (e.g., KeyboardInterrupt)
            if timeout is None:
                waiter.acquire()
                gotit = True
            else:
                if timeout > 0:
                    gotit = waiter.acquire(True, timeout)
                else:
                    gotit = waiter.acquire(False)
            return gotit
        finally:
            self._acquire_restore(saved_state)
            if not gotit:
                try:
                    self._waiters.remove(waiter)
                except ValueError:
                    pass

    def _insert(self, waiter):
        """Insert waiter into the waiter queue"""
        raise NotImplementedError()


class LifoCondition(CustomCondition):
    """Condition variable with LIFO waiter insertion"""
    def _insert(self, waiter):
        self._waiters.insert(0, waiter)


class RandomCondition(CustomCondition):
    """Condition variable with random waiter insertion"""
    def _insert(self, waiter):
        self._waiters.insert(randint(0, len(self._waiters)), waiter)


class LifoSemaphore(FifoSemaphore):
    """Semaphore that uses LifoCondition"""
    def __init__(self, value=1):
        super().__init__(value)
        self._cond = LifoCondition(threading.Lock())


class RandomSemaphore(FifoSemaphore):
    """Semaphore that uses RandomCondition"""
    def __init__(self, value=1):
        super().__init__(value)
        self._cond = RandomCondition(threading.Lock())


class Semaphore:
    """Factory class for the Semaphore objects. Uses random waiter queue by
    default
    """
    def __new__(cls, value=1, insert='random'):
        subclasses = {
            'fifo': FifoSemaphore,
            'lifo': LifoSemaphore,
            'random': RandomSemaphore,
        }
        try:
            _class = subclasses[insert]
        except KeyError:
            raise ValueError(
                f"Incorrect insertion type '{insert}'. Supported types are fifo, lifo and random."
            )
        return _class(value)


class Mutex():
    """Wrapper for the Lock class in the threading module."""
    def __init__(self):
        self.m = threading.Lock()

    def lock(self, *args, **kwargs):
        return self.m.acquire(*args, **kwargs)

    def unlock(self):
        return self.m.release()


class Event(threading.Event):
    """Wrapper for the Event class in the threading module."""
    signal = threading.Event.set


_print = print
_print_mutex = Mutex()


def print(*args, **kwargs):
    _print_mutex.lock()
    _print(*args, **kwargs)
    _print_mutex.unlock()


def watcher():
    """Forks a process, and the child process returns.

    The parent process waits for a KeyBoard interrupt, kills
    the child, and exits.

    This is a workaround for a problem with Python threads:
    when there is more than one thread, a KeyBoard interrupt
    might be delivered to any of them (or occasionally, it seems,
    none of them).
    """
    child = os.fork()
    if child == 0:
        return

    try:
        os.wait()
    except KeyboardInterrupt:
        print('KeyBoardInterrupt')
        try:
            os.kill(child, signal.SIGKILL)
        except OSError:
            pass
    sys.exit()
