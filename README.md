# 📈 Sales & Demand Forecasting

A Machine Learning project for predicting expected sales using historical sales patterns and time-based features.

## 🚀 Live Demo

Deployed using Streamlit Community Cloud.

## 📌 Project Overview

The goal of this project is to build a machine learning model that can predict sales based on store, item, historical sales and time-related features.

The project covers the complete machine learning workflow:

- Data loading and exploration
- Data cleaning
- Exploratory Data Analysis
- Feature engineering
- Lag features
- Rolling average features
- Time-based features
- Chronological train-test split
- Model training
- Model evaluation
- Feature importance analysis
- Model saving
- Prediction pipeline
- Streamlit deployment

## 🧠 Machine Learning Model

The final model is a lightweight Random Forest Regressor designed to work efficiently on limited hardware.

### Model Configuration

- Algorithm: Random Forest Regressor
- Number of Trees: 30
- Maximum Depth: 20
- Random State: 42
- Parallel Jobs: 2

## 📊 Model Performance

| Metric | Score |
|---|---:|
| MAE | 5.75 |
| RMSE | 7.48 |
| R² | 0.913 |

## 🔧 Features

The model uses the following features:

- Store
- Item
- Lag 1 Sales
- Lag 7 Sales
- 7-Day Rolling Mean
- Year
- Month
- Day
- Day of Week
- Weekend Indicator

## 🖥️ Streamlit Application

The Streamlit application allows users to enter sales-related information and receive a predicted sales value.

### Example

Input:

- Store: 1
- Item: 1
- Lag 1: 50
- Lag 7: 55
- 7-Day Average: 52

Output:

```text
Predicted Sales: 42.99 units