def part_a(yearly_salary, portion_saved, cost_of_dream_home):
	#########################################################################
	portion_down_payment = 0.25
	amount_saved = 0.0
	r = 0.05 # At the end of each month, receive an addtional ```amount_saved * (r/12)```
	months = 0
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	while cost_of_dream_home*portion_down_payment > amount_saved:
	    months += 1
	    amount_saved += amount_saved * (r/12) + yearly_salary/12*portion_saved
	print("Number of months:", months)
	return months