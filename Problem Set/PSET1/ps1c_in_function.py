def part_c(initial_deposit):
	#########################################################################
	# Write a program to calculate the minimum rate of return r needed in oreder to reach your goal of a sufficient down payment in 3 years, give an initial_deposit.
	# We should save $200,000 ($800,000 * 25%) for paying down payment.
	goal = 200000.
	steps = 0
	low, high = 0., 1.
	r = 0.
	epsilon = 100. # dollars
	def amount_saved(init, rate):
	    return init*((1+rate/12)**36)
	##################################################################################################
	## Determine the lowest rate of return needed to get the down payment for your dream home below ##
	##################################################################################################
	if not amount_saved(initial_deposit, 1) < goal:
	    while abs(amount_saved(initial_deposit, r) - goal) > epsilon:
	        steps+=1
	        if amount_saved(initial_deposit, r) < goal: # rate should be raised
	            low = r
	        else:
	            high = r
	        r = (low+high)/2.0
	else:
	    r = None
	
	print("Best saving rate:", r)
	print("Steps in bisection search:",steps)
	return r, steps