### ■ Greeks
CALL/Option Price
#### Price
- Delta: has the biggest impact on an option's value. It identifies how much the options premium may change, if the underlying price changes $1.00.
It could also be interpreted as the probability of expiring ITM, e.g. Delta .40 (40% probability of expiring ITM). Lower the Delta, lower probability the option will expire ITM.
One important thing to note about Delta, is that it doesn't have a constant rate of change. It grows as an option moves further ITM, and shringks as it moves furhter OTM. To understand how this works, please refer to Gamma.
- Gamma: Gamma measures Delta's expected rate of change. If an option has a Delta of 0.40, and a Gamma of 0.05, the premium will expect to change $0.40 with the first dollar move in the underlying. Then to figure out the impact of the next dollar move, Simply add Delta and Gamma together, e.g. $1.40 ($1.00 + $0.4 = $1.40), $1.85 ($1.40 + $0.45 = $1.85)

#### Time
- Theta: Time decay. Theta estimates how much value slips away from an option with each passing day. If an option has a Theta of negative 0.04, it would be expected to lose $0.04 of value every day. Time decay works against buyers and for sellers.

#### Implied Volatility
- Vega: Vega estimates how much the premium may change with each one percentage point change in impolied volatility. If an option has a Vega 0.03 and implied volatility decreases one percentage point, the premium will be expected to drop $0.03. There are a lot of factors that could cause a spike in implied volatility, e.g. earning announcements, political conditions, and even weather. And the further out an option's expiration is, the higher its Vega will be. In other words, options with a longer expiration may react more to a change in the volatility.
 
 ### ■ Notes
Implied volatility changes will also have an effect on Gamma. As implied volatility decreases, Gamma of ATM calls and puts increases. When implied volatility goes higher, the Gamma of both ITM and OTM calls and puts will be decreasing. This occurs because low implied volatility options will have a more dramatic change in Delta when the underlying moves. A high implied volatility underlying product will see less of a Delta change with movement as the possibility of more movements is foreseen.
![alt tag](/image/the_greeks.jpg)
