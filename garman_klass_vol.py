# -*- coding: utf-8 -*-
# @Author: boyac
# @Date:   2016-05-02 18:28:28
# @Last Modified by:   boyac
# @Last Modified time: 2016-05-02 19:09:29

from pandas import np
import pandas_datareader.data as web


def gk_vol(sym, days):
    """"
    Return the annualized stddev of daily log returns of picked stock
    Historical Open-High-Low-Close Volatility: Garman Klass
    sigma**2 = ((h-l)**2)/2 - (2ln(2) - 1)(c-o)**2
    ref: http://www.wilmottwiki.com/wiki/index.php?title=Volatility
    """

    try:
    	o = web.DataReader(sym, 'yahoo')['Open'][-days:] 
    	h = web.DataReader(sym, 'yahoo')['High'][-days:] 
    	l = web.DataReader(sym, 'yahoo')['Low'][-days:] 
        c = web.DataReader(sym, 'yahoo')['Close'][-days:]
    except Exception, e:
        print "Error getting data for symbol '{}'.\n".format(sym), e
        return None, None
    sigma = np.sqrt(252*sum((np.log(h/l))**2/2 - (2*np.log(2)-1)*(np.log(c/o)**2))/days)
    return sigma
    
    
if __name__ == "__main__":
    print gk_vol('FB', 30) # facebook
