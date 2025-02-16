import streamlit as st 
from bmi_operations import calculate_bmi,bmi_to_remarks
st.header("BMI CALCULATOR APP")
weight=st.text_input('Weight(in kg)',value="60",placeholder="Enter your weight",max_chars=5)
print(weight)
height=st.text_input('height(in inches)',value="170",placeholder="Enter your height ", max_chars=4)
print(height)
if st.button('Submit',help='click here', type='primary'):
    bmi = calculate_bmi(height, float(weight))
    bmi_remarks = bmi_to_remarks(bmi)
    st.status(f"Your BMI is {bmi}. Remarks: {bmi_remarks}", expanded=False, state="complete")
