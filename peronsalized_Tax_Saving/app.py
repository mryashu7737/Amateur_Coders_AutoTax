# app.py

from flask import Flask, render_template, request, jsonify
from openai_api import get_tax_saving_strategy

app = Flask(__name__)

# Route to serve the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and OpenAI API call
@app.route('/submit', methods=['POST'])
def submit_form():
    # Get the user data from the form
    user_data = {
        'Income': int(request.form['income']),
        'Investments': int(request.form['investments']),
        'Insurance': int(request.form['insurance']),
        'Loan': int(request.form['loan']),
        'Expenses': int(request.form['expenses'])
    }

    # Get personalized tax-saving strategy from OpenAI API
    strategy = get_tax_saving_strategy(user_data)

    # Return the strategy as a JSON response
    return jsonify({'strategy': strategy})

if __name__ == '__main__':
    app.run(debug=True)
