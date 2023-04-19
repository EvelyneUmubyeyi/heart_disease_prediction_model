import streamlit as st
import pickle
from zipfile import ZipFile

# with ZipFile('model.zip', 'r') as zip:
#     model_pkl = zip.read('model.pkl')

# model = pickle.loads(model_pkl)

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
    page_icon="images/heart_beat.png"
)
st.title("❤️ Heart Disease Diagnosis ")
st.subheader("This app helps you know your heart health by self dignosis.")
st.markdown("""
    This app uses machine learning algorithms to analyze various health parameters and provide users with insights into their heart health. 
    The app collects data such as age, gender, blood pressure, cholesterol information, and lifestyle habits to list a few and uses this information to predict the risk of developing heart disease. 
    The app can also provide recommendations to help users manage their risk factors and prevent the onset of heart disease.
    By leveraging the power of machine learning, you can know about your heath in just a few seconds.

    To predict your heart health follow the steps below:
    1. Provide the answer that best describes you
    2. Press the "Predict" button
      
""")

st.markdown("<div style='padding: 50px'></div>", unsafe_allow_html=True)

st.subheader("Answer the following question thoroughly: ")
st.markdown("<div style='padding: 10px'></div>", unsafe_allow_html=True)

options_dict = {'No': 0, 'Yes': 1}
options = list(options_dict.keys())


bp = st.radio('Have you ever been told that you have high blood pressure by a doctor, nurse, or other health '
              'professional?', options, index=0)
chl = st.radio('Have you ever been told by a doctor, nurse or other health professional that your cholesterol is high?',
               options, index=0)
chl_chk = st.radio('Have you ever had Cholesterol check within past five years', options, index=0)
height = st.number_input("What is your height in meters?", min_value=0.1)
weight = st.number_input("What is your weight in kilograms?", min_value=0)
cigarettes = st.radio("Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes]", options, index=0)
stroke = st.radio("Have you ever been told you had a stroke?", options, index=0)
diabetes = st.radio("Have you ever been told you had diabetes?", options, index=0)
sports = st.radio("Did you engage in a physical activity or exercise during the past 30 days other than your regular job?", options, index=0)
fruits = st.radio("Do you consume fruits one or more times per day?", options, index=0)
veggies= st.radio("Do you consume vegetables one or more times per day?", options, index=0)
alcohol = st.radio("Do you drink more than 14 drinks per week if you are male or more than 7 drinks per week if you are female?", options, index=0)
insurance = st.radio("Do you have some form of health insurance?", options, index=0)
meds_cost = st.radio("Was there a time in the past 12 months when you needed to see a doctor but could not because you could not afford it?", options, index=0)

health_options = {
    "Excellent": 1,
    "Very good": 2,
    "Good": 3, 
    "Fair": 4,
    "Poor": 5
}

health_gen = st.radio("How is your health in general?", options=list(health_options.keys()), index=0)
mental_health = st.number_input("How many days during the past 30 days was your mental health not good?", min_value=0, max_value=30)
physical_health = st.number_input("how many days during the past 30 days was your physical health not good?", min_value=0, max_value=30)

gender_options = {
    "Male": 1,
    "Female": 2
}

gender = st.radio("What is your birth sex?", options=list(gender_options.keys()), index=0)

age_range = {
    "Age 18 to 24 ": 1,
    "Age 25 to 29": 2, 
    "Age 30 to 34": 3, 
    "Age 35 to 39": 4 ,
    "Age 40 to 44": 5,
    "Age 45 to 49 ": 6,
    "Age 50 to 54": 7 ,
    "Age 55 to 59": 8,
    "Age 60 to 64": 9,
    "Age 65 to 69": 10 ,
    "Age 70 to 74": 11,
    "Age 75 to 79": 12,
    "Age 80 or older": 13
}

age_group = st.selectbox("Select your age group:", options=list(age_range.keys()), index=0)

grade_range = {
    "Never attended school or only kindergarten": 1,
    "Grades 1 through 8 (Elementary)": 2 ,
    "Grades 9 through 11 (Some high school)": 3,
    "Grade 12 or GED (High school graduate) ": 4,
    "College 1 year to 3 years (Some college or technical school)": 5,
    "College 4 years or more (College graduate)": 6,
}

school = st.selectbox("What is the highest grade or year of school you completed?", options=list(grade_range.keys()), index=0)

income_range = {
    "Less than $10,000": 1, 
    "Less than $15,000 ($10,000 to < $15,000) ": 2,
    "Less than $20,000 ($15,000 to < $20,000)": 3,
    "Less than $25,000 ($20,000 to < $25,000)": 4,
    "Less than $35,000 ($25,000 to < $35,000)": 5, 
    "Less than $50,000 ($35,000 to < $50,000)": 6, 
    "Less than $75,000 ($50,000 to < $75,000)": 7, 
    "Less than $100,000 ($75,000 to < $100,000)": 8,
    "Less than $150,000 ($100,000 to < $150,000)": 9,
    "Less than $200,000 ($150,000 to < $200,000)": 10, 
    "$200,000 or more": 11
}

income = st.selectbox("Select your annual household income from all sources?", options=list(income_range.keys()), index=0)

st.markdown("<div style='padding: 20px'></div>", unsafe_allow_html=True)
predict = st.button("Predict")
bmi = weight / (height ** 2)
pred_cols = [options_dict[bp], options_dict[chl], options_dict[chl_chk], bmi, options_dict[cigarettes], options_dict[stroke], options_dict[diabetes], 
             options_dict[sports], options_dict[fruits], options_dict[veggies], options_dict[alcohol], options_dict[insurance], options_dict[meds_cost], 
             health_options[health_gen], mental_health, physical_health, gender_options[gender], age_range[age_group], grade_range[school], income_range[income]
            ]

if predict:
    print(pred_cols)
    # prediction = model.predict([pred_cols])
    # st.success("the overall potential {}".format(prediction))
