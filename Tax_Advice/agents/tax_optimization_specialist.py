class TaxOptimizationSpecialist:
    def __init__(self):
        self.role = "Tax Optimization Specialist"
        self.goal = "Optimize tax savings based on retirement and donations."

    def analyze(self, data):
        retirement = data['retirement_contributions']
        donations = data['charitable_donations']
        income = data['annual_income']

        # Retirement optimization with contribution limits
        if retirement < 19000:
            retirement_suggestion = f"Consider maximizing your retirement contributions up to $19,500 to reduce taxable income."
        else:
            retirement_suggestion = f"You're contributing the maximum allowed for retirement accounts."

        # Charitable donations for high-income earners
        if income > 200000:
            donation_suggestion = f"Donating ${donations} can reduce your taxable income and also allow you to avoid the higher tax bracket."
        else:
            donation_suggestion = f"Your charitable donations of ${donations} will help reduce your taxable income."

        return f"{retirement_suggestion}\n{donation_suggestion}"
