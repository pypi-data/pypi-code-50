from bisect import bisect_left

class ListTools():
    def index(self, a, x):
        ''' Locate the leftmost value exactly equal to x
            NOTE: It seems important to ensure ListTools().index works.
            There seems to be a difference in the sorting in query vs in Python.
            may be due to locale setting in Mysql??
        '''
        i = bisect_left(a, x)
        if i != len(a) and a[i] == x:
            return i
        raise ValueError

    def find_lt(self, a, x):
        'Find rightmost value less than x'
        i = bisect_left(a, x)
        if i:
            return a[i-1]
        raise ValueError

    def find_le(self, a, x):
        'Find rightmost value less than or equal to x'
        i = bisect_right(a, x)
        if i:
            return a[i-1]
        raise ValueError

    def find_gt(self, a, x):
        'Find leftmost value greater than x'
        i = bisect_right(a, x)
        if i != len(a):
            return a[i]
        raise ValueError

    def find_ge(self, a, x):
        'Find leftmost item greater than or equal to x'
        i = bisect_left(a, x)
        if i != len(a):
            return a[i]
        raise ValueError

    def chunks(self, l, n):
        'generate chunks of max_length n from list l'
        # For item i in a range that is a length of l,
        for i in range(0, len(l), n):
            # Create an index range for l of n items:
            yield l[i:i+n]

