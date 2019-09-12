# -*- coding: utf-8 -*-
# @Author: boyac
# @Date:   2016-04-27 19:12:48
# @Last Modified by:   boyac
# @Last Modified time: 2016-05-15 00:49:14

from random import *
from math import exp, sqrt

def generate_asset_price(S,v,r,T):
	return S * exp((r - 0.5 * v**2) * T + v * sqrt(T) * gauss(0,1.0))

def call_payoff(S_T,K):
	return max(0.0, S_T-K) # (S_T - K) = Intrinsic value for call

def monte_carlo(simulations):
	payoffs = []
	discount_factor = exp(-r * T)

	for i in xrange(simulations):
		S_T = generate_asset_price(S,v,r,T)
		payoffs.append(call_payoff(S_T,K))

	price = discount_factor * (sum(payoffs) / float(simulations))
	return 'Price: %.4f' % price


if __name__ == '__main__':
	S = 761.68
	K = 680
	t = 1.1479
	r = 0.04
	v = 0.3232
	print monte_carlo(100000)
	# read more about Monte_Carlo on investment: http://wiki.mbalib.com/wiki/%E8%92%99%E7%89%B9%E5%8D%A1%E7%BD%97%E6%96%B9%E6%B3%95
