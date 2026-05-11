from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open('heart_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    age = float(request.form['Age'])

    # Sex
    sex_input = request.form['Sex']
    sex = 1 if sex_input == 'Male' else 0

    # Chest Pain Type
    cp_input = request.form['ChestPainType']

    if cp_input == 'ATA':
        chestpain = 1
    elif cp_input == 'NAP':
        chestpain = 2
    elif cp_input == 'ASY':
        chestpain = 0
    else:
        chestpain = 3

    bp = float(request.form['RestingBP'])
    chol = float(request.form['Cholesterol'])

    fasting = int(request.form['FastingBS'])

    # Resting ECG
    ecg_input = request.form['RestingECG']

    if ecg_input == 'Normal':
        ecg = 1
    elif ecg_input == 'ST':
        ecg = 2
    else:
        ecg = 0

    maxhr = float(request.form['MaxHR'])

    # Exercise Angina
    angina_input = request.form['ExerciseAngina']
    angina = 1 if angina_input == 'Yes' else 0

    oldpeak = float(request.form['Oldpeak'])

    # ST Slope
    slope_input = request.form['ST_Slope']

    if slope_input == 'Down':
        slope = 0
    elif slope_input == 'Flat':
        slope = 1
    else:
        slope = 2

    data = np.array([[age, sex, chestpain, bp, chol,
                      fasting, ecg, maxhr,
                      angina, oldpeak, slope]])

    scaled_data = scaler.transform(data)

    prediction = model.predict(scaled_data)

    if prediction[0] == 1:
        result = "Heart Disease Detected"
    else:
        result = "No Heart Disease"

    return render_template('index.html',
                           prediction_text=result)

if __name__ == '__main__':
    app.run(debug=False)