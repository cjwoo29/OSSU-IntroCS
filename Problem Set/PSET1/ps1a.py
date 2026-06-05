## 6.100A PSet 1: Part A

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))


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
    months += 1
    amount_saved += amount_saved * (r/12) + yearly_salary/12*portion_saved
print("Number of months:", months)
