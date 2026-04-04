import streamlit as st
import pandas as pd
import joblib

# --- Page Config ---
st.set_page_config(
    page_title="Diabetes Risk Predictor",
    page_icon="💉",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Load Model ---
pipeline = joblib.load("pipeline.pkl")  # your trained model

# --- App Title ---
st.title("💉 Diabetes Risk Prediction")
st.markdown("""
This model was trained on the Diabetes Health Indicators Dataset from the **2015 BRFSS dataset**. 
It predicts whether an individual has **Prediabetes/Diabetes** or **No Diabetes** 
using key health and lifestyle indicators.
            
**Classes:**  
0 = No Diabetes  
1 = Prediabetes / Diabetes
""")

# --- Sidebar Inputs ---
st.sidebar.header("Individual Information")

# Sidebar mostly for categorical/profile inputs
HighChol = st.sidebar.selectbox("High Cholesterol", ["Yes", "No"])
CholCheck = st.sidebar.selectbox("Cholesterol Checked", ["Yes", "No"])
HeartDiseaseorAttack = st.sidebar.selectbox("Heart Disease or Attack", ["Yes", "No"])
Fruits = st.sidebar.selectbox("Consumes Fruits Daily", ["Yes", "No"])
HvyAlcoholConsump = st.sidebar.selectbox("Heavy Alcohol Consumption", ["Yes", "No"])
DiffWalk = st.sidebar.selectbox("Difficulty Walking", ["Yes", "No"])
Sex = st.sidebar.selectbox("Sex", ["Male", "Female"])

# Age, Education, Income
age_options = {
    "18-24": 1, "25-29": 2, "30-34": 3, "35-39": 4,
    "40-44": 5, "45-49": 6, "50-54": 7, "55-59": 8,
    "60-64": 9, "65-69": 10, "70-74": 11, "75-79": 12, "80+": 13
}
Age = st.sidebar.selectbox("Age Category", list(age_options.keys()))
Age = age_options[Age]

education_options = {
    "Never attended school / only kindergarten": 1,
    "Grades 1-8": 2,
    "Grades 9-11": 3,
    "Grade 12 / GED": 4,
    "Some college / technical school": 5,
    "College graduate or higher": 6
}
Education = st.sidebar.selectbox("Education Level", list(education_options.keys()))
Education = education_options[Education]

income_options = {
    "Less than $10,000": 1, "$10,000 - $15,000": 2, "$15,000 - $20,000": 3,
    "$20,000 - $25,000": 4, "$25,000 - $35,000": 5, "$35,000 - $50,000": 6,
    "$50,000 - $75,000": 7, "$75,000 or more": 8
}
Income = st.sidebar.selectbox("Income Level", list(income_options.keys()))
Income = income_options[Income]

# --- Main Panel Inputs (side by side) ---
st.subheader("Health & Lifestyle Information")
col1, col2 = st.columns(2)

with col1:
    BMI = st.number_input("BMI", 0.0, 70.0, 25.0)
    MentHlth = st.slider("Mental Health (days in past 30)", 0, 30, 0)

with col2:
    genhlth_options = {"Excellent":1, "Very Good":2, "Good":3, "Fair":4, "Poor":5}
    GenHlth_label = st.selectbox("General Health", list(genhlth_options.keys()))
    GenHlth = genhlth_options[GenHlth_label]
    PhysHlth = st.slider("Physical Health (days in past 30)", 0, 30, 0)

# --- Binary encoding ---
HighChol = 1 if HighChol == "Yes" else 0
CholCheck = 1 if CholCheck == "Yes" else 0
HeartDiseaseorAttack = 1 if HeartDiseaseorAttack == "Yes" else 0
Fruits = 1 if Fruits == "Yes" else 0
HvyAlcoholConsump = 1 if HvyAlcoholConsump == "Yes" else 0
DiffWalk = 1 if DiffWalk == "Yes" else 0
Sex = 1 if Sex == "Male" else 0

# --- Prepare Data ---
input_df = pd.DataFrame([{
    'HighChol': HighChol,
    'CholCheck': CholCheck,
    'BMI': float(BMI),
    'HeartDiseaseorAttack': HeartDiseaseorAttack,
    'Fruits': Fruits,
    'HvyAlcoholConsump': HvyAlcoholConsump,
    'GenHlth': int(GenHlth),
    'MentHlth': int(MentHlth),
    'PhysHlth': int(PhysHlth),
    'DiffWalk': DiffWalk,
    'Sex': Sex,
    'Age': int(Age),
    'Education': Education,
    'Income': Income
}])

# --- Prediction ---
if st.button("📊 Predict Diabetes Risk"):
    prediction = pipeline.predict(input_df)
    prediction_proba = pipeline.predict_proba(input_df)

    prob_no = prediction_proba[0][0]
    prob_yes = prediction_proba[0][1]

    pred_class = prediction[0]
    status_map = {0: "No Diabetes", 1: "Prediabetes / Diabetes"}
    description_map = {0: "Individual is likely healthy.", 1: "Individual may have prediabetes or diabetes."}

    # --- Prediction Box ---
    background_color = "#e74c3c" if pred_class == 1 else "#2ecc71"
    st.subheader("Prediction")
    st.markdown(
        f"""
        <div style='
            background-color:{background_color};
            padding:15px;
            border-radius:8px;
            color:white;
            font-size:20px;
            font-weight:bold;
            text-align:center;
        '>
        Prediction: {status_map[pred_class]}
        </div>
        """, unsafe_allow_html=True
    )
    st.markdown(f"**Interpretation:** {description_map[pred_class]}")

    # --- Risk Probability ---
    st.subheader("Risk Probability")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("No Diabetes Probability", f"{prob_no*100:.2f}%")
    with col2:
        st.metric("Prediabetes / Diabetes Probability", f"{prob_yes*100:.2f}%")

    # --- Risk Level ---
    st.subheader("Risk Level")
    st.progress(int(prob_yes*100))

    if prob_yes > 0.65:
        st.markdown(f"""
        <div style="background-color:#e74c3c;padding:15px;border-radius:8px;color:white;font-size:18px;font-weight:bold;text-align:center;">
        🔥 High Risk
        </div>
        """, unsafe_allow_html=True)
    elif prob_yes > 0.35:
        st.markdown(f"""
        <div style="background-color:#f1c40f;padding:15px;border-radius:8px;color:black;font-size:18px;font-weight:bold;text-align:center;">
        ⚡ Moderate Risk
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style="background-color:#2ecc71;padding:15px;border-radius:8px;color:white;font-size:18px;font-weight:bold;text-align:center;">
        🌿 Low Risk
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.caption("Diabetes Risk Prediction Model | Machine Learning Deployment")
