import streamlit as st
from tasks.advanced_tax_analysis_task import run_advanced_tax_analysis

st.title("Comprehensive Tax Advice and Reduction Strategies")

# Collect user financial data
annual_income = st.number_input("Annual Income", min_value=0, max_value=1000000, step=1000)
deductions = st.number_input("Deductions", min_value=0, max_value=1000000, step=100)
tax_credits = st.number_input("Tax Credits", min_value=0, max_value=50000, step=500)
retirement_contributions = st.number_input("Retirement Contributions", min_value=0, max_value=50000, step=500)
charitable_donations = st.number_input("Charitable Donations", min_value=0, max_value=100000, step=500)
investments = st.number_input("Investments", min_value=0, max_value=1000000, step=1000)
hsa_contributions = st.number_input("HSA Contributions", min_value=0, max_value=10000, step=500)
fsa_contributions = st.number_input("FSA Contributions", min_value=0, max_value=5000, step=500)

# Submit button
if st.button("Analyze Tax Data"):
    # Prepare the user data
    user_data = {
        "annual_income": annual_income,
        "deductions": deductions,
        "tax_credits": tax_credits,
        "retirement_contributions": retirement_contributions,
        "charitable_donations": charitable_donations,
        "investments": investments,
        "hsa_contributions": hsa_contributions,
        "fsa_contributions": fsa_contributions,
    }

    # Run advanced tax analysis and get detailed advice
    result = run_advanced_tax_analysis(user_data)

    st.write(result)
