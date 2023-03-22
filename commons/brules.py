# Bonus Calculations by comparing today's date with
# date of joing

from datetime import timedelta, date

def calc_bonus(DOJ):
    # $5000 - 10 Years
    # $2000 - 5  Years
    today = date.today()
    
    one_year = timedelta(days=365) # Create delta of 1 year
    five_year = one_year * 5
    ten_year = one_year * 10
    
    difference = today - DOJ
    
    if difference >= ten_year:
        bonus = 5000.0
    elif difference >= five_year:
        bonus = 2000        
    else:
        bonus = 0.0
    return bonus
