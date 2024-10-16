# credit-fraud-risk-predictor

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
