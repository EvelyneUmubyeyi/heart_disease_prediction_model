import streamlit as st
import pickle
from zipfile import ZipFile
import pandas
import numpy
import pickle

with ZipFile('model.zip', 'r') as zipFile:
    model_pkl = zipFile.read('model.pkl')

model = pickle.loads(model_pkl)

st.set_page_config(
    page_title="Heart Disease Prediction App",
    page_icon="images/heart_beat.png"
)
st.title("❤️ Heart Disease Diagnosis ❤️")
st.markdown("<div style='padding: 30px'></div>", unsafe_allow_html=True)
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


bp = st.selectbox('Have you ever been told that you have high blood pressure by a doctor, nurse, or other health '
              'professional?', options, index=0)
chl = st.selectbox('Have you ever been told by a doctor, nurse or other health professional that your cholesterol is high?',
               options, index=0)
chl_chk = st.selectbox('Have you ever had Cholesterol check within past five years', options, index=0)
height = st.number_input("What is your height in meters?", min_value=0.1)
weight = st.number_input("What is your weight in kilograms?", min_value=0)
cigarettes = st.selectbox("Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes]", options, index=0)
stroke = st.selectbox("Have you ever been told you had a stroke?", options, index=0)
diabetes_options = {
    "Yes" : 1,
    "Yes, but female told only during pregnancy":  2, 
    "No": 3,
    "No, pre-diabetes or borderline diabetes": 4
}
diabetes = st.selectbox("Have you ever been told you had diabetes?", diabetes_options.keys(), index=0)
sports = st.selectbox("Did you engage in a physical activity or exercise during the past 30 days other than your regular job?", options, index=0)
fruits = st.selectbox("Do you consume fruits one or more times per day?", options, index=0)
veggies= st.selectbox("Do you consume vegetables one or more times per day?", options, index=0)
alcohol = st.selectbox("Do you drink more than 14 drinks per week if you are male or more than 7 drinks per week if you are female?", options, index=0)
insurance = st.selectbox("Do you have some form of health insurance?", options, index=0)
meds_cost = st.selectbox("Was there a time in the past 12 months when you needed to see a doctor but could not because you could not afford it?", options, index=0)

health_options = {
    "Excellent": 1,
    "Very good": 2,
    "Good": 3, 
    "Fair": 4,
    "Poor": 5
}

health_gen = st.selectbox("How is your health in general?", options=list(health_options.keys()), index=0)
mental_health = st.number_input("How many days during the past 30 days was your mental health not good?", min_value=0, max_value=30)
physical_health = st.number_input("how many days during the past 30 days was your physical health not good?", min_value=0, max_value=30)
diff_walk= st.selectbox("Do you have serious difficulty walking or climbing stairs? ", options, index=0)
gender_options = {
    "Male": 1,
    "Female": 2
}

gender = st.selectbox("What is your birth sex?", options=list(gender_options.keys()), index=0)

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

income = st.selectbox("Select your annual household income from all sources: ", options=list(income_range.keys()), index=0)

st.markdown("<div style='padding: 20px'></div>", unsafe_allow_html=True)
predict = st.button("Predict")
bmi = weight / (height ** 2)
pred_cols = [options_dict[bp], options_dict[chl], options_dict[chl_chk], bmi, options_dict[cigarettes], options_dict[stroke], diabetes_options[diabetes], 
             options_dict[sports], options_dict[fruits], options_dict[veggies], options_dict[alcohol], options_dict[insurance], options_dict[meds_cost], 
             health_options[health_gen], mental_health, physical_health, options_dict[diff_walk], gender_options[gender], age_range[age_group], grade_range[school], income_range[income]
            ]

selected_columns = ['_RFHYPE6','TOLDHI3','_CHOLCH3','_BMI5','SMOKE100','CVDSTRK3','DIABETE4','_TOTINDA','_FRTLT1A','_VEGLT1A','_RFDRHV7','_HLTHPLN','MEDCOST1',
        'GENHLTH','MENTHLTH','PHYSHLTH','DIFFWALK','_SEX','_AGEG5YR','EDUCA','INCOME3']

df = pandas.DataFrame([pred_cols], columns=selected_columns)
st.markdown("<div style='padding: 20px'></div>", unsafe_allow_html=True)
if predict:
    prediction = model.predict(df)
    if prediction == 1:
        st.subheader("❤️‍🩹 There is a possibility that you could a heart disease.")
        st.markdown("<div style='padding: 5px'></div>", unsafe_allow_html=True)
        st.image("images/bad.jpg")
        st.markdown("""
            Based on the information you provided, it appears that you may have some risk factors for heart diseases, such as high blood pressure, high cholesterol levels, and a sedentary lifestyle. However, there are several things you can do to mitigate these risk factors and improve your heart health.

            Regular physical activity is essential for maintaining good cardiovascular health. Engaging in at least 30 minutes of moderate-intensity exercise most days of the week can help reduce the risk of developing heart diseases. This can include activities such as brisk walking, cycling, or swimming.

            Eating a balanced diet that is rich in fruits, vegetables, whole grains, lean proteins, and healthy fats can also help maintain good heart health. It is recommended to consume at least five servings of fruits and vegetables per day and to limit the intake of saturated and trans fats, sodium, and added sugars.

            It is also important to avoid smoking and limit alcohol consumption. Smoking is a significant risk factor for heart diseases, and reducing or quitting smoking can significantly improve heart health. Excessive alcohol consumption can also increase the risk of heart diseases, and it is recommended to limit intake to no more than 14 drinks per week if you are male or 7 drinks per week if you are female.

            Regular check-ups with a healthcare provider can also help monitor heart health and identify any potential risks or issues. It is recommended to have a cholesterol check at least once every five years and to discuss any concerns about blood pressure or diabetes with a healthcare provider.

            It is also important to prioritize rest and relaxation, as adequate sleep and stress management can significantly impact your health and well-being.
             """) 
    else:
        st.subheader(" 💓 You heart health seems to be okay.")
        st.markdown("<div style='padding: 5px'></div>", unsafe_allow_html=True)
        st.image("images/good.jpg")
        st.markdown("""
            Based on the responses you provided, it seems that you do not have any heart diseases. However, it is important to maintain a healthy lifestyle to prevent the development of heart diseases and maintain good health.

            Regular exercise, a balanced and nutritious diet, and sufficient rest are all essential components of a healthy lifestyle. Engaging in physical activity for at least 30 minutes a day can help strengthen your heart, lungs, and muscles, and reduce your risk of developing chronic conditions such as heart disease, obesity, and type 2 diabetes.

            Staying hydrated by drinking plenty of water and avoiding excessive alcohol consumption and smoking can also benefit your overall health. 

            Remember that making healthy choices can have long-term benefits for your physical and mental health.
        """)

