# -*- coding: utf-8 -*-
# @Author: boyac
# @Date:   2016-05-02 18:28:28
# @Last Modified by:   boyac
# @Last Modified time: 2016-05-04 00:27:52

from scipy.stats import norm
from math import *

# Cumulative normal distribution
def CND(X):
    return norm.cdf(X)

# Black Sholes Function
def BlackScholes(CallPutFlag,S,K,t,r,s):
    """
    S = Current stock price
    t = Time until option exercise (years to maturity)
    K = Option striking price
    r = Risk-free interest rate
    N = Cumulative standard normal distribution
    e = Exponential term
    s = Variance(volitility)
    Ln = NaturalLog
    """
    d1 = (log(S/K)+(r+(s**2)/2)*t)/(sqrt(s*t))
    d2 = d1-sqrt(s*t)

    if CallPutFlag=='c':
        return S*CND(d1)-K*exp(-r*t)*CND(d2) # call option
    else:
        return K*exp(-r*t)*CND(-d2)-S*CND(-d1) # put option 


if __name__ == "__main__":
    # Number taken from: http://wiki.mbalib.com/wiki/Black-Scholes期权定价模型
    print BlackScholes('c', 164.0, 165.0, 0.0959, 0.0521, 0.0841) # 5.788529972549341
