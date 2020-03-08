'''
Austin Griffith
bsoptions.py

Provides an analytical solution to options via the Black Scholes methodology.
'''

import numpy as np
from scipy.stats import norm


class EuroOptions:
    '''
        
    The Black Scholes value of a European Call / Put option
    Payoffs are of the form :
    C = max(S - K, 0)
    P = max(K - S, 0)
    
    The delta value of a European Call / Put option measures sensitivity 
    of option value with respect to change in underlying asset price, 
    calculated from the derivative dV/dS
    Deltas are of the form :
    C = e**-qT N(d1)
    P = -e**-qT N(-d1)
    
    The gamma value of a European option measures sensitivity of option 
    delta with respect to change in underlying asset price,
    calculated from the derivative d2C/dS2
    Gamma is of the form :
    G = e**(-qT) N'(d1) / S vol sqrt(T)
    
    The rho value of a European Call / Put option measures sensitivity 
    of option value with respect to change in interest rate over the life 
    of the option, calculated from derivative dV/dr
    Rhos are of the form :
    C = e**-rT K T N(d2)
    P = -e**-rT K T N(-d2)
    
    The theta value of a European Call / Put option, measures sensitivity 
    of option value with respect to change in time,
    calculated from derivative dV/dT
    
    The vega value of a European Call / Put option measures sensitivity 
    of option value with respect to change in underlying asset volatility, 
    calculated from derivative dV/dσ
    Vega is of the form :
    V = S e**(-qT) N'(d1) sqrt(T)

    Parameters
    ----------
    spot : number of any type (int, float8, float64 etc.), numpy array of any type
        should the user wish to have a list of values output with varying s
        Spot value of underlying asset at current time, t
    strike : number of any type (int, float8, float64 etc.), numpy array of any type
        should the user wish to have a list of values output with varying k
        Strike value of option, determined at initiation
    riskfree : number of any type (int, float8, float64 etc.), numpy array of any type
        should the user wish to have a list of values output with varying r
        Risk free interest rate, implied constant till expiration
    tau : number of any type (int, float8, float64 etc.), numpy array of any type
        should the user wish to have a list of values output with varying T
        Time till expiration for option
    vol : number of any type (int, float8, float64 etc.), numpy array of any type
        should the user wish to have a list of values output with varying vol
        Volatility of underlying, implied constant till expiration in Black
        Scholes model
    div : number of any type (int, float8, float64 etc.) or numpy array of any type
        should the user wish to have a list of values output with varying q
        Continuous dividend payout, as a percentage

    Notes
    -----
    All parameters can be individual values.
    Only one of these parameters can be a numpy.array, otherwise there will be
    a dimension mismatch.

    '''
    
    def __init__(self, spot, strike, riskfree, tau, vol, div):
        self.s = spot
        self.k = strike
        self.r = riskfree
        self.T = tau
        self.vol = self.vol
        self.q = div
        
        self.d1, self.d2 = self._euroD()
        self.optionleg, self.strikeleg = self._euroParity()
        
        
    def EuroPrice(self):
        '''
        
        Returns
        -------
        [call,put] : list of pair of float or numpy.array values
            Euro call and put prices, type depends on input value.
            If all input values are individual numbers, then output will be float.
            If one input value is numpy.array, then output will be numpy.array.

        '''
        call = max(self._euroPriceCall(), 0)
        put = max(self._euroPricePut(), 0)
        return([call,put])
        
    def EuroCall(self):
        '''

        Returns
        -------
        data : dictionary float or numpy.array values
            Euro call price and greeks, labeled according to the respective value.
            If all input values are individual numbers, then output will be float.
            If one input value is numpy.array, then output will be numpy.array.

        '''
        price = max(self._euroPriceCall(), 0)
        delta = self._euroDeltaCall()
        gamma = self._euroGamma()
        vega = self._euroVega()
        theta = self._euroThetaCall()
        rho = self._euroRhoCall()
    
        eur = [price, delta, gamma, vega, theta, rho]        
        label = ['price','delta','gamma','vega','theta','rho']
        data = dict(zip(label, eur))
        return(data)
    
    def EuroPut(self):
        '''

        Returns
        -------
        data : dictionary float or numpy.array values
            Euro put price and greeks, labeled according to the respective value.
            If all input values are individual numbers, then output will be float.
            If one input value is numpy.array, then output will be numpy.array.

        '''
        price = max(self._euroPricePut(), 0)
        delta = self._euroDeltaPut()
        gamma = self._euroGamma()
        vega = self._euroVega()
        theta = self._euroThetaPut()
        rho = self._euroRhoPut()
    
        eur = [price, delta, gamma, vega, theta, rho]        
        label = ['price','delta','gamma','vega','theta','rho']
        data = dict(zip(label, eur))
        return(data)
    
    def _euroRhoCall(self):
        r = self.strikeleg*self.T*norm.cdf(self.d2)
        return(r)
    
    def _euroRhoPut(self):
        r = -1*self.strikeleg*self.T*norm.cdf(-1*self.d2)
        return(r)
    
    def _euroThetaCall(self):
        t = self._euroDerivTheta() - self.strikeleg*norm.cdf(self.d2) + \
            self.optionleg*norm.cdf(self.d1)
        return(t)
    
    def _euroThetaPut(self):
        t = self._euroDerivTheta() + self.strikeleg*norm.cdf(-1*self.d2) - \
            self.optionleg*norm.cdf(-1*self.d1)
        return(t)
    
    def _euroDerivTheta(self):
        dt = -0.5*np.exp(-1*self.q*self.T)*norm.pdf(self.d1)*self.s*self.vol / np.sqrt(self.T)
        return(dt)
    
    def _euroPriceCall(self):
        p = self.strikeleg*norm.cdf(-1*self.d2) - self.optionleg*norm.cdf(-1*self.d1)
        return(p)
    
    def _euroPricePut(self):
        p = self.optionleg*norm.cdf(self.d1) - self.strikeleg*norm.cdf(self.d2)
        return(p)
    
    def _euroD(self):
        d1 = (np.log(self.s / self.k) + \
              (self.r - self.q + 0.5*self.vol*self.vol)*self.T) / self.vol*np.sqrt(self.T)
        d2 = d1 - self.vol*np.sqrt(self.T)
        return(d1, d2)
    
    def _euroParity(self):
        o_leg = np.exp(-1*self.q*self.T)*self.s
        k_leg = np.exp(-1*self.r*self.T)*self.k
        return(o_leg, k_leg)
    
    def _euroGamma(self):
        g = np.exp(-1*self.q*self.T)*norm.pdf(self.d1) / (self.s*self.vol*np.sqrt(self.T))
        return(g)
    
    def _euroVega(self):
        v = self.s*np.exp(-1*self.q*self.T)*norm.pdf(self.d1)*np.sqrt(self.T)
        return(v)
    
    def _euroDeltaCall(self):
        ed = np.exp(-1*self.q*self.T)*norm.cdf(self.d1)
        return(ed)
        
    def _euroDeltaPut(self):
        ed = -1*np.exp(-1*self.q*self.T)*norm.cdf(-1*self.d1)
        return(ed)
    
    
    
class ExoticOptions:
    
    @staticmethod
    def AsianGeometric(s, k, r, T, vol, q):
        '''
        
        Calculate the Black Scholes value of Geometric Average Asian Call / Put
        option with a fixed strike
        Payoffs are of the form :
        C = max(AVG_geo - K, 0)
        P = max(K - AVG_geo, 0)
    
        Parameters
        ----------
        s : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying s
            Spot value of underlying asset at current time, t
        k : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying k
            Strike value of option, determined at initiation
        r : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying r
            Risk free interest rate, implied constant till expiration
        T : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying T
            Time till expiration for option
        vol : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying vol
            Volatility of underlying, implied constant till expiration in Black
            Scholes model
        q : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying q
            Continuous dividend payout, as a percentage
    
        Notes
        -----
        All parameters can be individual values.
        Only one of these parameters can be a numpy.array, otherwise there will be
        a dimension mismatch.
    
        Returns
        -------
        [call,put] : list of pair of float or numpy.array values
            Asian call and put values, type depends on input value.
            If all input values are individual numbers, then output will be float.
            If one input value is numpy.array, then output will be numpy.array.
    
        '''
        a = 0.5*(r - q - vol*vol/6)
        volG = vol/np.sqrt(3)
    
        d1 = (np.log(s/k) + (a + 0.5*volG*volG)*T) / (volG*np.sqrt(T))
        d2 = d1 - volG*np.sqrt(T)
    
        option = s*np.exp((a - r)*T)
        strike = k*np.exp(-r*T)
    
        put = max(strike*norm.cdf(-d2) - option*norm.cdf(-d1), 0)
        call = max(option*norm.cdf(d1) - strike*norm.cdf(d2), 0)
        return([call,put])
    
    @staticmethod
    def AsianArithmetic(s, k, r, T, vol, q):
        '''
        
        Calculate the Black Scholes value of Arithmetic Average Asian Call / Put
        option with a fixed strike
        Payoffs are of the form :
        C = max(AVG_arithmetic - K, 0)
        P = max(K - AVG_arithmetic, 0)
    
        Parameters
        ----------
        s : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying s
            Spot value of underlying asset at current time, t
        k : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying k
            Strike value of option, determined at initiation
        r : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying r
            Risk free interest rate, implied constant till expiration
        T : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying T
            Time till expiration for option
        vol : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying vol
            Volatility of underlying, implied constant till expiration in Black
            Scholes model
        q : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying q
            Continuous dividend payout, as a percentage
    
        Notes
        -----
        All parameters can be individual values.
        Only one of these parameters can be a numpy.array, otherwise there will be
        a dimension mismatch.
    
        * want r > q, else the natural logarithm has a chance of breaking
    
        Returns
        -------
        [call,put] : list of pair of float or numpy.array values
            Asian call and put values, type depends on input value.
            If all input values are individual numbers, then output will be float.
            If one input value is numpy.array, then output will be numpy.array.
    
        '''
        m1 = s*(np.exp((r - q)*T) - 1) / ((r - q)*T)
        m2l = 2*s*s*np.exp((2*r - 2*q + vol*vol)*T) / ((r - q +vol*vol)*T*T*(2*r - 2*q + vol*vol))
        m2r = (2*s*s / ((r-q)*T*T))*((1/(2*(r-q) + vol*vol)) -
            np.exp((r-q)*T)/(r - q - vol*vol))
        m2 = m2l + m2r
    
        volA = np.sqrt(np.log(m2/(m1*m1)) / T)
    
        d1 = (np.log(m1/k) + 0.5*volA*volA*T) / (volA*np.sqrt(T))
        d2 = d1 - volA*np.sqrt(T)
    
        call = np.exp(-r*T)*(m1*norm.cdf(d1) - k*norm.cdf(d2))
        put = np.exp(-r*T)*(k*norm.cdf(-d2) - m1*norm.cdf(-d1))
        return([call,put])
    
    @staticmethod
    def Power(s, k, r, T, vol, q, n):
        '''
        
        Calculate the Black Scholes value of a traditional Power Call / Put option
        with a fixed strike
        Payoffs are of the form :
        C = max(S**n - K, 0)
        P = max(K - S**n, 0)
    
        Parameters
        ----------
        s : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying s
            Spot value of underlying asset at current time, t
        k : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying k
            Strike value of option, determined at initiation
        r : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying r
            Risk free interest rate, implied constant till expiration
        T : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying T
            Time till expiration for option
        vol : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying vol
            Volatility of underlying, implied constant till expiration in Black
            Scholes model
        q : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying q
            Continuous dividend payout, as a percentage
        n : number of any type (int, float8, float64 etc.)
            Power to which the underlying spot is raised at payoff
    
        Notes
        -----
        All parameters can be individual values.
        Only one of these parameters can be a numpy.array (not including 'n'),
        otherwise there will be a dimension mismatch.
    
        Returns
        -------
        [call,put] : list of pair of float or numpy.array values
            Power call and put values, type depends on input value.
            If all input values are individual numbers, then output will be float.
            If one input value, other than 'n', is numpy.array, then output
            will be numpy.array.
    
        '''
        d1 = (np.log(s/np.power(k,1/n)) + (r - q + vol*vol*(n - 0.5))*T) / (vol*np.sqrt(T))
        d2 = d1 - n*vol*np.sqrt(T)
    
        option = np.exp(T*(n-1)*(r + 0.5*n*vol*vol))*np.power(s,n)
        strike = k*np.exp(-r*T)
    
        put = strike*norm.cdf(-d2) - option*norm.cdf(-d1)
        call = option*norm.cdf(d1) - strike*norm.cdf(d2)
        return([call,put])
    
    @staticmethod
    def PowerStrike(s, k, r, T, vol, q, n):
        '''
        
        Calculate the Black Scholes value of Power Call / Put option with a
        fixed strike to the power n
        Payoffs are of the form :
        C = max(S**n - K**n, 0)
        P = max(K**n - S**n, 0)
    
        Parameters
        ----------
        s : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying s
            Spot value of underlying asset at current time, t
        k : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying k
            Strike value of option, determined at initiation
        r : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying r
            Risk free interest rate, implied constant till expiration
        T : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying T
            Time till expiration for option
        vol : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying vol
            Volatility of underlying, implied constant till expiration in Black
            Scholes model
        q : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying q
            Continuous dividend payout, as a percentage
        n : number of any type (int, float8, float64 etc.)
            Power to which the underlying spot is raised at payoff
    
        Notes
        -----
        All parameters can be individual values.
        Only one of these parameters can be a numpy.array (not including 'n'),
        otherwise there will be a dimension mismatch.
    
        Returns
        -------
        [call,put] : list of pair of float or numpy.array values
            Power call and put values, type depends on input value.
            If all input values are individual numbers, then output will be float.
            If one input value, other than 'n', is numpy.array, then output
            will be numpy.array.
    
        '''
        d1 = (np.log(s/np.power(k,1/n)) + (r - q + vol*vol*(n - 0.5))*T) / (vol*np.sqrt(T))
        d2 = d1 - n*vol*np.sqrt(T)
    
        option = np.exp(T*(n-1)*(r + 0.5*n*vol*vol))*np.power(s,n)
        strike = np.power(k,n)*np.exp(-r*T)
    
        put = strike*norm.cdf(-d2) - option*norm.cdf(-d1)
        call = option*norm.cdf(d1) - strike*norm.cdf(d2)
        return([call,put])
    
    @staticmethod
    def Margrabe(s, s2, T, vol, vol2, q, q2, corr):
        '''
        
        Calculate the Black Scholes value of the Margrabe Option
        Payoff is of the form :
        O = max(S_1 - S_2, 0)
    
        Parameters
        ----------
        s1 and s2 : number of any type (int, float8, float64 etc.), numpy array of
            any type should the user wish to have a list of values output with
            varying s
            Spot value of underlying assets 1 and 2 at current time, t
        T : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying T
            Time till expiration for option
        vol1 and vol2 : number of any type (int, float8, float64 etc.), numpy array
            of any type should the user wish to have a list of values output with
            varying vol
            Volatility of underlying for assets 1 and 2, implied constant till
            expiration in Black Scholes model
        q1 and q2 : number of any type (int, float8, float64 etc.), numpy array of
            any type should the user wish to have a list of values output with
            varying q
            Continuous dividend payout for assets 1 and 2, as a percentage
        corr : number of any type (int, float8, float64 etc.), numpy array of any
            type should the user wish to have a list of values output with varying
            corr
            Correlation between the motion of the underlying (relationship between
            the Weiner process of asset 1 and 2)
    
        Notes
        -----
        All parameters can be individual values.
        At most, only one pair of these parameters can be a numpy.array,
        otherwise there will be a dimension mismatch.
    
        Returns
        -------
        price : float or numpy.array value
            Margrabe price, type depends on input value.
            If all input values are individual numbers, then output will be float.
            If one pair of input values are a numpy.array,
            then output will be numpy.array.
    
        '''
        volMix = np.sqrt(vol*vol + vol2*vol2 - vol*vol2*corr)
        d1 = (np.log(s/s2) + (q2 - q + 0.5*(volMix**2))*T) / (volMix*np.sqrt(T))
        d2 = d1 - volMix*np.sqrt(T)
    
        option = np.exp(-q*T)*s*norm.cdf(d1)
        option2 = np.exp(-q2*T)*s2*norm.cdf(d2)
    
        price = option - option2
        return(price)
    
    @staticmethod
    def Lookback(s, M, r, T, vol, q):
        '''
        
        Calculate the Black Scholes value of floating strike
        Lookback Call / Put option
        Payoffs are of the form :
        C = S_T - min(m,m_T)
        P = max(M,M_T) - S_T
        where 'm' is the current minimum, or starting strike at initiation, and
        'm_T' is the minimum over the remaining life of the option
        similarly, 'M' is the current maximum, or starting strike at initiation, and
        'M_T' is the maximum over the remaining life of the option
    
        Parameters
        ----------
        s : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying s
            Spot value of underlying asset at current time, t
        M : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying k
            Strike value of option, determined by minimum value of underlying
            over the life of the option
        r : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying r
            Risk free interest rate, implied constant till expiration
        T : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying T
            Time till expiration for option
        vol : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying vol
            Volatility of underlying, implied constant till expiration in Black
            Scholes model
        q : number of any type (int, float8, float64 etc.), numpy array of any type
            should the user wish to have a list of values output with varying q
            Continuous dividend payout, as a percentage
    
        Notes
        -----
        All parameters can be individual values.
        Only one of these parameters can be a numpy.array, otherwise there will be
        a dimension mismatch.
    
        Returns
        -------
        [call,put] : list of pair of float or numpy.array values
            Lookback call and put values, type depends on input value.
            If all input values are individual numbers, then output will be float.
            If one input value is numpy.array, then output will be numpy.array.
    
        '''
        B = 2*(r - q) / (vol*vol)
        x = (np.log(s/M) + (r - q - 0.5*vol*vol)*T) / (vol*np.sqrt(T))
        y = (-np.log(s/M) - (r - q + 0.5*vol*vol)*T) / (vol*np.sqrt(T))
    
        option = s*np.exp(-q*T)
        minimum = M*np.exp(-r*T)
        left = np.exp(-r*T)*np.power(s/M,-B)
        right = np.exp(-q*T)
    
        call = (option*norm.cdf(x + vol*np.sqrt(T)) -
            minimum*norm.cdf(x) +
            (s/B)*(left*norm.cdf(y + B*vol*np.sqrt(T)) -
                right*norm.cdf(y)))
        put = (-option*norm.cdf(-x - vol*np.sqrt(T)) +
            minimum*norm.cdf(-x) -
            (s/B)*(left*norm.cdf(-y - B*vol*np.sqrt(T)) -
                right*norm.cdf(-y)))
        return([call,put])
    


class BarrierOptions:
    '''
        
    Provides an analytical solution to barrier options using
    the Black Scholes methodology. Due to the underlying calculus'
    assumptions, the risk-free rate and implied volatility of the 
    underlying are held constant from t0 to t1.
    
    f(u) : the density function of the natural logarithm of
        the risk-neutral underlying asset return
    g(u) : the density function of the natural logarithm of
        the risk-neutral underlying asset return when the
        underlying asset price starts above/below the barrier
        crosses the barrier but ends up above/below the barrier
        at expiration
    
    The _I functions are set values used as the analytical 
    solution to the barrier options. Since a barrier option
    is marked by a set of logic conditions being met, these
    can be manipulated via an alpha and beta scalar to account
    for each barrier option's requirements. Each barrier is
    a linear combination of this set of analytical solutions.
    
    I1 - I2 : call payoff integrated over f(u) between the 
        strike and barrier
    I1 - I3 : call payoff integrated over the probability density
        of the terminal asset price conditional on NOT crossing
        the barrier
    I2 - I4 : 
    I3 : call payoff integrated over g(u) conditional on crossing
        the barrier
    I4 : call payoff integrated over the density function of
        the natural logarithm under risk-neutral assumptions 
        between the barrier and infinity
    I5 : rebate for "In" options
    I6 : reabte for "Out" options
    
    
    Parameters
    ----------
    spot : number of any type (int, float8, float64 etc.)
        Spot value of underlying asset at current time, t
    strike : number of any type (int, float8, float64 etc.)
        Strike value of option, determined at initiation
    riskfree : number of any type (int, float8, float64 etc.)
        Risk free interest rate, implied constant till expiration
    barrier : number of any type (int, float8, float64 etc.)
        Barrier value of option, determined at initiation
    tau : number of any type (int, float8, float64 etc.)
        Time till expiration for option, can be interpreted as 'T - t' should
        the option already be initiated, and be 't' time from time = 0
    vol : number of any type (int, float8, float64 etc.)
        Volatility of underlying, implied constant till expiration in Black
        Scholes model
    div : number of any type (int, float8, float64 etc.)
        Continuous dividend payout, as a percentage
    rebate : number of any type (int, float8, float64 etc.)
        Rebate of barrier option, if there is no rebate provision, set = 0
        Default value is 0
        
    '''
    def __init__(self, spot, strike, riskfree, barrier, tau, vol, div, rebate=0):
        self.s = spot
        self.k = strike
        self.r = riskfree
        self.Z = barrier
        self.T = tau
        self.vol = vol
        self.q = div
        self.R = rebate
        
        self.L = self._lambdaDrift()


    def _lambdaDrift(self):
        '''
        
        Lambda constant calculated from the risk-netural
        drift of the underlying

        Returns
        -------
        l : float
            The lambda constant used in each of barrier option
            analytical solutions

        '''
        m = self._mu()
        l = 1 + (m / (self.vol*self.vol))
        return(l)
    
    
    def _mu(self):
        '''
        
        The underlying's risk-netural drift term,
        referred to as 'Mu'

        Returns
        -------
        mu : float
            The drift term used in the barrier option
            analytical solutions

        '''
        mu = (self.r - self.q - self.vol*self.vol*0.5)
        return(mu)


    def _x1val(self):
        x = np.log(self.s / self.Z) / (self.vol*np.sqrt(self.T)) + self.L*self.vol*np.sqrt(self.T)
        return(x)
    
    def _xval(self):
        x = np.log(self.s / self.k) / (self.vol*np.sqrt(self.T)) + self.L*self.vol*np.sqrt(self.T)
        return(x)
    
    def _y1val(self):
        y = np.log(self.Z / self.s) / (self.vol*np.sqrt(self.T)) + self.L*self.vol*np.sqrt(self.T)
        return(y)
    
    def _yval(self):
        y = np.log(np.square(self.Z) / (self.s*self.k)) / (self.vol*np.sqrt(self.T)) + self.L*self.vol*np.sqrt(self.T)
        return(y)
    
    def _zval(self):
        z = np.log(self.Z / self.s) / (self.vol*np.sqrt(self.T)) + self._bval()*self.vol*np.sqrt(self.T)
        return(z)

    def _aval(self):
        a = self._mu() / (self.vol*self.vol)
        return(a)
    
    def _bval(self):
        b = np.sqrt(self._mu()**2 + 2*self.r*self.vol*self.vol) / (self.vol*self.vol)
        return(b)


    def _I1(self, alpha : int, beta : int):
        '''
        
        Parameters
        ----------
        alpha : int
            Scalar to represent either a call or put
        beta : int
            Scalar to represent whether the asset price
            starts above or below the barrier

        Returns
        -------
        partial : float
            The I1 partial analytical solution for the barrier option
            
        '''
        xval = self._xval()
        partial = alpha*self.s*norm.cdf(alpha*xval) - alpha*self.k*np.exp(-1*self.r*self.T)*norm.cdf(alpha*xval - alpha*self.vol*np.sqrt(self.T))
        return(partial)


    def _I2(self, alpha : int, beta : int):
        '''
        
        Parameters
        ----------
        alpha : int
            Scalar to represent either a call or put
        beta : int
            Scalar to represent whether the asset price
            starts above or below the barrier

        Returns
        -------
        partial : float
            The I2 partial analytical solution for the barrier option
            
        '''
        xval = self._x1val()
        partial = alpha*self.s*norm.cdf(alpha*xval) - alpha*self.k*np.exp(-1*self.r*self.T)*norm.cdf(alpha*xval - alpha*self.vol*np.sqrt(self.T))
        return(partial)
    
    
    def _I3(self, alpha : int, beta : int):
        '''
        
        Parameters
        ----------
        alpha : int
            Scalar to represent either a call or put
        beta : int
            Scalar to represent whether the asset price
            starts above or below the barrier

        Returns
        -------
        partial : float
            The I3 partial analytical solution for the barrier option
            
        '''
        yval = self._yval()
        partial = alpha*self.s*np.power(self.Z / self.s, 2*self.L)*norm.cdf(beta*yval) - \
            alpha*self.k*np.exp(-1*self.r*self.T)*np.power(self.Z / self.s, 2*self.L - 2)*norm.cdf(beta*yval - beta*self.vol*np.sqrt(self.T))
        return(partial)
    
    
    def _I4(self, alpha : int, beta : int):
        '''

        Parameters
        ----------
        alpha : int
            Scalar to represent either a call or put
        beta : int
            Scalar to represent whether the asset price
            starts above or below the barrier

        Returns
        -------
        partial : float
            The I4 partial analytical solution for the barrier option
            
        '''
        yval = self._y1val()
        partial = alpha*self.s*np.power(self.Z / self.s, 2*self.L)*norm.cdf(beta*yval) - \
            alpha*self.k*np.exp(-1*self.r*self.T)*np.power(self.Z / self.s, 2*self.L - 2)*norm.cdf(beta*yval - beta*self.vol*np.sqrt(self.T))
        return(partial)
    
    
    def _I5(self, beta : int):
        x = self._x1val()
        y = self._y1val()
        partial = self.R*np.exp(-1*self.r*self.T) * \
            (norm.cdf(beta*x - beta*self.vol*np.sqrt(self.T)) - \
             np.power(self.Z / self.s, 2*self.L - 2)*norm.cdf(beta*y - beta*self.vol*np.sqrt(self.T)))
        return(partial)
    
    
    def _I6(self, beta : int):
        a = self._aval()
        b = self._bval()
        z = self._zval()
        partial = self.R * (np.power(self.Z / self.s, a - b)*norm.cdf(beta*z) - \
                            np.power(self.Z / self.s, a - b)*norm.cdf(beta*z - 2*beta*b*self.vol*np.sqrt(self.T)))
        return(partial)



    def DownOutPut(self):
        '''
        
        Calculate the Down-and-Out PUT option
    
        Returns
        -------
        price : float
            Price value of barrier option. 
    
        '''
        a = -1
        b = 1
        
        if self.k > self.Z and self.s >= self.Z:
            price = self._I1(a,b) - self._I2(a,b) + self._I3(a,b) - self._I4(a,b) + self._I6(b)
        elif self.k < self.Z and self.s >= self.Z:
            price = self._I6(b)
        else:
            price = 0.0
        return(max(price, 0.0))
    
    
    def DownOutCall(self):
        '''
        
        Calculate the Down-and-Out CALL option, for any barrier
    
        Returns
        -------
        price : float
            Price value of barrier option.
    
        '''
        a = 1
        b = 1
    
        if self.k > self.Z and self.s >= self.Z:
            price = self._I1(a,b) - self._I3(a,b) + self._I6(b)
        elif self.k < self.Z and self.s >= self.Z:
            price = self._I2(a,b) - self._I4(a,b) + self._I6(b)
        else:
            price = 0.0
        return(max(price, 0.0))
    
    
    def UpOutCall(self):
        '''
        
        Calculate the Up-and-Out CALL option
    
        Returns
        -------
        price : float
            Price value of barrier option.
    
        '''
        a = 1
        b = -1
        
        if self.k > self.Z and self.s <= self.Z:
            price = self._I1(a,b) - self._I2(a,b) + self._I3(a,b) - self._I4(a,b) + self._I6(b)
        elif self.k < self.Z and self.s <= self.Z:
            price = self._I6(b)
        else:
            price = 0.0
        return(max(price, 0.0))
    
    
    def UpOutPut(self):
        '''
        
        Calculate the Up-and-Out PUT option
    
        Returns
        -------
        price : float
            Price value of barrier option.

        '''
        a = -1
        b = -1
    
        if self.k < self.Z and self.s <= self.Z:
            price = self._I1(a,b) - self._I3(a,b) + self._I6(b)
        elif self.k > self.Z and self.s <= self.Z:
            price = self._I2(a,b) - self._I4(a,b) + self._I6(b)
        else:
            price = 0.0
        return(max(price, 0.0))
    
    
    def DownInCall(self):
        '''
        
        Calculate the Down-and-In CALL option
    
        Returns
        -------
        price : float
            Price value of barrier option.

        '''
        a = 1
        b = 1
    
        if self.k > self.Z:
            price = self._I3(a,b) + self._I5(b)
        elif self.k < self.Z:
            price = self._I1(a,b) - self._I2(a,b) + self._I4(a,b) + self._I5(b)
        else:
            price = 0.0
        return(max(price, 0.0))
    
    
    def DownInPut(self):
        '''
        
        Calculate the Down-and-In PUT option
    
        Returns
        -------
        price : float
            Price value of barrier option.
    
        '''
        a = -1
        b = 1
    
        if self.k > self.Z:
            price = self._I2(a,b) - self._I3(a,b) + self._I4(a,b) + self._I5(b)
        elif self.k < self.Z:
            price = self._I1(a,b) + self._I5(b)
        else:
            price = 0.0
        return(max(price, 0.0))
    
    
    def UpInCall(self):
        '''
        
        Calculate the Up-and-In Call option
    
        Returns
        -------
        price : float
            Price value of barrier option.
    
        '''
        a = 1
        b = -1
    
        if self.k > self.Z:
            price = self._I1(a,b) + self._I5(b)
        elif self.k < self.Z:
            price = self._I2(a,b) - self._I3(a,b) + self._I4(a,b) + self._I5(b)
        else:
            price = 0.0
        return(max(price, 0.0))
    
    
    def UpInPut(self):
        '''
        
        Calculate the Up-and-In Put option
    
        Returns
        -------
        price : float
            Price value of barrier option.
    
        '''
        a = -1
        b = -1
    
        if self.k > self.Z:
            price = self._I1(a,b) - self._I2(a,b) + self._I4(a,b) + self._I5(b)
        elif self.k < self.Z:
            price = self._I3(a,b) + self._I5(b)
        else:
            price = 0.0
        return(max(price, 0.0))



if __name__ == '__main__':
    opt1 = [1, 2, 0.02, 1.5, 5, 0.05, 0.01, 0.01]
    bro = BarrierOptions(*opt1)
    a = bro.DownInCall()