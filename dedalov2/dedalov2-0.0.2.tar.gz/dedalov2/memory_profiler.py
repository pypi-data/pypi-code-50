
import logging
from typing import Callable

MemoryProfiler = Callable[[], None]

LOG = logging.getLogger('dedalov2.memory_profile')


def profiler(profile: bool) -> MemoryProfiler:
    if profile:
        from mem_top import mem_top
        
        def p():
            LOG.debug(mem_top())
        return p
    else:
        def p():
            pass
        return p
