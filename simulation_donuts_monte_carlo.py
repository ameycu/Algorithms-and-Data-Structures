
"""
In a donuts shop, number of customer per day can be as follows:
2 with prob of 0.32
4 with prob of 0.3
6 with prob of 0.25
8 with reamining prob

Each customer can order 1,2,3 or 4 donuts (randomly)

profit per donut sold is $1

excess donuts cause loss of $0.5 per donut

Find optimal number of donuts to be made using monte carlo simulation
"""

import math as m
import random as r
import numpy as n

def demand_per_day():
	order_choice = [1,2,3,4] #customers can order either of these qtys

	def num_cus(p): #Number of customers can be 2,4,6 or 8 based on probaility p
		if p < 0.35: return 2
		if p < 0.35+0.3: return 4
		if p < 0.35+0.3+0.25: return 6
		else: return 8

	demand_each_customer = []

	for i in range(8):
		demand_each_customer.append(r.choice(order_choice))

	random_number = r.random()

	num_customers = num_cus(random_number)

	demand = 0

	for i in range(num_customers):
		demand += demand_each_customer[i]
	"""
	print 'demand for each customer = ',demand_each_customer
	print 'random num = ',random_number
	print 'number of customers for that day = ',num_customers
	print 'demand for that day',demand
	"""
	return demand

manufacture_amount_choice = range(1,15)

def profit(manufacture_amount):
	profit_val = 0
	for i in range(100000):
		demand = demand_per_day()

		excess = manufacture_amount-demand

		if excess<=0:
			profit_val += demand
		else:
			profit_val += demand - 0.5*(excess)
	return profit_val

for i in manufacture_amount_choice:
	print 'Profit for manufacture_amount = ',i,' profit = ',profit(i)
