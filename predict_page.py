import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('model_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor_loaded = data['model']
le_age = data['le_age']
le_work = data['le_work']
le_education = data['le_education']
le_country = data['le_country']
le_industry = data['le_industry']

# define the page
def show_predict_page():
    st.title("Software Developer Salary Prediction") # title
    
    st.write("""### We need some information to predict the salary""")
    
    age = (
        "25-34 years old",
        "35-44 years old",
        "45-54 years old",
        "18-24 years old",
        "55-64 years old",
        "65 years or older"
    )
    
    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad"
    )
    
    industry = (
        "IT, Software Development, Technology",
        "Manufacturing, Transportation, Supply",
        "Retail and Consumer Services",
        "Advertising Services",
        "Financial Services",
        "Higher Education",
        "Legal Services",
        "Healthcare",
        "Oil & Gas",
        "Insurance",
        "Wholesale",
        "Other",
    )
    
    remotework = (
        "In-person",
        "Hybrid",
        "Remote"
    )
    
    countries = (
        "United States",
        "Germany",
        "United Kingdom",
        "India",
        "Canada",
        "France",
        "Brazil",
        "Netherlands",
        "Spain",
        "Australia",
        "Italy",
        "Poland",
        "Sweden",
        "Switzerland",
        "Israel",
        "Portugal",
        "Denmark",
        "Austria",
        "Finland",
        "Norway",
        "Russian"
    )
    
    
    age = st.selectbox("Age", age)
    
    # education select box
    education = st.selectbox("Education Level", education)
    
    industry = st.selectbox("Industry", industry)
    
    remotework = st.selectbox("RemoteWork", remotework)
    
    # Select box to choose from it your country in the interface:
    country = st.selectbox("Country", countries)
 
    # Experience:
    experience = st.slider("Years of Experience", 0, 50, 3 ) #default value, max value, min value
    
    
    # Prediction button
    ok = st.button("Calculate Salary")
    
    if ok:
        X = np.array([[age, remotework, education, experience, country, industry]])
        X[:, 0] = le_age.transform(X[:,0])
        X[:, 1] = le_work.transform(X[:,1])
        X[:, 2] = le_education.transform(X[:,2])
        X[:, 4] = le_country.transform(X[:,4])
        X[:, 5] = le_industry.transform(X[:,5])
        X = X.astype(float)
        
        # calculate the prediction
        salary = regressor_loaded.predict(X)
        # display the prediction 
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")
