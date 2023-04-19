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

st.set_page_config(
        page_title="Heart Disease Prediction App",
        page_icon="images/heart.png"
    )
st.title("Heart Disease Diagnosis")


bp = st.radio('Have you ever been told that you have high blood pressure by a doctor, nurse, or other health '
              'professional?', options, index=0)
chl = st.radio('Have you ever been told by a doctor, nurse or other health professional that your cholesterol is high?',
               options, index=0)
chl_chk = st.radio('Have you ever had Cholesterol check within past five years', options, index=0)
height = st.number_input("What is your height in meters?", min_value=0)
weight = st.number_input("What is your weight in kilograms?", min_value=0)
cigarettes = st.radio("Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes]", options, index=0)
stroke = st.radio("Have you ever been told you had a stroke?", options, index=0)
diabetes = st.radio("Have you ever been told you had diabetes?", options, index=0)
sports = st.radio("Did you engage in a physical activity or exercise during the past 30 days other than your regular job?", options, index=0)
fruits = st.radio("Do you consume fruits one or more times per day?", options, index=0)
veggies= st.radio("Do you consume vegetables one or more times per day?", options, index=0)
alcohol = st.radio("Do you drink more than 14 drinks per week if you are male or more than 7 drinks per week if you are female?", options, index=0)
insurance = st.radio("Do you have some form of health insurance?", options, index=0)
meds = st.radio("Was there a time in the past 12 months when you needed to see a doctor but could not because you could not afford it?", options, index=0)
health_options = {
    1: "Excellent",
2:"Very good",
3: "Good", 
4: "Fair",
5: "Poor"
}
health_gen = st.radio("How is your health in general?", options=list(health_options.values()), index=0)
mental_health = st.number_input("How many days during the past 30 days was your mental health not good?", min_value=0, max_value=30)
physical_health = st.number_input("how many days during the past 30 days was your physical health not good?", min_value=0, max_value=30)
gender_options = {
    1: "Male",
    2: "Female"
}
gender = st.radio("What is your birth sex?", options=list(gender_options.values()), index=0)
age_range = {
    1: "Age 18 to 24 ",
2: "Age 25 to 29", 
3: "Age 30 to 34", 
4: "Age 35 to 39" ,
5: "Age 40 to 44" ,
6: "Age 45 to 49 ",
7: "Age 50 to 54" ,
8: "Age 55 to 59",
9: "Age 60 to 64" ,
10: "Age 65 to 69" ,
11: "Age 70 to 74",
12: "Age 75 to 79",
13: "Age 80 or older"

}
age_group = st.selectbox("Select your age group:", options=list(age_range.values()), index=0)
grade_range = {
    1: "Never attended school or only kindergarten",
2: "Grades 1 through 8 (Elementary)" ,
3: "Grades 9 through 11 (Some high school)",
4: "Grade 12 or GED (High school graduate) ",
5: "College 1 year to 3 years (Some college or technical school)",
6: "College 4 years or more (College graduate)",
}

grade_school = st.selectbox("What is the highest grade or year of school you completed?", options=list(age_range.values()), index=0)

income_range = {
    1: "Less than $10,000", 
2: "Less than $15,000 ($10,000 to < $15,000) ",
3: "Less than $20,000 ($15,000 to < $20,000)",
4: "Less than $25,000 ($20,000 to < $25,000)",
5: "Less than $35,000 ($25,000 to < $35,000)", 
6: "Less than $50,000 ($35,000 to < $50,000)", 
7: "Less than $75,000 ($50,000 to < $75,000)", 
8: "Less than $100,000 ($75,000 to < $100,000)",
9: "Less than $150,000 ($100,000 to < $150,000)",
10: "Less than $200,000 ($150,000 to < $200,000)", 
11: "$200,000 or more"
}

salary_income = st.selectbox("Select your annual household income from all sources?", options=list(income_range.values()), index=0)

predict = st.button("Heart Condition", on_click=print("hello"))

