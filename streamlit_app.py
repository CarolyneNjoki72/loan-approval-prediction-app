import streamlit as st
import pandas as pd

st.title('🎈 Loan Approval Prediction App')

st.info('This is an app built to predict loan approvals.')

with st.expander('Data')
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/CarolyneNjoki72/Loan-Prediction-Model/refs/heads/main/loan_prediction_cleancopy.csv')
  df
