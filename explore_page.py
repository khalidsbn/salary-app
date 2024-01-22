import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data/df_cleaned.csv')

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
    