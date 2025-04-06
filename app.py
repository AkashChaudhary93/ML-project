# import streamlit as st
# import joblib
# import pandas as pd

# # Load trained models
# college_model = joblib.load("college_predictor.pkl")
# salary_model = joblib.load("salary_predictor.pkl")

# st.title("🎓 Career Predictor App")
# st.markdown("Predict your **college** and **expected salary** based on your profile.")

# # Input fields
# tenth = st.number_input("10th %", min_value=0.0, max_value=100.0, step=0.1)
# twelfth = st.number_input("12th %", min_value=0.0, max_value=100.0, step=0.1)
# jee_rank = st.number_input("JEE Rank", min_value=1, step=1)
# work_exp = st.number_input("Work Experience (years)", min_value=0, step=1)
# field_exp = st.number_input("Field Experience (years)", min_value=0, step=1)
# projects = st.number_input("Number of Projects", min_value=0, step=1)
# expertise = st.slider("Expertise Level (1-5)", 1, 5)
# internships = st.number_input("Number of Internships", min_value=0, step=1)
# soft_skills = st.slider("Soft Skill Rating (1-5)", 1, 5)
# aptitude = st.slider("Aptitude Rating (1-5)", 1, 5)
# dsa_level = st.slider("DSA Level (1-5)", 1, 5)
# hackathons = st.number_input("Hackathons Participated", min_value=0, step=1)
# coding_qs = st.number_input("Competitive Coding Questions Solved", min_value=0, step=1)
# repos = st.number_input("Number of GitHub Repositories", min_value=0, step=1)
# github_acts = st.number_input("GitHub Contributions", min_value=0, step=1)
# linkedin_posts = st.number_input("LinkedIn Posts", min_value=0, step=1)
# certifications = st.number_input("Number of Certifications", min_value=0, step=1)
# cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.01)

# # Keep as strings — do not encode manually
# gender = st.selectbox("Gender", ["Male", "Female"])
# domain = st.selectbox("Preferred Domain", ["Full Stack", "Data Science", "AI", "Cybersecurity", "Other"])
# referral = st.selectbox("Got Referral?", ["Yes", "No"])

# # Define DataFrame with original column names used during training
# features_df = pd.DataFrame([{
#     '10th_percent': tenth,
#     '12th_percent': twelfth,
#     'jee_rank': jee_rank,
#     'experience': work_exp,
#     'experience_field': field_exp,
#     'num_projects': projects,
#     'expertise_level': expertise,
#     'num_internships': internships,
#     'soft_skill_rating': soft_skills,
#     'aptitude_rating': aptitude,
#     'dsa_level': dsa_level,
#     'num_hackathons': hackathons,
#     'competitive_coding_solved': coding_qs,
#     'num_repos': repos,
#     'github_activities': github_acts,
#     'linkedin_posts': linkedin_posts,
#     'num_certifications': certifications,
#     'cgpa': cgpa,
#     'gender': gender,
#     'domain': domain,
#     'referral': referral
# }])

# # Predict on button click
# if st.button("Predict"):
#     try:
#         college = college_model.predict(features_df)[0]
#         salary = salary_model.predict(features_df)[0]

#         st.success(f"🎓 **Predicted College Tier:** {college}")
#         st.success(f"💰 **Expected Salary:** ₹{salary:,.2f}")
#     except Exception as e:
#         st.error(f"⚠️ Prediction failed: {e}")




import streamlit as st
import joblib
import pandas as pd

# Load trained models
college_model = joblib.load("college_predictor.pkl")
salary_model = joblib.load("salary_predictor.pkl")

# Custom CSS for styling
st.markdown("""
    <style>
    .main-title {
        font-size: 200px;  /* Larger heading */
        color: #2c3e50;
        text-align: center;
        font-weight: bold;
    }
    .subtitle {
        font-size: 20px;
        color: #7f8c8d;
        text-align: center;
        margin-bottom: 30px;
    }
    .section-header {
        font-size: 28px;
        color: #2980b9;
        margin-top: 20px;
        font-weight: bold;
    }
    .stButton>button {
        background-color: #27ae60;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
    }
    .stSuccess {
        font-size: 20px;
        font-weight: bold;
    }
    .sidebar .sidebar-content {
        background-color: #2c3e50;
        color: white;
    }
    .sidebar .sidebar-content a {
        color: #e74c3c;
    }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown('<p class="main-title">🎓 Career Predictor Pro</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Unlock Your Future: Predict Your College Tier & Expected Salary</p>', unsafe_allow_html=True)

# Sidebar with Predictor, About, and Help
with st.sidebar:
    st.markdown('<h2 style="color: white;">Navigation</h2>', unsafe_allow_html=True)
    st.image("https://via.placeholder.com/150", caption="Your Career Journey", use_container_width=True)
    
    # Predictor Section
    st.markdown("### 📊 Predictor")
    st.write("Enter your academic and professional details to get personalized predictions!")
    
    # About Section
    st.markdown("### ℹ️ About")
    st.write("Learn more about Career Predictor Pro and how it can guide your career path.")
    
    # Help Section
    st.markdown("### ❓ Help")
    st.write("Need assistance? Find FAQs or contact support for guidance.")
    
    st.markdown("Built with ❤️ by [Your Name]")

# Tabs for better organization
tab1, tab2, tab3 = st.tabs(["📚 Academic Details", "💼 Professional Details", "🔍 Predictions"])

# Academic Details Tab
with tab1:
    st.markdown('<p class="section-header">📚 Academic Background</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        tenth = st.number_input("10th % 📖", min_value=0.0, max_value=100.0, step=0.1, help="Your 10th grade percentage")
        twelfth = st.number_input("12th % 📘", min_value=0.0, max_value=100.0, step=0.1, help="Your 12th grade percentage")
        jee_rank = st.number_input("JEE Rank 🏆", min_value=1, step=1, help="Your JEE rank")
    
    with col2:
        cgpa = st.number_input("CGPA 🎓", min_value=0.0, max_value=10.0, step=0.01, help="Your college CGPA")
        certifications = st.number_input("Certifications 🏅", min_value=0, step=1, help="Number of certifications earned")
    
    st.progress(min(tenth / 100, 1.0), text="10th % Progress")
    st.progress(min(twelfth / 100, 1.0), text="12th % Progress")

# Professional Details Tab
with tab2:
    st.markdown('<p class="section-header">💼 Professional Experience</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        work_exp = st.number_input("Work Experience (years) 🕒", min_value=0, step=1, help="Years of work experience")
        field_exp = st.number_input("Field Experience (years) 🌐", min_value=0, step=1, help="Years in your domain")
        projects = st.number_input("Projects Completed 🚀", min_value=0, step=1, help="Number of projects")
        internships = st.number_input("Internships 🎯", min_value=0, step=1, help="Number of internships")
        hackathons = st.number_input("Hackathons 🖥️", min_value=0, step=1, help="Hackathons participated")
    
    with col2:
        expertise = st.slider("Expertise Level (1-5) 🌟", 1, 5, help="Rate your expertise")
        soft_skills = st.slider("Soft Skills (1-5) 🤝", 1, 5, help="Rate your soft skills")
        aptitude = st.slider("Aptitude (1-5) 🧠", 1, 5, help="Rate your aptitude")
        dsa_level = st.slider("DSA Level (1-5) 💻", 1, 5, help="Data Structures & Algorithms level")
        coding_qs = st.number_input("Coding Questions Solved 🧩", min_value=0, step=1, help="Competitive coding questions")
    
    st.markdown("### Online Presence")
    repos = st.number_input("GitHub Repos 📂", min_value=0, step=1, help="Number of GitHub repositories")
    github_acts = st.number_input("GitHub Contributions 🌍", min_value=0, step=1, help="Total GitHub contributions")
    linkedin_posts = st.number_input("LinkedIn Posts 📝", min_value=0, step=1, help="Number of LinkedIn posts")

# Predictions Tab
with tab3:
    st.markdown('<p class="section-header">🔍 Your Profile</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        gender = st.selectbox("Gender 👤", ["Male", "Female"], help="Select your gender")
        domain = st.selectbox("Preferred Domain 🌐", ["Full Stack", "Data Science", "AI", "Cybersecurity", "Other"], help="Your career domain")
    
    with col2:
        referral = st.selectbox("Got Referral? 🤝", ["Yes", "No"], help="Do you have a referral?")
    
    # DataFrame for prediction
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
    
    # Predict Button
    if st.button("🚀 Predict My Future"):
        with st.spinner("Analyzing your profile..."):
            try:
                college = college_model.predict(features_df)[0]
                salary = salary_model.predict(features_df)[0]
                
                st.markdown("### 🎉 Prediction Results")
                st.success(f"🎓 **Predicted College Tier:** {college}")
                st.success(f"💰 **Expected Salary:** ₹{salary:,.2f}")
                
                # Visualization
                st.bar_chart({"College Tier": [college], "Salary (Lakhs)": [salary / 100000]})
            except Exception as e:
                st.error(f"⚠️ Oops! Something went wrong: {e}")

# Footer
st.markdown("---")
st.write("© 2025 Career Predictor Pro | Powered by Streamlit")