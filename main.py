import json
from scripts.calculator import *

'''
#Calculating Income Tax
before_tax_income = input("Enter your gross income, before tax: ")
before_tax_income = float(before_tax_income)
with open('input/tax_slabs.json') as tax_slabs_file:
    tax_slabs = json.load(tax_slabs_file)
    tax_slabs = tax_slabs["tax_slabs"]
calc = Calculator()
iTax = calc.calc_income_tax(before_tax_income, tax_slabs)
print("Tax on income is:", iTax)
medicare_levy = 0.00
if (before_tax_income > tax_slabs[0]['slab_end']):
    medicare_levy = 0.02*before_tax_income
print("Medicare Levy is:", medicare_levy)
print("Total Tax:", iTax + medicare_levy)
print("Note: Total Tax above does not include the tax offset you might be eligible for")
'''

'''
#Credit card repayments calculations
calc = Calculator()
form = Formatter()
closing_balance = input('Enter the closing balance: ')
closing_balance = float(closing_balance)
min_pmt_pct = input("Enter percentage for minimum repayment:")
min_pmt_pct = float(min_pmt_pct)
min_amount = input("Enter the minimum amount for the repayment:")
min_amount = float(min_amount)

cc_interest_rate = input("Enter your credit card's interest rate:")
cc_interest_rate = float(cc_interest_rate)

min_pmt = calc.calc_cc_min_repayment(closing_balance, min_pmt_pct, min_amount)
print("Your monthly minimum repayment would be:", min_pmt)

months = calc.calc_months_to_payoff(cc_interest_rate, min_pmt*-1, closing_balance)
print("Time to pay off the closing balance using minimum repayment:", form.format_months(months))

total_interest = calc.calc_total_interest(cc_interest_rate, closing_balance, min_pmt, months)
print("Total interest, if only minimum repayments paid:", total_interest)

max_months = 24
if (months>max_months):
    pmt=calc.calc_cc_monthly_pmt(cc_interest_rate, 12, closing_balance)
    pmt = round(pmt, 2)
    print("To payoff in", max_months, "months, the monthly payment needed is:", pmt)
    total_interest_new = calc.calc_total_interest(cc_interest_rate, closing_balance, pmt, max_months)
    print("Total interest if this new amount is paid each month:", total_interest_new)
    print("Total saving in interest:", round(total_interest - total_interest_new, 2))
'''
after_tax_income = input("Enter the income, you want to receive after tax: ")
after_tax_income = float(after_tax_income)
with open('input/tax_slabs.json') as tax_slabs_file:
    tax_slabs = json.load(tax_slabs_file)
    tax_slabs = tax_slabs["tax_slabs"]
calc = Calculator()
pre_tax_income = calc.calc_before_tax_income(after_tax_income, tax_slabs)

print("Your gross income before tax should be:", pre_tax_income)
