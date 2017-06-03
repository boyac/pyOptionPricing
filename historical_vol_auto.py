from pandas import np
import pandas_datareader.data as web
import threading

def hv(sym, days):
    """
    Return the annualized stddev of daily log returns of picked stock,
    and auto refresh data loading every 5 seconds.
    """
    try:
    	# past number of 'days' close price data, normally between (30, 60)
        hv.quotes = web.DataReader(sym, 'yahoo')['Close'][-days:]     
    except Exception, e:
        print "Error getting data for symbol '{}'.\n".format(sym), e
        return None, None
    logreturns = np.log(hv.quotes / hv.quotes.shift(1))
    # return square root * trading days * logreturns variance
    # NYSE 252 trading days, Shanghai Stock Exchange = 242, Tokyo Stock Exchange = 246 days?
    return np.sqrt(252*logreturns.var()) 
    
if __name__ == "__main__":
    print hv('FB', 30) # facebook/ 0.294282265956
    threading.Timer(5, hv.quotes).start()
   
   
# [BUG]Cannot read Time Series data
""" 
Exception in thread Thread-1:
Traceback (most recent call last):
  File "/usr/local/Cellar/python/2.7.11/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py", line 801, in __bootstrap_inner
    self.run()
  File "/usr/local/Cellar/python/2.7.11/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py", line 1073, in run
    self.function(*self.args, **self.kwargs)
TypeError: 'Series' object is not callable
"""
