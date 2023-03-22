from classes.employee import Employee
from commons.conversions import str_to_date
from commons.brules import calc_bonus

# Open the file in the respective mode

emp_file = open('input\employee.csv')
benefits = open(r'output\benefits.csv', 'w')

# read the records
for emp in emp_file:
    name, ID, DOJ, email, salary = emp.split(sep = ',')
    empo = Employee(name, ID, DOJ, int(salary))
    
    # Convert the date from string to datetime format
    
    DOJ  = str_to_date(DOJ)
    
    # Calculate bonus
    bonus = calc_bonus(DOJ)
    print(emp, bonus)
    
    # Set bonus
    empo.set_bonus(bonus)
    
    # Write to the file
    benefits.write(str(empo) + '\n')
    
benefits.close()