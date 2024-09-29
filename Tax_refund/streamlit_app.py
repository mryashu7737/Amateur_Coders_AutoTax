import streamlit as st
from huggingface_integration import generate_tax_summary  # Import Hugging Face text generator

st.title("Tax Refund and Payment Assistance")

# Input form for tax data
with st.form("tax_data_form"):
    tax_refund_amount = st.number_input("Enter your tax refund amount", min_value=0, max_value=10000, step=50)
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.write("Generating explanation...")
        summary = generate_tax_summary(tax_refund_amount)
        st.success("Tax Summary Generated")
        st.write(summary)
