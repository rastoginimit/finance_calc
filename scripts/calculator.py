import numpy as np 
import math 
class Calculator:
    def __init__(self):
        super().__init__()
    def calc_income_tax(self, before_tax_income, tax_slabs):
        prev_slab_tax = 0.00
        for slab in tax_slabs:
            if before_tax_income > slab["slab_start"] and before_tax_income <= slab["slab_end"]:
                tax = prev_slab_tax + (before_tax_income - slab["slab_start"])*slab["tax_pct"]/100.00
                tax = round(tax,2)
                return tax
            if slab["slab_start"] != tax_slabs[-1]["slab_start"]:
                prev_slab_tax = prev_slab_tax + (slab["slab_end"] - slab["slab_start"])*slab["tax_pct"]/100.00
        tax = prev_slab_tax + (before_tax_income - tax_slabs[-1]["slab_start"])*tax_slabs[-1]["tax_pct"]/100.00
        tax = round(tax,2)
        return tax
    
    def generate_rev_tax_slabs(self, tax_slabs):
        rev_tax_slabs = list()
        prev_slab_tax = 0.00
        for slab in tax_slabs:
            rev_slab = dict()
            rev_slab["div_factor"] = 100.00 - slab["tax_pct"]
            rev_slab["sub_factor"] = slab["slab_start"] * slab["tax_pct"]/100.00 - prev_slab_tax
            rev_slab["slab_start"] = slab["slab_start"] * rev_slab["div_factor"]/100.00 + rev_slab["sub_factor"]
            rev_slab["slab_end"]   = slab["slab_end"]   * rev_slab["div_factor"]/100.00 + rev_slab["sub_factor"]
            rev_tax_slabs.append(rev_slab)
            prev_slab_tax = prev_slab_tax + (slab["slab_end"] - slab["slab_start"])*slab["tax_pct"]/100.00
        return rev_tax_slabs
    
    def calc_before_tax_income(self, after_tax_income, tax_slabs):
        rev_tax_slabs = self.generate_rev_tax_slabs(tax_slabs)
        for slab in rev_tax_slabs:
            if after_tax_income > slab["slab_start"] and after_tax_income <= slab["slab_end"] :
                before_tax_income=(after_tax_income-slab["sub_factor"])*100.00/slab["div_factor"]
                before_tax_income=round(before_tax_income,2)
                return before_tax_income
        before_tax_income=(after_tax_income-rev_tax_slabs[-1]["sub_factor"])*100.00/rev_tax_slabs[-1]["div_factor"]
        before_tax_income=round(before_tax_income,2)
        return before_tax_income

    def calc_cc_min_repayment(self, closing_balance, pct, min_amount):
        return max([min_amount, math.ceil(closing_balance*pct/100)])
    
    def calc_months_to_payoff(self, rate, pmt, closing_balance):
        nper = np.nper(rate/12/100.00, pmt, closing_balance)
        return nper
    def calc_cc_monthly_pmt(self, rate, months, closing_balance):
        pmt = -np.pmt(rate/12/100.00, 24, closing_balance)
        return pmt
    def calc_total_interest(self, rate, closing_balance, pmt, nper):
        per = np.arange(nper) + 1
        ipmt = -np.ipmt(rate/12/100.00, per, nper, closing_balance)
        totalinterest = np.sum(ipmt)
        totalinterest = round(totalinterest, 2)
        return totalinterest

class Formatter:
    def format_months(self, months):
        months = math.ceil(months)
        years=math.floor(months/12)
        remaining_months = months - (years*12)
        if (years == 0):
            formatted_years = ""
            formatted_months = str(remaining_months) + " Months"
        else:
            formatted_years = str(years) + " Years"
            if (remaining_months == 0):
                formatted_months = ""
            else:
                formatted_months = " and " + str(remaining_months) + " Months"
        return formatted_years + formatted_months
