# Credit-Fraud-Risk-Predictor

This project aims to detect fraudulent transactions from a credit card dataset using a Logistic Regression model. The dataset contains information about credit card loans, and the task is to classify transactions as legit (non-default) or fraudulent (default).

A machine learning project to detect fraudulent (default) vs. legitimate (non-default) credit card transactions using Logistic Regression.

Table of Contents

Overview

Features

Dataset

Installation

Usage

Model

Results

Contributing

License

Overview

Credit card fraud detection is a major financial challenge. This project demonstrates a Logistic Regression model that classifies credit card transactions into legit (non-default) and fraudulent (default) categories. The dataset is balanced using undersampling to ensure fair model training. The workflow includes data preprocessing, feature-target separation, model training, and evaluation.

Features

Detects fraudulent vs. legitimate credit transactions.

Implements Logistic Regression for classification.

Handles data imbalance using undersampling.

Provides accuracy results for both training and testing data.

Dataset

File format: CSV

File name: credit_data.csv

Key column: default (0 = Legit, 1 = Fraudulent)

Other columns include loan-related numerical values.

Data balancing performed by undersampling legit transactions.

Installation
Prerequisites

Ensure you have the following installed:

Python 3.x

NumPy

Pandas

Scikit-learn

Install dependencies:

pip install -r requirements.txt

Usage

Clone the repository:

git clone https://github.com/your-username/Credit-Fraud-Risk-Predictor.git
cd Credit-Fraud-Risk-Predictor


Run the script:

python main.py


Expected outputs:

Dataset summary and statistics.

Distribution of legit vs. fraud transactions.

Model training accuracy and test accuracy.

Model

Algorithm used: Logistic Regression.

Train-test split: 80% training, 20% testing.

Balancing strategy: Undersampling legitimate transactions.

Evaluation metric: Accuracy score.

Results

Reported accuracy on training data.

Reported accuracy on test data.

Fraud detection performance depends on balanced dataset preparation.

Contributing

Contributions are welcome! Please fork this repo, create a branch, and submit a pull request.
