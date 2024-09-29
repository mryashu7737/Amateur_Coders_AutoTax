import streamlit as st
from components.refund_calculator import calculate_tax_refund
from components.payment_plan import calculate_payment_plan
from components.refund_tracker import check_refund_status

# App Title
st.title("Tax Refund and Payment Assistance")

# Section 1: Tax Refund Calculation
st.header("Tax Refund Calculator")
income = st.number_input("Annual Income", min_value=0)
withholdings = st.number_input("Taxes Withheld", min_value=0)
deductions = st.number_input("Deductions", min_value=0)
credits = st.number_input("Tax Credits", min_value=0)

if st.button("Calculate Refund"):
    result = calculate_tax_refund(income, withholdings, deductions, credits)
    st.write(result)
    
    # Offer Payment Plan if Taxes Owed
    if "owe" in result:
        try:
            # Extract the owed amount from the result string (e.g., "You owe $132911.00 in taxes.")
            amount_owed = float(result.split('$')[1].split(' ')[0])  # Extract numeric part only
            months = st.slider("Select payment plan duration (months):", min_value=3, max_value=24)
            payment_plan = calculate_payment_plan(amount_owed, months)
            st.write(payment_plan)
        except ValueError as e:
            st.error("Error parsing the owed amount. Please check the input data.")

# Section 2: Refund Status Tracking
st.header("Track Your Refund Status")
ssn = st.text_input("Enter your Aadhaar Card Number:")
filing_status = st.selectbox("Filing Status", ["Single", "Married", "Head of Household"])
refund_amount = st.number_input("Expected Refund Amount", min_value=0)

if st.button("Check Refund Status"):
    refund_status = check_refund_status(ssn, filing_status, refund_amount)
    st.write(refund_status)
