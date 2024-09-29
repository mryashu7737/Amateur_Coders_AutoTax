class TaxReductionAdvisor:
    def __init__(self):
        self.role = "Tax Reduction Advisor"
        self.goal = "Provide personalized strategies to reduce taxes."

    def analyze(self, data):
        deductions = data['deductions']
        credits = data['tax_credits']
        income = data['annual_income']

        # Example logic for standard deductions and phase-outs
        if income > 150000:
            return f"Your income exceeds the limit for certain credits, but you can still claim {deductions} in itemized deductions."
        elif income < 40000:
            return f"You're eligible for a higher Earned Income Credit and {credits} in additional tax credits."
        else:
            return f"Based on your income level, maximizing {deductions} in deductions will reduce your taxable income significantly."
