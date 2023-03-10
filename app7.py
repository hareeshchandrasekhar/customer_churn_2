# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 16:13:22 2023

@author: Purushothama G V
"""

import numpy as np
import pickle
import pandas as pd

import streamlit as st 

from PIL import Image

pickle_in = open(r"C:\Users\excel\Downloads\hari doubts\model_df_smott.pkl","rb")
model_df_smott=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def Churn_prediction(account_length,voice_plan,voice_messages,intl_plan,intl_mins,intl_calls,intl_charge,day_mins,day_calls,day_charge,eve_mins,eve_calls,eve_charge,night_mins,night_calls,night_charge,customer_calls):
   if voice_plan == "No":
        voice_plan = 0
   else:
        voice_plan = 1
   if intl_plan == "No":
        intl_plan = 0
   else:
        intl_plan = 1 
   prediction=model_df_smott.predict([[account_length,voice_plan,voice_messages,intl_plan,intl_mins,intl_calls,intl_charge,day_mins,day_calls,day_charge,eve_mins,eve_calls,eve_charge,night_mins,night_calls,night_charge,customer_calls]])
   print(prediction)
   if (prediction[0] == 0):
        return 'The person will not be churned'
   else:
        return 'The person will be churned'
    



def main():
    
    st.title('Churn prediction Web App')
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Churn Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    account_length=st.sidebar.number_input("Enter the Account Length")
    voice_plan=st.sidebar.selectbox("Do you have a Voice plan",("No","Yes"))
    voice_messages=st.sidebar.number_input("Enter the number of voice messages")
    intl_plan=st.sidebar.selectbox("Do you have a international plan", ("No","Yes"))
    intl_mins=st.sidebar.number_input("Enter the total international mins")
    intl_calls=st.sidebar.number_input("Enter the number of international calls")
    intl_charge=st.sidebar.number_input("Enter the total INTL charge")
    day_mins=st.sidebar.number_input("Enter the total day mins")
    day_calls=st.sidebar.number_input("Enter the number of day calls")
    day_charge=st.sidebar.number_input("Enter the total day charge")
    eve_mins=st.sidebar.number_input("Enter the total evening mins")
    eve_calls=st.sidebar.number_input("Enter the number of Evening calls")
    eve_charge=st.sidebar.number_input("Enter the total evening charge")
    night_mins=st.sidebar.number_input("Enter the total night mins")
    night_calls=st.sidebar.number_input("Enter the number of Night calls")
    night_charge=st.sidebar.number_input("Enter the total night charge")
    customer_calls=st.sidebar.number_input("Enter the total customer calls")
    
    #code for prediction (the result of prediction will return in this empty string)
    Churn = ''
    
    #creating button for prediction
    if st.button('Churn Result'):
        Churn = Churn_prediction(account_length,voice_plan,voice_messages,intl_plan,intl_mins,intl_calls,intl_charge,day_mins,day_calls,day_charge,eve_mins,eve_calls,eve_charge,night_mins,night_calls,night_charge,customer_calls)
    
    
    st.success(Churn)
    
    
    
if __name__ == '__main__':
    main()