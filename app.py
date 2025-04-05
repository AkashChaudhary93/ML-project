import streamlit as st
import joblib
import pandas as pd

# Load trained models
college_model = joblib.load("college_predictor.pkl")
salary_model = joblib.load("salary_predictor.pkl")

st.title("🎓 Career Predictor App")
st.markdown("Predict your **college** and **expected salary** based on your profile.")

# Input fields
tenth = st.number_input("10th %", min_value=0.0, max_value=100.0, step=0.1)
twelfth = st.number_input("12th %", min_value=0.0, max_value=100.0, step=0.1)
jee_rank = st.number_input("JEE Rank", min_value=1, step=1)
work_exp = st.number_input("Work Experience (years)", min_value=0, step=1)
field_exp = st.number_input("Field Experience (years)", min_value=0, step=1)
projects = st.number_input("Number of Projects", min_value=0, step=1)
expertise = st.slider("Expertise Level (1-5)", 1, 5)
internships = st.number_input("Number of Internships", min_value=0, step=1)
soft_skills = st.slider("Soft Skill Rating (1-5)", 1, 5)
aptitude = st.slider("Aptitude Rating (1-5)", 1, 5)
dsa_level = st.slider("DSA Level (1-5)", 1, 5)
hackathons = st.number_input("Hackathons Participated", min_value=0, step=1)
coding_qs = st.number_input("Competitive Coding Questions Solved", min_value=0, step=1)
repos = st.number_input("Number of GitHub Repositories", min_value=0, step=1)
github_acts = st.number_input("GitHub Contributions", min_value=0, step=1)
linkedin_posts = st.number_input("LinkedIn Posts", min_value=0, step=1)
certifications = st.number_input("Number of Certifications", min_value=0, step=1)
cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.01)

# Keep as strings — do not encode manually
gender = st.selectbox("Gender", ["Male", "Female"])
domain = st.selectbox("Preferred Domain", ["Full Stack", "Data Science", "AI", "Cybersecurity", "Other"])
referral = st.selectbox("Got Referral?", ["Yes", "No"])

# Define DataFrame with original column names used during training
features_df = pd.DataFrame([{
    '10th_percent': tenth,
    '12th_percent': twelfth,
    'jee_rank': jee_rank,
    'experience': work_exp,
    'experience_field': field_exp,
    'num_projects': projects,
    'expertise_level': expertise,
    'num_internships': internships,
    'soft_skill_rating': soft_skills,
    'aptitude_rating': aptitude,
    'dsa_level': dsa_level,
    'num_hackathons': hackathons,
    'competitive_coding_solved': coding_qs,
    'num_repos': repos,
    'github_activities': github_acts,
    'linkedin_posts': linkedin_posts,
    'num_certifications': certifications,
    'cgpa': cgpa,
    'gender': gender,
    'domain': domain,
    'referral': referral
}])

# Predict on button click
if st.button("Predict"):
    try:
        college = college_model.predict(features_df)[0]
        salary = salary_model.predict(features_df)[0]

        st.success(f"🎓 **Predicted College Tier:** {college}")
        st.success(f"💰 **Expected Salary:** ₹{salary:,.2f}")
    except Exception as e:
        st.error(f"⚠️ Prediction failed: {e}")











# import streamlit as st
# import joblib
# import numpy as np

# # Load the trained models
# college_model = joblib.load("college_predictor.pkl")
# salary_model = joblib.load("salary_predictor.pkl")

# st.title("🎓 Career Predictor App")
# st.markdown("Predict your **college** and **salary** based on your profile.")

# # Input fields
# tenth = st.number_input("10th %", min_value=0.0, max_value=100.0)
# twelfth = st.number_input("12th %", min_value=0.0, max_value=100.0)
# jee_rank = st.number_input("JEE Rank", min_value=1)
# work_exp = st.number_input("Work Experience (years)", min_value=0)
# field_exp = st.number_input("Field Experience (years)", min_value=0)
# projects = st.number_input("No. of Projects", min_value=0)
# expertise = st.slider("Expertise (1-5)", 1, 5)
# internships = st.number_input("Internships", min_value=0)
# soft_skills = st.slider("Soft Skills (1-5)", 1, 5)
# aptitude = st.slider("Aptitude (1-5)", 1, 5)
# dsa_level = st.slider("DSA Level (1-5)", 1, 5)
# hackathons = st.number_input("Hackathons Participated", min_value=0)
# coding_qs = st.number_input("Coding Questions Solved", min_value=0)
# repos = st.number_input("GitHub Repositories", min_value=0)
# github_acts = st.number_input("GitHub Contributions", min_value=0)
# linkedin_posts = st.number_input("LinkedIn Posts", min_value=0)
# certifications = st.number_input("Certifications", min_value=0)
# cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0)

# gender = st.selectbox("Gender", ["Male", "Female"])
# domain = st.selectbox("Domain", ["Full Stack", "Data Science", "AI", "Cybersecurity", "Other"])
# referral = st.selectbox("Referral", ["Yes", "No"])

# # Encoding categorical variables
# gender_encoded = 1 if gender == "Male" else 0
# domain_dict = {"Full Stack": 0, "Data Science": 1, "AI": 2, "Cybersecurity": 3, "Other": 4}
# referral_encoded = 1 if referral == "Yes" else 0

# domain_encoded = domain_dict[domain]

# # Combine all features
# features = np.array([[
#     tenth, twelfth, jee_rank, work_exp, field_exp, projects, expertise, internships,
#     soft_skills, aptitude, dsa_level, hackathons, coding_qs, repos,
#     github_acts, linkedin_posts, certifications, cgpa,
#     gender_encoded, domain_encoded, referral_encoded
# ]])

# # Prediction
# if st.button("Predict"):
#     college = college_model.predict(features)[0]
#     salary = salary_model.predict(features)[0]

#     st.success(f"🎓 Predicted College: {college}")
#     st.success(f"💰 Expected Salary: ₹{salary:,.2f}")
