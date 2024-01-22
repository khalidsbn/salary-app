import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

# side bar
page = st.sidebar.selectbox("Explore or Predict", ("Predict", "Explore"))

if page == "Predict":
    # exicute the page
    show_predict_page()
else:
    show_explore_page()
