import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics  import mean_squared_error as mse
import pickle

#reading the csv and saving it as a dataframe
df = pd.read_csv('../csv/admission.csv', index_col=0)

#renaming the columns according to our flexibility
df.columns = df.columns.str.lower()
df = df.rename(columns= {'chance of admit ': 'admission_chance'})

#separating the feaures and target
X = df.drop('admission_chance', axis=1)
y = df['admission_chance']

#spliting the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

#fitting the model
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

#accuracy is being measured by means of root mean squared error
print(np.sqrt(mse(y_test, predictions)))

pickle.dump(model, open("model.pkl","wb"))
