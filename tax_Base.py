


def calculate_tax(
    income: float,
) -> dict:

    #TAX_BRACKETS = [
    #    (0, 10908, lambda x: 0.0),  # No tax below €10,908
    #    (10909, 15999, lambda x: (x - 10908) * 0.14),  # 14% marginal rate
    #    (16000, 62809, lambda x: 2397 + (x - 15999) * 0.42),  # Progressive up to 42%
    #    (62810, float('inf'), lambda x: 2397 + (62809 - 15999) * 0.42 + (x - 62809) * 0.45),  # 45% marginal rate
    #]
#
    #TAX_BRACKETS = [
    #    (0, 10908, lambda x: 0.0),  # No tax for income below €10,908
    #    (10909, 15999, lambda x: (x - 10908) * 0.14),  # 14% for income above €10,908
    #    (16000, 62809, lambda x: 2397 + (x - 15999) * 0.24),  # Progressive 24%
    #    (62810, 277825, lambda x: 16497.36 + (x - 62809) * 0.42),  # 42% for income in this range
    #    (277826, 350000, lambda x: 93353.36 + (x - 277825) * 0.42),  # Flat 42% for high earners
    #    (350001, float('inf'), lambda x: 124394.36 + (x - 350000) * 0.45),  # 45% for the top tier
    #]

    # 2024
    # a) bis 11.784 € (Grundfreibetrag): 0;
    # b) 11.785 € bis 17.005 €: ESt = (954,80 * y + 1.400) * y;
    #                           y = (zvE - 11.784) / 10.000 
    # c) 17.006 € bis 66.760 €: ESt = (181,19 * z + 2.397) * z + 991,21;
    #                           z = (zvE - 17.005) / 10.000 
    # d) 66.761 € bis 277.825 €:              ESt = 0,42 * zvE - 10.636,31;
    # e) ab 277.826 €:              ESt = 0,45 * zvE - 18.971,06.
    TAX_BRACKETS = [
        (0, 11784, lambda x: 0.0),  # A
        (11785, 17005, lambda x: (954.80 * ((x - 11784) / 10000) + 1400) * ((x - 11784) / 10000)),  # B
        (17006, 66760, lambda x: (181.19 * ((x - 17005) / 10000) + 2397) * ((x - 17005) / 10000) + 991.21),  # C
        (66761, 277825, lambda x:0.42*x - 10636.31),  # D
        (277826, float('inf'), lambda x:0.45*x - 18971.06),  # Flat 45% for high earners
    ]




    # 2025
    # #TAX_BRACKETS = [
    #    (0, 12084, lambda x: 0.0),  # No tax below €12,084
    #    (12085, 18000, lambda x: (997.80 * ((x - 12084) / 10000) + 1400) * ((x - 12084) / 10000)),  # First progressive zone
    #    (18001, 63809, lambda x: (2172 * ((x - 18000) / 10000) + 2397) * ((x - 18000) / 10000)),  # Second progressive zone
    #    (63810, 277825, lambda x: 0.42 * x - 9933),  # Middle tax zone (42% rate)
    #    (277826, float('inf'), lambda x: 0.45 * x - 17671.20),  # Top tax zone (45% rate)
    #]


    for lower, upper, tax_func in TAX_BRACKETS:
        if lower <= income <= upper:
            return tax_func(income)
    return 0.0  # Default case (should not occur)

# Calculate taxes using the splitting method
def calculate_split_tax(total_income):
    half_income = total_income / 2
    tax_on_half_income = calculate_tax(half_income)
    return tax_on_half_income * 2

# Calculate taxes using the splitting method
def calc_tax(salary, severance_pay):
    #Adjust the income
    taxbase = calculate_tax(salary)
    taxbase_joint = calculate_split_tax(salary)
    taxSevOnly = (calculate_split_tax(salary + severance_pay/5) - taxbase_joint) * 5
    out_totalTax_WF = (taxSevOnly + taxbase_joint) * 1.05
    out_netIncome = salary + severance_pay - out_totalTax_WF
    out_netIncome_cent = ( out_netIncome / (salary+severance_pay) ) * 100

    print(taxSevOnly)



