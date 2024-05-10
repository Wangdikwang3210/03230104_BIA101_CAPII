class Salary:
    def __init__(self, basic_salary, allowances,num_child,expense):
        self.basic_salary = basic_salary
        self.allowances = allowances
        self.num_child=num_child
        self.expense=expense

    def calculate_gross_salary(self):# addition of basic salary and allowance gives you gross salary.
        gross_salary=self.basic_salary + self.allowances
        return gross_salary


    def calculate_pf_deduction(self):
        deduction=0                    # deduction of NPPF from the gross salary of an individual
        deduction +=gross_salary * 0.10# though it differs from company to company, here it is considered 10% for application convinience
        deduction += 200 
        deduction += min(350000*self.num_child,self.expense * self.num_child)
        return deduction

    def calculate_taxable_income(self):
        return gross_salary - deduction

class TaxCalculator: # calculation of tax amount on individual's taxable income
    def __init__(self,taxable_income):
         self.taxable_income= taxable_income
    def calculate_tax(self):
        
        if taxable_income <= 300000: # no imposition of tax if income is less than 300000
                return 0
        elif 300001 < taxable_income < 400000:#if income is more than 300000 and less than 400000, you will be imposed 10% of your income.
                return taxable_income * 0.1
        elif 400001 < taxable_income < 650000:#if income is more than 400000 and less than 650000, you will be imposed 15% of your income.
            return taxable_income * .15
        elif 650001 < taxable_income < 1000000:#if income is more than 650000 and less than 1000000, you will be imposed 20% of your income.
            return taxable_income * .20
        elif 1000000 < taxable_income < 1500000:#if income is more than 1000000 and less than 1500000, you will be imposed 25% of your income.
            return taxable_income * .25
        else:
             return taxable_income *.30#if income is more than 1500000, you will be imposed 30% of your income.

        
# asking for the user input to provide individual's information such as salary amount, allowances,no.of children and expenses.
basic_salary = float(input("please enter your basic salary amount: "))
allowances = float(input("please enter your allowances amount: "))
child=int(input(' how many children do you have :'))
expense=int(input('Enter expense per child :'))

salary = Salary(basic_salary, allowances,child,expense)
gross_salary = salary.calculate_gross_salary()

deduction = salary.calculate_pf_deduction()


taxable_income = salary.calculate_taxable_income()

tax = TaxCalculator.calculate_tax(taxable_income)

print("Your gross salary is:", gross_salary)
print("PF deduction:", deduction)
print("Your taxable income is:", taxable_income)
print("Tax amount payable:", tax)
