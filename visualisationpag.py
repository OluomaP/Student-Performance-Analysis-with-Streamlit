#import Libraries
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

def show_visual_page():
	#Giving a title 
	st.title("Visualisation Page")
	#get the data
	Data = pd.read_csv("student_performance.csv")

	st.title("Student Performance Dashboard")
	st.header('This dashboard will visualize the Student Performance Dataset')
	
	
	st.image("Sex_Grade.jpg",use_column_width=True)
	st.markdown("This chart shows that Male performed better than Female. 60% of Male got an A and a B respectively while 100% of the Female Got a D")
	st.image("Passed.jpg")
	st.markdown("This Chart is the Percentage of those that passed to those that failed")
	st.image("study_travel_grade.jpg")
	st.markdown("This Chart shows that those that devote themselves more to their study performed better than those that traveled more")
	st.image("Romantic_by_Grade.jpg")
	st.markdown("This Chart shows that student who has no romantic interest performed better by 5%")
	st.image("Passed_by_sex.jpg",use_column_width=True)
	st.markdown("This Chart shows that Females performed better in total than the Male")
	st.image("Grade_by_internet.jpg",use_column_width=True)
	st.image("Grade_by_School.jpg",use_column_width=True)


	fig1 = plt.figure(figsize=(16,10))
	sns.countplot(
		y="Sex",hue="School",data=Data
		)
	st.pyplot(fig1)

	fig2 = plt.figure(figsize=(16,10))
	sns.countplot(Data['Total'], palette = 'BuPu')
	plt.title(
			'Comparison of math scores', fontweight = 30, fontsize = 20
			)
	plt.xlabel(
			'score'
			)
	plt.ylabel(
			'count'
			)
	plt.xticks(
			rotation = 90
			)
	st.pyplot(fig2)
