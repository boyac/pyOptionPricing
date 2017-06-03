# -*- coding: utf-8 -*-
# @Author: boyac
# @Date:   2016-05-22 16:12:29
# @Last Modified by:   boyac
# @Last Modified time: 2016-05-22 16:12:29


from math import *

def Binomial(S,K,u,d,r,T): # One-Step Binomial Pricing
    """
    S = Current stock price
    K = Option striking price
    u = Size of magnitude of up-jump / upstep 
    d = Size of magnitude of down-jump / downstep
    T = Time until option excercise (years to maturity)
    r = Risk-free interest rate

    * u, d can be calculated by volatility assumption
    """
    
    discount = exp(-r*T)
    delta_s = 1 / (S*u - S*d)
    portfolio = (S*d) * delta_s
    pv = portfolio * discount # portfolio present value
    option_price = (S * delta_s) - pv
    return option_price


if __name__ == "__main__":
    print Binomial(20, 21, 1.1, 0.9, 0.12, 0.25) # 0.632995099032
    print Binomial(164.0, 165.0, 1.1, 0.9, 0.0521, 0.0959) # 0.522427679626
