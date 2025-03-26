import streamlit as st
import pickle
import numpy as np

# Load the trained model and encoders
with open("loan_model.pkl", "rb") as f:
    loaded_data = pickle.load(f)

model = loaded_data["model"]  # Extract trained model
label_encoders = loaded_data["encoders"]  # Extract encoders

# Streamlit UI
st.title("Loan Approval Prediction")

# User inputs for all features
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Number of Dependents", ["0", "1", "2", "3+"])  # 🔹 Ensure this is included!
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.number_input("Loan Term (in days)", min_value=0)
credit_history = st.selectbox("Credit History", [1, 0])
property_area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])

# Prepare user input for model prediction
if st.button("Predict Loan Approval"):
    # Initialize user_data array with features
    user_data = np.array([
        gender, married, dependents, education, self_employed,
        applicant_income, coapplicant_income, loan_amount, loan_term,
        credit_history, property_area
    ]).reshape(1, -1)  # Now contains 11 features!

    # Debug: Print the initial user data (should contain strings for categorical columns)
    st.write(f"Initial user_data (raw inputs): {user_data}")

    # Encode categorical inputs
    categorical_cols = ["Gender", "Married", "Dependents", "Education", "Self_Employed", "Property_Area"]
    for i, col in enumerate(categorical_cols):
        try:
            # Check if the value is in the encoder classes, if not, assign a default value
            if user_data[0, i] not in label_encoders[col].classes_:
                # You can assign a default value or handle it as needed
                user_data[0, i] = label_encoders[col].classes_[0]  # Default to first class
            # Transform the input value and update user_data with the encoded value
            user_data[0, i] = label_encoders[col].transform([user_data[0, i]])[0]
        except KeyError:
            st.error(f"Label encoder not found for column: {col}")
            continue

    # Debug: Print the encoded user data (should now be numeric values)
    st.write(f"Encoded user_data (numeric values): {user_data}")

    # Encode `Property_Area` (which is categorical)
    user_data[0, 10] = label_encoders["Property_Area"].transform([user_data[0, 10]])[0]

    # Debug: Print the encoded user data after encoding Property_Area
    st.write(f"Encoded user_data after encoding Property_Area: {user_data}")

    # Convert all columns to float (now that categorical columns are numeric)
    user_data = user_data.astype(float)  # Now it's all numeric

    # Debug: Print the final user data before prediction
    st.write(f"Final user_data (float values): {user_data}")

    # Make prediction
    try:
        prediction = model.predict(user_data)
        # Display result
        result = "Approved" if prediction[0] == 1 else "Rejected"
        st.success(f"Loan Status: {result}")
    except ValueError as e:
        st.error(f"Error during prediction: {e}")
