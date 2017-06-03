from pandas import np
import pandas_datareader.data as web

def historical_volatility(sym, days): # stock symbol, number of days
    "Return the annualized stddev of daily log returns of picked stock"
    try:
        # past number of 'days' close price data, normally between (30, 60)
        quotes = web.DataReader(sym, 'yahoo')['Close'][-days:] 
    except Exception, e:
        print "Error getting data for symbol '{}'.\n".format(sym), e
        return None, None
    logreturns = np.log(quotes / quotes.shift(1))
    # return square root * trading days * logreturns variance
    # NYSE = 252 trading days; Shanghai Stock Exchange = 242; Tokyo Stock Exchange = 246 days?
    return np.sqrt(252*logreturns.var()) 
    
    
if __name__ == "__main__":
    print historical_volatility('FB', 30) # facebook
