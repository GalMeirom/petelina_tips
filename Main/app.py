#This the main page where everythng is gonna run

from employees import Waiter, Bartender
from Main.shift import Shift
from Main.utilities import intro, waiters_input, bartenders_input, add_hour, cal_money_emp, shift_report

if __name__ == "__main__":
    num_bartenders = 0
    s = Shift()
    l_employees_data = []
    l_employees = []
    intro()
    s.shift_input()
    waiters_input(l_employees_data)
    bartenders_input(l_employees_data)
    for person in l_employees_data:
        if person[1] != 0:
            waiter = Waiter(person[0],person[1])
            l_employees.append(waiter)
        else:
            bartender = Bartender(person[0],person[1])
            l_employees.append(bartender)
            num_bartenders += 1
    s.total_hours = add_hour(l_employees,s.total_hours)
    s.bar_provision(num_bartenders)
    s.cal_per_hours()
    cal_money_emp(l_employees,s.cash_per_hour,s.credit_per_hour,s.cash_bar,num_bartenders)
    shift_report(l_employees,s.cash_per_hour,s.credit_per_hour)