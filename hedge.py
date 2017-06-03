# -*- coding: utf-8 -*-
import math

class Hedge:
	def __init__(self):
		pass

	def ratio(self,S,K,u,d,r):
		self.S = S # current stock price
		self.K = K # strike price
		self.u = u # stock up price
		self.d = d # stock down price
		self.r = r # risk free interest rate

		self.c_price_u = self.u - self.K
		self.c_price_d = self.d - self.K
		
		if (self.c_price_d < 0):
			self.c_price_d = 0
		
		hedge_ratio = (self.c_price_u - self.c_price_d) / (self.u - self.d) # size of exporsure / size of position in the future
		return hedge_ratio
		
	# resize proportion
	def hedge_ratio_proportion(self,ratio):
	    multiplier = 1 / ratio
	    prop_value = multiplier
	    v_u = self.u -  prop_value * self.c_price_u
	    v_d = self.d - prop_value * self.c_price_d

	    if v_u!=v_d:
	    	print 'Arbitrage Exist!'
	    else:
	    	print 'NO Arbitrage Opportunity!'
	# work on this a bit more; need to check other documents
		c = (self.S- v_u / self.r) / prop_value
	# / (risk-free interest rate) 
		print "Call price is {}".format(c)


if __name__ == "__main__":
	h = Hedge()
	r = h.ratio(100,30,125,75,.05)
	print h.hedge_ratio_proportion(r)

	# NO Arbitrage Opportunity!
	# Call price is -500.0
