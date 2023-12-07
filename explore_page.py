import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Process functions
def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map

def clear_experience(x):
    if x == 'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post grad'
    return 'Less than a Bachelors'




# all the steps we did in data processing
@st.cache_data # exicute it one time and will be save for other times
def load_data():
    df = pd.read_csv('data/survey_results_public.csv')
    df = df[['Country', 'EdLevel', 'YearsCodePro', 'Employment', 'ConvertedCompYearly']]

    df = df[df["ConvertedCompYearly"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed, full-time"]
    df = df.drop("Employment", axis = 1)
    
    country_map = shorten_categories(df.Country.value_counts(), 300)
    df["Country"] = df["Country"].map(country_map)
    df = df[df["ConvertedCompYearly"] <= 250000]
    df = df[df["ConvertedCompYearly"] >= 10000]
    df = df[df["Country"] != "Other"]
    
    df["YearsCodePro"] = df["YearsCodePro"].apply(clear_experience)
    df["EdLevel"] = df["EdLevel"].apply(clean_education)
    df = df.rename({"ConvertedCompYearly": "Salary"}, axis = 1)
   
    return df




df = load_data()


# display page
def show_explore_page():
    st.title("Explore Software Engineer Salaries")
    
    st.write(
        """
        ### Stack Overflow Developer Survey 2023
    """
    )
    
    data = df["Country"].value_counts()[:10]
    
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels = data.index, autopct = "%1.1f%%", startangle = 90)
    ax1.axis("equal")
    
    st.write("""### Number of Data from different countries""")
    
    # plot the figure using streamlit: plt plots
    st.pyplot(fig1)
    
    st.write(
        """
    ### Mean Salary Based On Country
    """
    )
    
    data = df.groupby(['Country'])['Salary'].mean().sort_values(ascending=True)
    st.bar_chart(data)
    
    st.write(
        """
    ### Mean Salary Based on Experience
    """
    )
    
    data = df.groupby(['YearsCodePro'])['Salary'].mean().sort_values(ascending=True)
    st.line_chart(data)
    