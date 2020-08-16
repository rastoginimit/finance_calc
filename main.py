import json
from scripts.calculator import Calculator

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