# Census Income Prediction

## Problem

### Description

Income prediction is a classification problem that aims to determine whether an individual's annual income exceeds $50,000 based on demographic and employment-related information.

Predicting income levels helps identify relationships between personal characteristics, education, occupation, and income distribution.

The objective is to predict whether an individual earns more than $50K annually based on demographic, educational, and employment features.

### Solution

Develop a Machine Learning classification model to predict individual income levels using the Census Income (Adult) dataset.

The solution involves:

- Data understanding and exploratory data analysis.
- Handling missing values and inconsistent categorical values.
- Detecting and analyzing outliers.
- Encoding categorical features and scaling numerical features.
- Analyzing feature relationships and selecting relevant features.
- Training and evaluating classification models.
- Evaluating performance using Precision, Recall, F1-Score, and ROC-AUC.

The goal is to build a classification model capable of predicting income levels and identifying the factors associated with higher income.

## Insights

### Features

The dataset contains 14 input features describing individuals' demographic, educational, and employment information:

- **Demographic Features:** `age`, `sex`, `race`, `native_country`.
- **Educational Features:** `education`, `education_num`.
- **Employment Features:** `workclass`, `occupation`, `hours_per_week`.
- **Family and Relationship Features:** `marital_status`, `relationship`.
- **Financial Features:** `capital_gain`, `capital_loss`.
- **Additional Feature:** `fnlwgt` (final sampling weight).

### Target

`income` — Binary classification:

- `<=50K` — Income is less than or equal to $50,000.
- `>50K` — Income is greater than $50,000.
