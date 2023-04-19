import streamlit as st
import pickle
options_dict = {'No': 0, 'Yes': 1}

options = list(options_dict.keys())

questions_dict = {
    '_RFHYPE5':'Have you ever been told that you have high blood pressure by a doctor, nurse, or other health professional?',
    'TOLDHI2': 'Have you ever been told by a doctor, nurse or other health professional that your cholesterol is high?',
    '_CHOLCH2': 'Have you ever had Cholesterol check within past five years?',
    'Height': 'What is your height in meters?',
    'Weight': 'What is your weight in kilograms?',
    'SMOKE100': 'Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes]',
    'CVDSTRK3': 'Have you ever been told you had a stroke?',
    'DIABETE4': 'Have you ever been told you had diabetes?',
    '_TOTINDA': 'Did you engage in a physical activity or exercise during the past 30 days other than your regular job?',
    '_FRTLT1A': 'Do you consume fruits one or more times per day?',
    '_VEGLT1A': 'Do you consume vegetables one or more times per day?',
    '_RFDRHV7': 'Do you drink more than 14 drinks per week if you are male or more than 7 drinks per week if you are female?',
    '_HLTHPLN': 'Do you have some form of health insurance?',
'MEDCOST1': 'Was there a time in the past 12 months when you needed to see a doctor but could not because you could not afford it?'

}


bp = st.radio('Have you ever been told that you have high blood pressure by a doctor, nurse, or other health '
              'professional?', options, index=0)
chl = st.radio('Have you ever been told by a doctor, nurse or other health professional that your cholesterol is high?',
               options, index=0)
chl_chk = st.radio('Have you ever had Cholesterol check within past five years')
