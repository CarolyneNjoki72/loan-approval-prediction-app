import streamlit as st
import pandas as pd

st.title('🎈 Loan Approval Prediction App')

st.info('This is an app built to predict loan approvals.')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/CarolyneNjoki72/Loan-Prediction-Model/refs/heads/main/loan_prediction_cleancopy.csv')
  df
  
  st.dataframe(df, hide_index=True)

  st.write('**X**')
  X = df.drop('Loan_Status', axis=1)
  X

  st.dataframe(X, hide_index=True)

  st.write('**y**')
  y = df.Loan_Status
  y


with st.expander('Data Visualization'):
  st.scatter_chart(data=df, x='ApplicantIncome', y='LoanAmount', color='Loan_Status')
  
#Data preparation
with st.sidebar:
  st.header('Input features')

  Gender = st.selectbox('What is your gender?',('Female', 'Male'))
  Married = st.selectbox('Are you married?', ('Yes', 'No'))
  Dependents = st.selectbox('How many dependents do you have?', ('1', '2', '3+'))
  Education = st.selectbox('What is your highest education level?',('Graduate', 'Not Graduate'))
  Self_Employed = st.selectbox('Are you self employed?', ('Yes', 'No'))
  ApplicantIncome = st.slider('How much is your income?', 150, 81000, 5403)
  CoapplicantIncome = st.slider('How much does your coapplicant earn?', 0, 41667, 1621)
  LoanAmount = st.slider('How much are you applying?', 9, 700, 146)
  Loan_Amount_Term = st.slider('How long do you want to repay the loan(in months)?', 12, 480, 342)
  Credit_History = st.selectbox('Do you have some credit history?', (1, 0))
  Property_Area = st.selectbox('Select an appropriate term where your property sits.', ('Urban','Rural', 'Semiurban'))

# Create a dataframe for the input features
data = {'Gender': Gender,
        'Married': Married,
        'Dependents': Dependents,
        'Education': Education,
        'Self_Employed': Self_Employed,
        'ApplicantIncome': ApplicantIncome,
        'CoapplicantIncome': CoapplicantIncome,
        'LoanAmount': LoanAmount,
        'Loan_Amount_Term': Loan_Amount_Term,
        'Credit_History': Credit_History,
        'Property_Area': Property_Area}

input_df = pd.DataFrame(data, index=[0])
input_loans = pd.concat([input_df, X], axis=0)

with st.expander('Input features'):
  st.write('**Input loans**')
  input_df
  st.write('**Combined loans data**')
  input_loans

# Encode
df_loans = pd.get_dummies(input_loans, prefix=encode)
df_loans = df_loans.reindex(columns=pd.get_dummies(X, prefix=encode).columns, fill_value=0)
input_encoded = df_loans[:1]



