## 6.100A PSet 1: Part B
# We will build on your solution to Part A by adding a salary raise every six months
##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal:")) # Additional user input in Part B

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25
amount_saved = 0.0
r = 0.05 # At the end of each month, receive an addtional ```amount_saved * (r/12)```
months = 0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
while cost_of_dream_home*portion_down_payment > amount_saved:
    amount_saved += amount_saved * (r/12) + yearly_salary/12*portion_saved
    months += 1
    if months % 6 == 0: # raise
        yearly_salary *= (1 + semi_annual_raise)
print("Number of months:", months)
