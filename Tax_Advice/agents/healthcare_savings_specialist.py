class HealthcareSavingsSpecialist:
    def __init__(self):
        self.role = "Healthcare Savings Specialist"
        self.goal = "Optimize healthcare savings accounts (HSAs, FSAs) for tax benefits."

    def analyze(self, data):
        hsa_contributions = data.get('hsa_contributions', 0)
        fsa_contributions = data.get('fsa_contributions', 0)
        income = data['annual_income']

        if income > 100000 and hsa_contributions > 0:
            return f"Contributing ${hsa_contributions} to an HSA is highly beneficial for high-income earners since it reduces taxable income and grows tax-free."
        elif fsa_contributions > 0:
            return f"Your FSA contributions (${fsa_contributions}) can help lower your taxable income."

        return "Consider contributing to an HSA or FSA to optimize your healthcare-related tax savings."
