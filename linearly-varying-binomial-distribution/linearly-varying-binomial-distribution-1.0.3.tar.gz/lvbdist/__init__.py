__version__ = "1.0.3"

from ._lvbdist import cmax_times as _cmax_times
from ._lvbdist import chave_success_given_no_successes_before as _chave_success_given_no_successes_before
from ._lvbdist import chave_first_success_at_n as _chave_first_success_at_n
from ._lvbdist import chave_first_success_at_n_E as _chave_first_success_at_n_E
from ._lvbdist import chave_success_within_n_attempts as _chave_success_within_n_attempts
from ._lvbdist import chave_m_successes_within_n_attempts as _chave_m_successes_within_n_attempts
from ._lvbdist import chave_m_or_more_successes_within_n_attempts as _chave_m_or_more_successes_within_n_attempts
from ._lvbdist import chave_m_successes_within_n_attempts_E as _chave_m_successes_within_n_attempts_E
from ._lvbdist import chave_special_success_within_n_attempts as _chave_special_success_within_n_attempts
from ._lvbdist import chave_special_success_within_n_attempts_E as _chave_special_success_within_n_attempts_E

class LVBdistribution:
    '''
    Linearly varying "binomial" distribution \n
    The probability of success given some trails will increase given successive failures util it hits 1, and
    the probability will reset to base if one success occurs \n
    `base`: the starting probability to success. between 0 and 1. eg. 0.02 \n
    `additional`: the constant added to the base probability upon failures. between 0 and 1. eg 0.02 \n
    `threshold`: how many successive failures to trigger. nonnegative. eg 50
    '''
    def __init__(self,  base: float,
                        additional: float,
                        threshold: int):
        if (base < 0 or additional < 0 or threshold < 0 or
            base > 1 or additional > 1):
            raise ValueError("Invalid probability")
        if additional == 0:
            raise ValueError("Step constant cannot be 0"
                "as this will fall back to binomial distribution")
        self.base = base
        self.additional = additional
        self.threshold = threshold
        self.maxtimes = _cmax_times(base, additional, threshold)

    def max_times_to_ensure_success(self) -> int:
        'the index of trail where the success chance is 1'
        return self.maxtimes

    def have_success_given_no_successes_before(self, n: int) -> float:
        'given that one failed for `n-1` times, the chance of success at `n`-th'
        return _chave_success_given_no_successes_before(self.base, self.additional, self.threshold, n)

    def have_first_success_at_n(self, n: int) -> float:
        'the chance for one fails for `n-1` times, then succeed at `n`-th'
        return _chave_first_success_at_n(self.base, self.additional, self.threshold, n)

    def have_first_success_at_n_E(self) -> float:
        'average waiting trails until a success'
        return _chave_first_success_at_n_E(self.base, self.additional, self.threshold)

    def have_success_within_n_attempts(self, n: int) -> float:
        'the chance of having at least one success within `n` trails'
        return _chave_success_within_n_attempts(self.base, self.additional, self.threshold, n)

    def have_m_successes_within_n_attempts(self, n: int, m: int) -> float:
        'the chance of having `m` successes within `n` trails'
        return _chave_m_successes_within_n_attempts(self.base, self.additional, self.threshold, n, m)

    def have_m_or_more_successes_within_n_attempts(self, n: int, m: int) -> float:
        'the chance of having m or more successes within `n` trails'
        return _chave_m_or_more_successes_within_n_attempts(self.base, self.additional, self.threshold, n, m)

    def have_m_successes_within_n_attempts_E(self, n: int) -> float:
        'average number of successes given `n` trails'
        return _chave_m_successes_within_n_attempts_E(self.base, self.additional, self.threshold, n)

    def have_special_success_within_n_attempts(self, n: int, p: float) -> float:
        '''an event with probability `p` given a success can be marked as a special success.\n
        the chance of having at least one such special success within `n` trails\n
        `p` is between 0 and 1 exclusively.
        '''
        # errors are caught in c
        return _chave_special_success_within_n_attempts(self.base, self.additional, self.threshold, n, p)

    def have_special_success_within_n_attempts_E(self, p: float) -> float:
        '''an event with probability `p` given a success can be marked as a special success.\n
        the average waiting trails until a success\n
        `p` is between 0 and 1 exclusively.
        '''
        return _chave_special_success_within_n_attempts_E(self.base, self.additional, self.threshold, p)

__all__ = ( 'LVBdistribution', )
