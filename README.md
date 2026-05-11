# Heart-Disease-Prediction-System-using-KNN-ML-Project-
Heart Disease Prediction System using KNN and Flask with real-time prediction, hyperparameter tuning, feature scaling, cross-validation, and interactive web deployment.

## 📌 Project Overview

This project is a Machine Learning based Heart Disease Prediction System developed using the K-Nearest Neighbors (KNN) algorithm and deployed using Flask.

The application predicts whether a patient is likely to have heart disease based on medical parameters entered by the user.

---

# 🚀 Features

- Heart Disease Prediction using KNN Algorithm
- Real-time Prediction using Flask Web Application
- User-friendly Interface using HTML and CSS
- Feature Scaling using StandardScaler
- Hyperparameter Tuning using GridSearchCV
- Cross Validation
- Evaluation using Accuracy, Precision, Recall, F1-Score and Confusion Matrix
- Categorical Input Handling (Male/Female, Yes/No, etc.)

---

# 🛠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Flask | Web Framework |
| HTML | Frontend Structure |
| CSS | Styling |
| Scikit-learn | Machine Learning |
| Pandas | Data Handling |
| NumPy | Numerical Operations |
| Pickle | Model Saving |

---

# 📂 Project Structure

```text
Heart_Disease_ML_Project/
│
├── app.py
├── heart_model.pkl
├── scaler.pkl
├── heart.csv
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

# 📊 Dataset Information

Dataset contains medical information such as:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Resting ECG
- Maximum Heart Rate
- Exercise Angina
- Oldpeak
- ST Slope

Target Variable:

- HeartDisease
  - 1 = Heart Disease
  - 0 = No Heart Disease

---

# ⚙️ Machine Learning Workflow

1. Load Dataset
2. Data Cleaning
3. Encoding Categorical Columns
4. Feature Scaling
5. Train-Test Split
6. Model Building using KNN
7. Hyperparameter Tuning
8. Model Evaluation
9. Model Deployment using Flask

---

# 📈 Evaluation Metrics Used

- Accuracy Score
- Precision Score
- Recall Score
- F1 Score
- Confusion Matrix

---

# 🌐 Web Application

The Flask web application allows users to:

- Enter patient information
- Predict heart disease in real-time
- View prediction results instantly

---

# ▶️ How to Run the Project

## Step 1: Clone Repository

```bash
git clone <your-github-repository-link>
```

---

## Step 2: Open Project Folder

```bash
cd Heart_Disease_ML_Project
```

---

## Step 3: Install Required Libraries

```bash
pip install flask pandas numpy scikit-learn
```

---

## Step 4: Run Flask Application

```bash
python app.py
```

---

## Step 5: Open Browser

```text
http://127.0.0.1:5000
```

---

# 💡 Future Improvements

- Improve UI Design
- Add Authentication System
- Deploy on Cloud Platforms
- Add Database Integration
- Use Advanced ML Algorithms

---

# 👨‍💻 Author

Tirupati Kundagir

B.Tech Student | Data scientist & Machine Learning Enthusiast

---

# ⭐ Conclusion

This project demonstrates practical implementation of:

- Machine Learning
- Model Tuning
- Flask Deployment
- Frontend Integration
- End-to-End ML Workflow
