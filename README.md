# Heart_disease_prediction
This project is a machine learning-based system designed to predict the likelihood of heart disease in patients. Utilizing a dataset containing various health parameters, the system aims to assist healthcare professionals by providing an early warning tool for heart disease risk.
Heart Disease Prediction Model
Project Overview
This project implements a machine learning solution to predict heart disease using various clinical parameters. The model uses Support Vector Machine (SVM) and Logistic Regression algorithms to make predictions, with SVM being chosen as the final model based on its superior performance.
Features

Data preprocessing and visualization
Implementation of multiple machine learning models
Model comparison and evaluation
Interactive web deployment using Streamlit
Model persistence using Pickle

Technical Stack

Python
Scikit-learn
Streamlit
Pickle
Other data processing libraries

Model Performance
Logistic Regression

Training Accuracy: 85.12%
Testing Accuracy: 81.97%

Support Vector Machine (SVM)

Training Accuracy: 85.54%
Testing Accuracy: 81.97%

Based on the slightly better training accuracy, SVM was selected as the final model for deployment.And then it is deployed by using streamlit.

Future Improvements

Implementation of additional machine learning algorithms
Feature engineering to improve model accuracy
Enhanced visualization in the web interface
Cross-validation implementation
Hyperparameter tuning
