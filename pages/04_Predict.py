#Importing the libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from IPython.display import display

#Loading the data
data = pd.read_csv ('frozen3.csv')
#display(data.head())

#data.info()

#display(data['status'].value_counts())

X = data.drop (columns=['id','HN','status','fvisit'], axis=1)
Y = data ['status']

print(X)

print(Y)

X_train, X_test, Y_train, Y_test = train_test_split (X, Y, test_size=0.2, stratify=Y, random_state=2)
print (X.shape, X_train.shape, X_test.shape)

model = LogisticRegression()
# Training the LogisticRegression model with the Training data
model.fit (X_train.values, Y_train)

# Predicting the output with test data
y_pred=model.predict (X_test.values)
print (y_pred)

#Calculating the accuracy of the predicted outcome
print (accuracy_score (Y_test,y_pred))

input_data = ( 1, 2, 1, 150, 180, 30, 0, 0, 0, 0, 0, 150, 180, 30, 0, 0, 0, 0, 40, 60, 20, 0, 0, 0, 0, 40, 60, 20, 0, 0, 0)
# Change the input data to a numpy array
numpy_data= np.asarray (input_data)
# reshape the numpy array as we are predicting for only on instance
input_reshaped = numpy_data.reshape (1,-1)
prediction = model.predict (input_reshaped)
if (prediction[0]== 0):  
	print ('The Person does recover')
else:  
	print ('The Person does poor')

#Saving the trained model
import pickle
filename = 'trained_model.sav'
#dump=save your trained model
pickle.dump (model,open (filename,'wb'))
#loading the saved model
loaded_model = pickle.load (open ('trained_model.sav','rb'))