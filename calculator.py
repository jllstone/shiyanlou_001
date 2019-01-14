#!/usr/bin/env python3
import sys

def cal_tax(salary):
    tax_salary = salary * (1 - 0.165) - 3500
    if tax_salary < 0:
        tax = 0
    elif tax_salary < 1500:
        tax = tax_salary * 0.03 
    elif tax_salary < 4500:
        tax = tax_salary * 0.10 - 105
    elif tax_salary < 9000:
        tax = tax_salary * 0.20 - 555
    elif tax_salary < 35000:
        tax = tax_salary * 0.25 - 1005
    elif tax_salary < 55000:
        tax = tax_salary * 0.30 - 2755
    elif tax_salary < 80000:
        tax = tax_salary * 0.35 - 5505
    else:
        tax = tax_salary * 0.45 - 13505
    return salary * 0.835 - tax

if __name__ == '__main__' :
    try:
        for i in sys.argv[1:]:
            id, salary = i.split(':')
            print('{}:{:.2f}'.format(id, cal_tax(int(salary))))
    except ValueError:
        print('Parameter Error')
