# Credit-Fraud-Risk-Predictor

This project aims to detect fraudulent transactions from a credit card dataset using a Logistic Regression model. The dataset contains information about credit card loans, and the task is to classify transactions as legit (non-default) or fraudulent (default).

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model](#model)
- [Results](#results)
- [License](#license)

## Project Overview
Credit card fraud is a significant issue in the financial sector. This project focuses on building a binary classification model to predict whether a credit card transaction is legitimate or fraudulent. The model is built using logistic regression, and we balance the dataset using undersampling techniques to handle the imbalance between legitimate and fraudulent transactions.

## Dataset
The dataset used in this project contains credit card transaction details, including:
- Loan amount
- Other financial details (columns not specified in this README)
- A `default` column, where:
  - `0` indicates a legitimate (non-default) transaction
  - `1` indicates a fraudulent (default) transaction

Place the credit_data.csv file in the correct location:
The dataset is loaded from a CSV file (`credit_data.csv`).

## Installation

### Prerequisites
Ensure you have the following libraries installed:
- Python 3.x
- Pandas
- NumPy
- Scikit-learn

You can install the required dependencies using pip:

```bash
pip install numpy pandas scikit-learn

### Usage

Here's a template for your README.md file. It provides an overview of your credit card fraud detection project using logistic regression.

markdown
Copy code
# Credit Card Fraud Detection

This project aims to detect fraudulent transactions from a credit card dataset using a Logistic Regression model. The dataset contains information about credit card loans, and the task is to classify transactions as legit (non-default) or fraudulent (default).

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model](#model)
- [Results](#results)
- [License](#license)

## Project Overview 
Credit card fraud is a significant issue in the financial sector. This project focuses on building a binary classification model to predict whether a credit card transaction is legitimate or fraudulent. The model is built using logistic regression, and we balance the dataset using undersampling techniques to handle the imbalance between legitimate and fraudulent transactions.

## Dataset
The dataset used in this project contains credit card transaction details, including:
- Loan amount
- Other financial details (columns not specified in this README)
- A `default` column, where:
  - `0` indicates a legitimate (non-default) transaction
  - `1` indicates a fraudulent (default) transaction

The dataset is loaded from a CSV file (`credit_data.csv`).

## Installation

### Prerequisites
Ensure you have the following libraries installed:
- Python 3.x
- Pandas
- NumPy
- Scikit-learn

You can install the required dependencies using pip:

```bash
pip install numpy pandas scikit-learn
Dataset
Place the credit_data.csv file in the correct location:

bash
Copy code
/mnt/c/Users/bhanu/OneDrive/Desktop/project/
Usage
To run the project, follow these steps:
Clone the repository:
git clone https://github.com/your-username/credit-fraud-detector.git
cd credit-fraud-detector
Run the script:
python fraud_detection.py
The script will output:

Basic statistics of the dataset
Distribution of legitimate and fraudulent transactions
Accuracy on training and test datasets

### Model
The model used for classification is Logistic Regression. The dataset is split into training and testing sets, and the model is trained on the training set. Undersampling is applied to balance the dataset by matching the number of legitimate transactions to the number of fraudulent ones.

#### Key Steps:
Load and preprocess the data
Analyze the distribution of transactions
Apply undersampling to balance the data
Split the data into training and test sets
Train a logistic regression model
Evaluate the model on the training and test sets

#### Results
The logistic regression model achieved the following accuracies:
Training Accuracy: X% (replace with actual value)
Test Accuracy: X% (replace with actual value)


