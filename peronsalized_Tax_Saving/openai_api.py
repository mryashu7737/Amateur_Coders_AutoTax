# openai_api.py

import openai

# Set your OpenAI API key
openai.api_key = 'API'




# Function to get personalized tax-saving strategy using the new OpenAI API
def get_tax_saving_strategy(user_data):
    # Construct the prompt as a conversation message
    messages = [
        {"role": "system", "content": "You are an expert tax advisor."},
        {"role": "user", "content": f"""
        I have the following financial details:
        - Income: {user_data['Income']}
        - Investments: {user_data['Investments']}
        - Insurance: {user_data['Insurance']}
        - Loan: {user_data['Loan']}
        - Expenses: {user_data['Expenses']}

        Based on this, provide personalized tax-saving strategies according to Indian tax laws, considering Sections 80C, 80D, 80E, 80G, and other relevant sections.
        """}
    ]
    
    # Use the new ChatCompletion API
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # or 'gpt-4' if available
        messages=messages,
        max_tokens=300,
        temperature=0.7
    )
    
    # Extract the response text
    strategy = response['choices'][0]['message']['content'].strip()
    return strategy
