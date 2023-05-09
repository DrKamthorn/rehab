#Importing the libraries
import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load (open ("/Users/kamthorntan/rehab/pages/trained_model.sav", 'rb'))

input_data = ( 1, 2, 1, 150, 180, 30, 0, 0, 0, 0, 0, 150, 180, 30, 0, 0, 0, 0, 40, 60, 20, 0, 0, 0, 0, 40, 60, 20, 0, 0, 0)
#Creating a function for Prediction
def fz_prediction (input_data):
# changing the input data to a numpy array
	numpy_data= np.asarray (input_data)
#Reshaping the numpy array as we are predicting for only on instance
	input_reshaped = numpy_data.reshape (1,-1)
	prediction = loaded_model.predict (input_reshaped)
	if (prediction[0] == 0):
		st.success ('The person does RECOVER')
	else:
		st.warning ('The person does NOT recover')
#Adding title to the page
st.title ('Frozen Shoulder Prediction Web App')

#Getting the input data from the user
#age = st.text_input ('Age in Years')
gender = st.text_input ('Gender : 1 – female, 2 – male')
Dx = st.text_input ('Dx : 1 - Frozen shoulder, 2 - Adhesive capsulitis, 3 - Others')
side = st.text_input ('Side : 1 - Rt, 2 - Lt, 3 - Both')
F1 = st.number_input ('F1 in number')
F10 = st.number_input ('F10 in number')
F101 = st.number_input ('F10-F1 in number')
F20 = st.number_input ('F20 in number')
F201 = st.number_input ('F20-F1 in number')
F30 = st.number_input ('F30 in number')
F40 = st.number_input ('F40 in number')
F401 = st.number_input ('F40-F1 in number')
AB1 = st.number_input ('AB1 in number')
AB10 = st.number_input ('AB10 in number')
AB101 = st.number_input ('AB10-AB1 in number')
AB20 = st.number_input ('AB20 in number')
AB201 = st.number_input ('AB20-AB1 in number')
AB30 = st.number_input ('AB30 in number')
AB40 = st.number_input ('AB40 in number')
IR1 = st.number_input ('IR1 in number')
IR10 = st.number_input ('IR10 in number')
IR101 = st.number_input ('IR10-IR1 in number')
IR20 = st.number_input ('IR20 in number')
IR201 = st.number_input ('IR20-1 in number')
IR30 = st.number_input ('IR30 in number')
IR40 = st.number_input ('IR40 in number')
ER1 = st.number_input ('ER1 in number')
ER10 = st.number_input ('ER10 in number')
ER101 = st.number_input ('ER10-ER1 in number')
ER20 = st.number_input ('ER20 in number')
ER201 = st.number_input ('ER20-ER1 in number')
ER30 = st.number_input ('ER30 in number')

#
# code for Prediction
#diagnosis = ‘ ‘
# creating a button for Prediction
if st.button ('Frozen Shoulder Test Result'):
	diagnosis=fz_prediction ([gender,Dx,side,F1,F10,F101, F20, F201, F30, F40, F401, AB1, AB10, AB101, AB20, AB201, AB30, AB40, IR1, IR10, IR101, IR20, IR201, IR30, IR40, ER1, ER10, ER101, ER20, ER201, ER30])