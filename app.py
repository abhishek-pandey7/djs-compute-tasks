import streamlit as st
import pandas as pd
import numpy as np 
import pickle

#loading model and scaler
with open('asthma_model.pkl','rb') as f:
    model,scaler=pickle.load(f)

st.title('Asthma Predictor')
st.write('enter patient details to predict asthma probability')

#input from user
age=st.number_input('Age',min_value=1,max_value=120,value=25)
gender=st.selectbox('Gender',['male','female'])
bmi=st.number_input('BMI',min_value=10.0,max_value=50.0,value=22.5)
smoking_status=st.selectbox('Smoking Status',['Never','Former','Current'])
family_history=st.selectbox("Family History of Asthma",["Yes", "No"])
allergies = st.selectbox("Allergies", ["None", "Pets", "Pollen", "Dust", "Multiple"])
air_pollution=st.selectbox("Air Pollution Level",["Low","Moderate","High"])
physical_activity=st.selectbox("Physical Activity Level",["Sedentary","Moderate","Active"])
comorbidities=st.selectbox("Other Comorbidities",["Yes", "No"])
medication=st.selectbox("Medication Adherence",["Yes", "No"])
er_visits=st.number_input("Number of ER Visits",min_value=0,max_value=20,value=0)
peak_flow=st.number_input("Peak Expiratory Flow",min_value=50,max_value=800,value=400)
feno=st.number_input("FeNO Level",min_value=5,max_value=200,value=25)

#converting categorical data to numerical data
gender=1 if gender=='male' else 0
smoking_status={'Never':0,'Former':1,'Current':2}[smoking_status]
family_history=1 if family_history=='Yes' else 0
comorbidities=1 if comorbidities=='Yes' else 0
medication=1 if medication=='Yes' else 0
air_pollution={"Low":0, "Moderate":1,"High":2}[air_pollution]
physical_activity={"Sedentary": 0,"Moderate":1,"Active":2}[physical_activity]
allergies = {"None": 0, "Pets": 1, "Pollen": 2, "Dust": 3, "Multiple": 4}[allergies]

#make features array
features=np.array([[age,gender,bmi,smoking_status,family_history,allergies,air_pollution,physical_activity,comorbidities,medication,er_visits, peak_flow, feno]])

#scaling features
features=scaler.transform(features)

#prediction
if st.button('Predict'):
    prediction=model.predict(features)[0]
    probability=model.predict_proba(features)[0][1]

    if prediction==1:
        st.error(f'The patient is likely to have asthma with a probability of {probability:.2f}')
    else:
        st.success(f'The patient is unlikely to have asthma with a probability of {1-probability:.2f}')