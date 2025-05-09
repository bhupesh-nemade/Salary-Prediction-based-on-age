import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("salary_model.pkl")  # Make sure this file exists

st.title("Salary Prediction App")

# Input fields for user
experience = st.number_input("Enter Years of Experience:", min_value=0.0, max_value=50.0, step=0.1)
education = st.selectbox("Select Education Level:", ["Bachelor's", "Master's", "PhD"])
age = st.number_input("Enter Age:", min_value=18, max_value=70, step=1)

# Convert categorical values to numerical (dummy encoding example)
education_mapping = {"Bachelor's": 0, "Master's": 1, "PhD": 2}
education_value = education_mapping[education]

# Predict button
if st.button("Predict Salary"):
    input_data = np.array([[experience]])  # Only pass experience

    prediction = model.predict(input_data)
    st.success(f"Predicted Salary: ${prediction[0]:,.2f}")
