from flask import Flask, request, jsonify, render_template, send_file
from agents.extract_agent import ExtractAgent
from agents.fill_agent import FillAgent
import os

# Create the Flask application instance
app = Flask(__name__)

# Serve the home page with the form
@app.route('/')
def index():
    return render_template('index.html')

# Handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    # Get form data from the POST request
    user_data = {
        'PAN': request.form['PAN'],
        'First Name': request.form['First Name'],
        'Middle Name': request.form['Middle Name'],
        'Last Name': request.form['Last Name'],
        'Date of Birth': request.form['Date of Birth'],
        'Aadhaar Number': request.form['Aadhaar Number'],
        'Mobile Number': request.form['Mobile Number'],
        'Email Address': request.form['Email Address']
    }

    # Process form (using FillAgent)
    form_path = './data/uploads/ITR_form.png'  # Path to the blank ITR form
    fill_agent = FillAgent(form_path, user_data)
    filled_form_path = fill_agent.fill_form()

    # Return JSON response with the filled form download link
    return jsonify({
        'message': 'Form filled successfully!',
        'download_link': f'/download/{os.path.basename(filled_form_path)}'
    })

# Serve the filled form for download
@app.route('/download/<filename>', methods=['GET'])
def download_filled_form(filename):
    filled_form_path = os.path.join('./data/filled', filename)
    return send_file(filled_form_path, as_attachment=True)

# Start the Flask application

