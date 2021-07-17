import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


from sklearn import preprocessing
label_encoding = preprocessing.LabelEncoder()

def show_predict_page():
	#Get the Data
	Data = pd.read_csv("student_performance.csv")
	data= Data


    #Transform the Dataset through Label_encoding into 1s and 0s
	data["Sex"] = label_encoding.fit_transform(data["Sex"].astype(str))
	data["School"] = label_encoding.fit_transform(data["School"].astype(str))
	data["Pstatus"] = label_encoding.fit_transform(data["Pstatus"].astype(str))
	data["Mjob"] = label_encoding.fit_transform(data["Mjob"].astype(str))
	data["Fjob"] = label_encoding.fit_transform(data["Fjob"].astype(str))
	data["Reason"] = label_encoding.fit_transform(data["Reason"].astype(str))
	data["Guardian"] = label_encoding.fit_transform(data["Guardian"].astype(str))
	data["Famsup"] = label_encoding.fit_transform(data["Famsup"].astype(str))
	data["Paid"] = label_encoding.fit_transform(data["Paid"].astype(str))
	data["Activities"] = label_encoding.fit_transform(data["Activities"].astype(str))
	data["Internet"] = label_encoding.fit_transform(data["Internet"].astype(str))
	data["Romantic"] = label_encoding.fit_transform(data["Romantic"].astype(str))
	data["GRADE"] = label_encoding.fit_transform(data["GRADE"].astype(str))
	data["PASSED"] = label_encoding.fit_transform(data["PASSED"].astype(str))

    #Dropping unnecessary columns
	data.drop(data.columns[[4,5,7,8,9,10,11,12,16,17,20,21,24]], axis =1 , inplace= True)
	array = data.values
	X = array[:,0:23]
	Y = array[:,24]
	test_size = 0.33
	seed = 7

    #Split the data into the training and test set
	X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)

    #Get the features
	School = st.selectbox("School", options=['GP','MS'])
	Sex = st.selectbox("Sex",options=['F','M'])
	Age= st.slider("Age" ,min_value=16,max_value=20)
	Traveltime=st.slider("Traveltime", min_value=1,max_value=3)
	Studytime=st.slider("Studytime", min_value=1,max_value=3)
	Failures=st.slider("Failures", min_value=0,max_value=2)
	Paid=st.selectbox("Paid",options=['True','False'])
	Activities=st.selectbox("Activities",options=['True','False'])
	Internet=st.selectbox("Internet",options=['True','False'])
	Romantic=st.selectbox("Romantic",options=['True','False'])
	Freetime=st.slider("Freetime", min_value=1,max_value=5)
	Goout=st.slider("Goout", min_value=1,max_value=5)
	Dalc=st.slider("Dalc", min_value=1,max_value=5)
	Walc=st.slider("Walc", min_value=1,max_value=5)
	Health=st.slider("Health", min_value=1,max_value=5)
	Absences=st.slider("Absences", min_value=0,max_value=16)
	Predict = st.button("Predict")

	
    #Store the dictionary into a variable
	show_predict_page = {
	"School":School,
	"Sex":Sex,
	"Age":Age,
	"Traveltime":Traveltime,
	"Studytime":Studytime,
	"Failures":Failures,
	"Paid":Paid,
	"Activities":Activities,
	"Internet" :Internet,
	"Romantic":Romantic,
	"Freetime":Freetime,
	"Goout":Goout,
	"Dalc":Dalc,
	"Walc":Walc,
	"Health":Health,
	"Absences":Absences,
	}

    #transform the data into a data frame
	report_data=pd.DataFrame(show_predict_page,index=[0])
	return report_data

    #Store the user input into the show predict page variable
	user_input = show_predict_page()


    #Set a subheader and display the user_input
	st.subheader("Show Prediction")
	st.button(user_input)
	
	#Create and train model 
	model = LogisticRegression()
	model.fit(X_train, Y_train)

	st.subheader("Model Metrices:")
	st.write(str(accuracy_score(Y_test, LogisticRegressor.predict(X_test))*100)+"%")
	
	#Store the models prediction in a variable
	Predict = LogisticRegression.predict(user_input)
	st.subheader("STudent Academic Performance: ")
	output=""
	st.write(Predict)
	if Predict[0] == 1:
		output = "Student Has A High Probability of Passing the Exam"
	else:
		output = "Student Has A High Probability of Failing The Exam"
	st.write(output   )




	








