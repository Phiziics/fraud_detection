# Fraud Detection API

## Introduction

This project builds an end to end fraud detection system using highly imbalanced credit card transaction data. The goal is to detect fraudulent transactions while minimizing false alarms. The system includes exploratory data analysis, feature engineering, model training, evaluation, metadata tracking, and a FastAPI deployment layer for real time scoring.

## Problem

Fraud detection is a difficult classification problem because fraudulent transactions are rare. In this dataset, fraud represents only a very small fraction of all transactions. This means overall accuracy is not a reliable measure of model quality. The model must instead focus on identifying fraud effectively while controlling false positives.

## Dataset

The project uses the `creditcard.csv` dataset.

Features include:
- `V1` to `V28`: PCA transformed anonymized numerical features
- `Amount`: original transaction amount
- `Time`: elapsed seconds since the first transaction
- `Class`: target label where `1` is fraud and `0` is non fraud

## Feature Engineering

The final feature set includes:
- `V1` to `V28`
- `Amount_log`
- `Time_sin`
- `Time_cos`

Feature decisions:
- `Amount` was log transformed into `Amount_log` to reduce skew
- `Time` was converted into cyclical features using sine and cosine encoding
- Raw `Amount`, raw `Time`, and `Time_hour` were removed from the final training set

## Modeling Approach

The following models were trained and compared:
- Logistic Regression
- Random Forest
- XGBoost
- LightGBM

XGBoost was selected as the final model because it provided the best balance between precision and recall and achieved the strongest PR AUC.

## Final Model Performance

Final selected model: `XGBoost`

Key metrics:
- Accuracy: 0.9995
- Balanced Accuracy: 0.8894
- Precision: 0.9024
- Recall: 0.7789
- F1 Score: 0.8362
- ROC AUC: 0.9727
- PR AUC: 0.8225

Threshold tuning was performed to optimize the tradeoff between recall and precision. A threshold of `0.30` was selected for deployment.

## Project Structure

```text
fraud_detection/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── schemas.py
│   ├── fraud_model.py
│   └── fraud_service.py
├── artifacts/
│   ├── fraud_model_v1.0.joblib
│   └── fraud_model_v1.0_metadata.json
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_train.ipynb
│   └── 03_evaluation.ipynb
└── tests/
    └── test_fraud_api.py