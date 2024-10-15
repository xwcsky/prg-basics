###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0

bonus = 0.15 # 15%

decision = input("Do you like your employee Y/N ")
if decision == "Y":
    is_bonus = True # does the employee receive a bonus
elif decision == "N":
    is_bonus = False # does the employee receive a bonus

if is_bonus:
    total_salary = basic_salary*bonus + basic_salary
else:
    total_salary = basic_salary

    

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')