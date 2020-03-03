# -*- coding: utf-8 -*-
# @Author: boyac
# @Date:   2016-05-08 23:03:49
# @Last Modified by:   boyac
# @Last Modified time: 2016-05-08 23:54:21

import numpy as np
import random

def Money(num_sims, num_participants):
	"""
	This is the rewritten code of simulations from: 
	https://www.quora.com/How-can-I-win-a-stock-market-competition-in-1-month-from-scratch
	- We have 100 participants other than you
	- You pick 1 stock that has 70% chance of going bankrupt and 30% chance of jumping 100%
	- Other pick from the universe of stocks with 25%' volatility and 10%' average return. (# strong assumption)
	"""
	i_won = []	# array to store outcomes
	for sim in range(0, num_sims):	# for every simulation
		stock_returns = np.random.randn(num_participants) * 0.25 + 0.1
		best_return = max(stock_returns)
		my_return = 1 if np.random.rand() > 0.7 else -1 # a binary outcome for your stock: either win or lose
		i_won.append(1 if my_return > best_return else 0)

	win_prop = np.array(i_won).mean()
	std_err = 1.96 * np.sqrt(win_prop * (1-win_prop) / num_sims)
	upper = win_prop + std_err
	lower = win_prop - std_err
	return 'Win Probability (Upper): {:.5f} | Win Probability (Lower): {:.5f}'.format(upper, lower)


if __name__ == '__main__':
	num_sims = 10000 			# number of simuations
	num_participants = 100 			# number of participants
	print Money(num_sims, num_participants) # Win Probability (Upper): 0.31120 | Win Probability (Lower): 0.29320
	
	"""
	# a stock has 70% chance of going bankrupt and 30% chance of jumping 100%
	# question arises of how do you determine the 30/70 percent chances ratio?
	# I got stuck, if it follows a normal distribution and implied Vol 1 (= 100%),
	# 1 std, about 70% (actually 68%) confidence interval of bankrupt or double the original investment.
	# another 30% chance of either go -0 or more than double the orgional investment? 
	# Still couldn't get where 30／70 ratio come from, is it a skewed dataset? 
	# Besides, 'stock_returns' uses np.random.randn(normal distribution)
	"""
