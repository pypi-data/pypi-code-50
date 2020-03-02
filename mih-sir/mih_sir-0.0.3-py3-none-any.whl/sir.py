# encoding: utf-8

import numpy            as np
import matplotlib.pylab as plt


class SIR(object):


    def __init__(self, s, i, r, k, b):

        self.s = s
        self.i = i
        self.r = r
        self.n = float(self.s + self.i + self.r)

        self.k = k # I -> R
        self.b = b # I -> contact(SIR)

        self.inflection_x = 0
        self.inflection_y = self.k/self.b



    def fit(self):

        pass



    def predict(self, n, show=True):

        s = [self.s]
        i = [self.i]
        r = [self.r]
        
        t = list(range(n))

        for _t in t[:-1]:

            ds = -self.b * (s[_t]/self.n) * i[_t]
            ns = s[_t] + ds 
            ns = 0 if ns < 0 else ns # underflow
            s.append(ns)

            dr = self.k * i[_t]
            nr = r[_t] + dr
            r.append(nr)

            di = -ds-dr
            ni = i[_t] + di
            i.append(ni)

        # show
        if show:

            ns = np.array(s)/self.n
            ni = np.array(i)/self.n
            nr = np.array(r)/self.n

            plt.plot(t, ns, 'y.', label='S')
            plt.plot(t, ni, 'r.', label='I')
            plt.plot(t, nr, 'g.', label='R')

            # inflection point
            if s[0]/self.n > self.inflection_y:
                for x, y in enumerate(s):
                    if y/self.n == self.inflection_y:
                        self.inflection_x = x
                        break
                    elif y/self.n < self.inflection_y:
                        self.inflection_x = x-1
                        self.inflection_y = s[x-1]/self.n
                        break

            label = 't = %s, S(t) = %.2f, k/b = %.2f' % (self.inflection_x, self.inflection_y, self.k/self.b)
            plt.plot(self.inflection_x, self.inflection_y, 'b*', label=label)

            label = 't = %s' % self.inflection_x
            plt.vlines(self.inflection_x, 0, 1, color='c', linestyle='--', label=label)

            plt.ylim((0, 1))

            plt.legend()
            plt.show()
            
        return t, s, i, r
