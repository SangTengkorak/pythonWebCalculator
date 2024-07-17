from flask import Flask, request, jsonify, render_template

# Create the app object
app = Flask(__name__)

# Importing function for calculation
from basic_calculation_functions import basic_calculations

# Define calculator
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    a = request.form['a']
    b = request.form['b']
    operation = str(request.form['operation'])

    result = basic_calculations(a,b,operation)

    return render_template('index.html', prediction_text=str(result))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)