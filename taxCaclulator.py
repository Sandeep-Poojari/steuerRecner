import taxBracketManager as tbm

class TaxCalculator:
    def __init__(self, salary: float, severance_pay: float, assessment_year: int, joint_filing: bool):
        self.salary = salary
        self.severance_pay = severance_pay
        self.assessment_year = assessment_year
        self.joint_filing = joint_filing
        self.tax_brackets = tbm.TaxBracketManager.get_tax_brackets(assessment_year)

    def calculate_basetax(self, income: float) -> float:
        for lower, upper, tax_func in self.tax_brackets:
            if lower <= income <= upper:
                return tax_func(income)
        return 0.0

    def calculate_tax(self, total_income: float) -> float:

        adjusted_income = total_income
        if self.joint_filing == True : adjusted_income = total_income / 2

        tax = self.calculate_basetax(adjusted_income)
        if self.joint_filing == True : tax = tax * 2

        return tax*1.05  # add 5% solidarity tax

    def get_total_tax(self) -> float:
        total_tax = self.calculate_tax(self.salary)
        if self.severance_pay > 0:
            total_tax +=  ((self.calculate_tax(self.salary + self.severance_pay / 5) - total_tax) * 5)
        return total_tax
        
    def get_total_tax_wo_fifth(self) -> float:
        return self.calculate_tax(self.salary + self.severance_pay)

    def get_tax_severance_only(self) -> float:
        return (self.calculate_tax(self.salary + self.severance_pay / 5) - self.calculate_tax(self.salary)) * 5

    def get_net_income(self) -> float:
        return (self.salary + self.severance_pay - self.get_total_tax())

    def get_net_percent(self) -> float:
        return ((self.get_net_income() / (self.salary + self.severance_pay)) * 100)
    
