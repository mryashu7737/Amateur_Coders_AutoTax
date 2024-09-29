from agents.tax_reduction_advisor import TaxReductionAdvisor
from agents.tax_optimization_specialist import TaxOptimizationSpecialist
from agents.healthcare_savings_specialist import HealthcareSavingsSpecialist
from agents.investment_advisor import InvestmentAdvisor

def run_advanced_tax_analysis(user_data):
    reduction_advisor = TaxReductionAdvisor()
    optimization_specialist = TaxOptimizationSpecialist()
    healthcare_specialist = HealthcareSavingsSpecialist()
    investment_advisor = InvestmentAdvisor()

    # Get detailed advice from all agents
    reduction_advice = reduction_advisor.analyze(user_data)
    optimization_advice = optimization_specialist.analyze(user_data)
    healthcare_advice = healthcare_specialist.analyze(user_data)
    investment_advice = investment_advisor.analyze(user_data)

    # Compile a step-by-step action plan
    return f"""
    ## Step-by-Step Tax Reduction Plan
    
    ### 1. Tax Reduction Strategies:
    {reduction_advice}
    
    ### 2. Retirement and Charitable Donations Optimization:
    {optimization_advice}
    
    ### 3. Healthcare Savings:
    {healthcare_advice}
    
    ### 4. Investment Strategies for Tax Savings:
    {investment_advice}
    
    ### Summary:
    Following these strategies can help reduce your tax liability across multiple areas, 
    including deductions, credits, healthcare, and investments.
    """
