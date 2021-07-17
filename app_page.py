#Import Libraries
import streamlit as st
from PIL import Image
from predictionpage import show_predict_page
from explorepage import show_explore_page
from visualisationpag import show_visual_page

st.title("DATA SCIENCE STUDENT PERFORMANCE ANALYSIS PROJECT")
st.markdown("")
st.image("Data_Science.jpg",width=300)
page = st.sidebar.selectbox("STUDENT ACADEMIC PERFORMANCE ANALYSIS", ("Data Exploration", 'Data Visualisation', "Data Prediction"))

if page == "Data Exploration":
	show_explore_page()
elif page == "Data Visualisation":
	show_visual_page()
else:
	show_predict_page()

