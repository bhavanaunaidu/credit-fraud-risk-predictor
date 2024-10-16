import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# loading the dataset to a Pandas DataFrame
credit_card_data = pd.read_csv('/mnt/c/Users/bhanu/OneDrive/Desktop/project/credit_data.csv')

# first 5 rows of the dataset
print(credit_card_data.head())

# dataset information
credit_card_data.info()

# checking the number of missing values in each column
print(credit_card_data.isnull().sum())

# distribution of legit (non-default) transactions & fraudulent (default) transactions
print(credit_card_data['default'].value_counts())

# separating the data for analysis
legit = credit_card_data[credit_card_data.default == 0]
fraud = credit_card_data[credit_card_data.default == 1]

print(f"Legit shape: {legit.shape}")
print(f"Fraud shape: {fraud.shape}")

# statistical measures of the data
print(legit.loan.describe())
print(fraud.loan.describe())

# compare the values for both transactions
print(credit_card_data.groupby('default').mean())

# undersample the legit transactions
legit_sample = legit.sample(n=fraud.shape[0])
new_dataset = pd.concat([legit_sample, fraud], axis=0)

print(new_dataset['default'].value_counts())
print(new_dataset.groupby('default').mean())

# splitting the data into features and target
X = new_dataset.drop(columns='default', axis=1)
Y = new_dataset['default']

# splitting the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

print(f"X shape: {X.shape}")
print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")

# Logistic Regression model
model = LogisticRegression()

# training the model
model.fit(X_train, Y_train)

# accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Accuracy on Training data:', training_data_accuracy)

# accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy on Test data:', test_data_accuracy)
