class InvestmentAdvisor:
    def __init__(self):
        self.role = "Investment Advisor"
        self.goal = "Optimize capital gains and tax-efficient investment strategies."

    def analyze(self, data):
        investments = data['investments']
        income = data['annual_income']

        # Capital gains management and tax-efficient investments
        if investments > 50000 and income > 100000:
            return f"Consider tax-loss harvesting strategies to offset your capital gains. You can invest in tax-efficient accounts like IRAs or 401(k)s to defer taxes."
        else:
            return f"With investments totaling ${investments}, you can consider long-term capital gains strategies to minimize tax liabilities."
