import streamlit as st
import pickle as pkl

# Load the model
model = pkl.load(open('model.pkl', 'rb'))

# Load Scaler
scaler = pkl.load(open('scaler.pkl', 'rb'))

# Define the app
st.title("Loan Approval Prediction App")

# Get user inputs

# No of Dependents
no_of_dependents = st.number_input("Number of Dependents", min_value=0, max_value=10, value=0)
# Education
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
education = 0 if education == "Graduate" else 1
# Self Employed
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
self_employed = 1 if self_employed == "Yes" else 0
# Annual Income
income_annum = st.number_input("Annual Income", min_value=0, value=0)
# Loan Amount
loan_amount = st.number_input("Loan Amount", min_value=0, value=0)
# Loan Term
loan_term = st.number_input("Loan Term (in months)", min_value=0, value=0)
# CIBIL Score
cibil_score = st.number_input("CIBIL Score", min_value=0, max_value=900, value=0)
# Total Assets
assets = st.number_input("Total Assets", min_value=0, value=0)

# Create a button to predict
if st.button("Predict"):
    # Prepare the input data
    input_data = [[no_of_dependents, education, self_employed, income_annum,
                   loan_amount, loan_term, cibil_score, assets]]
    
    # Scale the input data
    input_data_scaled = scaler.transform(input_data)
    
    # Make the prediction
    prediction = model.predict(input_data_scaled)
    
    # Display the result
    probabilities = model.predict_proba(input_data_scaled)

    if prediction[0] == 0:
      st.success("Loan Approved")
      st.write(f"Confidence: {round(probabilities[0][0]*100,2)}%")
    else:
      st.error("Loan Rejected")
      st.write(f"Confidence: {round(probabilities[0][1]*100,2)}%")