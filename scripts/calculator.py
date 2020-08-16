
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
        