# loan-eligibility-analysis

This is a Streamlit-based application that predicts loan approval status based on user inputs. The app utilizes a pre-trained machine learning model to make predictions about whether a loan should be approved or rejected.

## Features

- **User Inputs**: Users provide details such as gender, marital status, education, income details, and property area.
- **Prediction**: The app predicts whether the loan is approved or rejected based on the input data.
- **Machine Learning Model**: The model used in the app is trained using a dataset with relevant features, and it predicts the loan approval status.
- **Data Preprocessing**: The app encodes categorical inputs (e.g., gender, education, etc.) before feeding them into the model for prediction.

## Requirements

To run this app locally, you need the following Python libraries:

- `streamlit`
- `pickle`
- `numpy`
- `scikit-learn`
  
## Screenshots

Below are screenshots of the Loan Approval Prediction app:

![Screenshot 1](ss1.png)  
Here you can input the data from a menu based technique

![Screenshot 2](ss2.png)  
Here you can hit predict and then see the result of the loan

## Model Details

The machine learning model used for loan approval prediction was trained using a dataset containing the following features:

- **Gender**: Male or Female
- **Marital Status**: Yes or No
- **Number of Dependents**: 0, 1, 2, or 3+
- **Education**: Graduate or Not Graduate
- **Self-Employed**: Yes or No
- **Applicant Income**: Numeric value representing the income of the applicant
- **Coapplicant Income**: Numeric value representing the income of the coapplicant
- **Loan Amount**: Numeric value representing the amount of loan requested
- **Loan Term**: Numeric value representing the term of the loan in days
- **Credit History**: Binary (1 for good credit history, 0 for bad credit history)
- **Property Area**: Urban, Rural, or Semiurban

The model was trained and pickled for use in the app.

## How It Works

1. The user inputs values for the above features.
2. The app encodes categorical values (such as `Gender`, `Marital Status`, etc.) using label encoding.
3. The encoded data is passed into the pre-trained model for prediction.
4. The app outputs whether the loan is "Approved" or "Rejected" based on the model's prediction.
