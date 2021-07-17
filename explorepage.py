import streamlit as st
import pandas as pd
import numpy as np
import pandas_profiling
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

def show_explore_page():
	st.title("Exploration Page")
	Data = pd.read_csv("student_performance.csv")
	st.header("*Now let's explain every column in the dataframe")
	st.markdown("- `school` : student's school (binary: GP or MS)")
	st.markdown("- `sex` : student's sex (binary: F - female or M - male)")
	st.markdown("- `age` : student's age (numeric: from 15 to 22)")
	st.markdown("- `address` : student's home address type (binary: U - urban or R - rural)")
	st.markdown("- `famsize` : family size (binary: LE3 - less or equal to 3 or GT3 - greater than 3)")
	st.markdown("- `Pstatus` : parent's cohabitation status (binary: T - living together or A - apart)")
	st.markdown("- `Medu` : mother's education (numeric: 0 - none,  1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education or 4 - higher education)")
	st.markdown("- `Fedu` : father's education (numeric: 0 - none,  1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education or 4 - higher education)")
	st.markdown("- `Mjob` : mother's job (nominal: teacher, health care related, civil services (e.g. administrative or police), at_home or other)")
	st.markdown("- `Fjob` : father's job (nominal: teacher, health care related, civil services (e.g. administrative or police), at_home or other)")
	st.markdown("- `reason` : reason to choose this school (nominal: close to home, school reputation, course preference or other)")
	st.markdown("- `guardian` : student's guardian (nominal: mother, father or other)")
	st.markdown("- `traveltime` : home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour)")
	st.markdown("- `studytime` : weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)")
	st.markdown("- `failures` : number of past class failures (numeric: n if 1<=n<3, else 4)")
	st.markdown("- `schoolsup` : extra educational support (binary: yes or no)")
	st.markdown("- `famsup` : family educational support (binary: yes or no)")
	st.markdown("- `paid` : extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)")
	st.markdown("- `activities` : extra-curricular activities (binary: yes or no)")
	st.markdown("- `nursery` : attended nursery school (binary: yes or no)")
	st.markdown("- `higher` : wants to take higher education (binary: yes or no)")
	st.markdown("- `internet` : Internet access at home (binary: yes or no)")
	st.markdown("- `romantic` : with a romantic relationship (binary: yes or no)")
	st.markdown("- `famrel` : quality of family relationships (numeric: from 1 - very bad to 5 - excellent)")
	st.markdown("- `freetime` : free time after school (numeric: from 1 - very low to 5 - very high)")
	st.markdown("- `goout` : going out with friends (numeric: from 1 - very low to 5 - very high)")
	st.markdown("- `Dalc` : workday alcohol consumption (numeric: from 1 - very low to 5 - very high)")
	st.markdown("- `Walc` : weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)")
	st.markdown("- `health` : current health status (numeric: from 1 - very bad to 5 - very good)")
	st.markdown("- `absences` : number of school absences (numeric: from 0 to 93)")
	st.markdown("- `passed` : did the student pass the final exam or not (binary: yes or no)")
	st.write(Data.head())

	st.write(Data.describe())


	profile = ProfileReport(Data,title="Student_Report")
	st_profile_report(profile)








