from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('model.pkl')

# Pre-calculated data statistics for Z-score analysis
data_stats = pd.read_csv('full_user_anomaly_detection_data.csv', index_col=0)

def analyze_anomaly(new_data):
    reasons = []
    suggestions = []
    
    for column in data_stats.index:
        mean_val = data_stats.loc[column, 'mean']
        std_dev = data_stats.loc[column, 'std']
        
        # Calculate Z-score
        z_score = (new_data[column] - mean_val) / std_dev
        
        if abs(z_score) > 3:  # If Z-score > 3, it's considered an anomaly
            anomaly_type = 'high' if z_score > 3 else 'low'
            reasons.append(f"{column} is too {anomaly_type} (Z-score: {z_score:.2f})")
            
            if anomaly_type == 'high':
                suggestions.append(f"Reduce {column} closer to the average of {mean_val:.2f}.")
            else:
                suggestions.append(f"Increase {column} closer to the average of {mean_val:.2f}.")
                
    return reasons, suggestions

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_data = {
            "Income": float(request.form['income']),
            "Deductions": float(request.form['deductions']),
            "Filing_Status": int(request.form['filing_status']),
            "Home_Loan_Interest": float(request.form['home_loan_interest']),
            "Education_Loan_Interest": float(request.form['education_loan_interest']),
            "Charitable_Donations": float(request.form['charitable_donations'])
        }
        
        input_data = pd.DataFrame([user_data])
        prediction = model.predict(input_data)
        
        is_anomaly = prediction[0] == -1
        reasons, suggestions = analyze_anomaly(input_data.iloc[0]) if is_anomaly else ([], [])
        
        return render_template('result.html', is_anomaly=is_anomaly, reasons=reasons, suggestions=suggestions, data=user_data)
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
