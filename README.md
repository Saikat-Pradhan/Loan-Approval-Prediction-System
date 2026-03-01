# 🏦 Loan Approval Prediction System Web App

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-MachineLearning-orange?logo=scikitlearn)
![Classification](https://img.shields.io/badge/Model-Classification-green)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-yellow)
![Deployment](https://img.shields.io/badge/Deployment-StreamlitCloud-brightgreen)

A smart Machine Learning–based Loan Approval Prediction Web Application that predicts whether a loan application will be approved or rejected based on applicant financial and personal details.

Built using Python, Scikit-learn, Streamlit, and successfully deployed online for real-time predictions.

---

## 🔗 Live Demo

👉 Try the deployed web app here: https://loan-approval-prediction-system-by-saikat-pradhan.streamlit.app/

---

## 🚀 Project Overview

### Financial institutions receive thousands of loan applications daily.

### This project demonstrates how Machine Learning classification models can automate loan approval decisions using applicant data.

### The system analyzes multiple financial factors and instantly predicts:

- Loan Approval Status
- Prediction Confidence Score

### The web interface allows users to interactively input applicant details and receive real-time predictions.

---

## 🎯 Application Features

- Interactive user-friendly UI
- Real-time loan approval prediction
- Confidence probability display
- Feature scaling using trained scaler
- ML model integration with Streamlit
- Instant prediction results
- Fully deployed cloud application

---

## 🧠 Input Parameters Used

### The prediction model considers:
- Number of Dependents
- Education Level
- Self Employment Status
- Annual Income
- Loan Amount
- Loan Term
- CIBIL Score
- Total Assets

These financial indicators help evaluate loan eligibility risk.

---

## 🧠 Technologies Used

- Python 🐍
- Streamlit 🌐
- Scikit-learn 🤖
- Pandas 📊
- NumPy 📐
- Machine Learning Classification ⚙️
- Pickle 📦 (Model Serialization)

---

## 📊 Dataset

### The dataset contains loan applicant financial and demographic information.

- Features Included
- Dependents
- Education
- Employment Status
- Income Details
- Loan Information
- Credit Score (CIBIL)
- Asset Details
- Loan Approval Status (Target)

### Dataset used for training: loan_approval_dataset.csv

---

## 🏗️ Model Training

### Model development and experimentation were performed in:

- Loan_Approval_Prediction_Model.ipynb
- Training Pipeline
- Data Cleaning
- Feature Encoding
- Feature Scaling
- Train-Test Split
- Model Training
- Model Evaluation
- Probability Prediction
- Model Serialization using Pickle

### Saved Files
- model.pkl   → Trained ML Model
- scaler.pkl  → Feature Scaler

---

## 🧠 How the App Works

- User enters loan applicant details.
- Input data is converted into numerical format.
- Data is scaled using trained scaler.
- Machine Learning model predicts approval status.
- Prediction probability is calculated.
- Result displayed instantly on dashboard.

---

## 📁 Project Structure
```
Loan-Approval-Prediction-System
│
├── app.py
├── model.pkl
├── scaler.pkl
├── loan_approval_dataset.csv
├── Loan_Approval_Prediction_Model.ipynb
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Guide (Run Locally)
### 1️⃣ Clone the Repository
```
git clone https://github.com/Saikat-Pradhan/Loan-Approval-Prediction-System.git
cd Loan-Approval-Prediction-System
```
### 2️⃣ Install Dependencies
```
pip install -r requirements.txt
```
### 3️⃣ Run the Streamlit Application
```
streamlit run app.py
```
### 🌐 Open in Browser
```
http://localhost:8501
```

---

## 📉 Prediction Output

### The application provides:

- Loan Approved / Rejected Result
- Prediction Confidence Score
- Instant Decision Support

---

## 🌍 Deployment

 Successfully deployed using Streamlit Cloud

### Live Application: https://loan-approval-prediction-system-by-saikat-pradhan.streamlit.app/

---

## ⭐ Support

If you like this project, please give it a ⭐ on GitHub.

It motivates me to build more Machine Learning & AI applications 🚀

---

## 👨‍💻 Author

Saikat Pradhan

🔗 GitHub: https://github.com/Saikat-Pradhan

💼 B.Tech CSE | Machine Learning & Data Science Enthusiast
