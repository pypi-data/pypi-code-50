# encoding: utf-8

import numpy            as np
import matplotlib.pylab as plt


class SEIR(object):


    def __init__(self, s, e, i, r, sigma, k, b):

        self.s = s
        self.e = e
        self.i = i
        self.r = r
        self.n = float(self.s + self.e + self.i + self.r)

        self.sigma = sigma # E -> I
        self.k     = k     # I -> R
        self.b     = b     # I -> contact(SEIR)



    def fit(self):

        pass



    def predict(self, n, show=True):

        s = [self.s]
        e = [self.e]
        i = [self.i]
        r = [self.r]
        
        t = list(range(n))

        dis = []

        for _t in t[:-1]:

            ds = -self.b * (s[_t]/self.n) * i[_t]
            print(s[_t], self.n, self.b, i[_t], ds)
            ns = s[_t] + ds 
            ns = 0 if ns < 0 else ns # underflow
            s.append(ns)

            dei = self.sigma * e[_t]
            de = -ds-dei
            ne = e[_t] + de
            e.append(ne)

            dr = self.k * i[_t]
            nr = r[_t] + dr
            r.append(nr)

            di = dei-dr
            dis.append(di)
            ni = i[_t] + di
            i.append(ni)

        # show
        if show:

            # ns = np.array(s)/self.n
            # ne = np.array(e)/self.n
            # ni = np.array(i)/self.n
            # nr = np.array(r)/self.n

            plt.plot(t, s, 'c-', label='S')
            plt.plot(t, e, 'b-', label='E')
            plt.plot(t, i, 'r-', label='I')
            plt.plot(t, r, 'g-', label='R')

            # inflection point
            for i in range(len(dis)-1):
                if not ((dis[i] >  0 and dis[i+1] >  0) or 
                        (dis[i] == 0 and dis[i+1] == 0) or
                        (dis[i] <  0 and dis[i+1] <  0)):
                    plt.vlines(i+1, 0, self.n, color='k', linestyle='--', label='t = %s' % (i+1))

            # plt.ylim((-0.2, 1.2))

            plt.legend()
            plt.show()
            
        return t, s, e, i, r
