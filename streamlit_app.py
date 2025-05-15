import streamlit as st
import pandas as pd

st.title('🎈 Loan Approval Prediction App')

st.info('This is an app built to predict loan approvals.')

with st.expander('Data'):
#Data preparation
with st.sidebar:
  st.header('Input features')
  #Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area,Loan_Status
  Gender = st.selectbox('What is your gender?',('Female', 'Male'))
  Married = st.selectbox('Are you married?', ('Yes', 'No'))
  Dependents = st.selectbox('How many dependents do you have?', ('1', '2', '3+'))
  Education = st.selectbox('What is your highest education level?',('Graduate', 'Not Graduate')) 
  Self_Employed = st.selectbox('Are you self employed?', ('Yes', 'No'))
  ApplicantIncome = st.slider('How much is your income?', 150, 81000, 5403)
  
