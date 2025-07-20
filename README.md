# Heart Disease Prediction

This project is a simple yet practical machine learning-based tool that predicts the likelihood of heart disease in a person based on various medical features. The goal is to assist in early diagnosis and risk assessment using a quick and non-invasive method. It’s built using Python, trained with real-world data, and deployed using Streamlit for easy access.

🔗 **Live Demo:**  
[Click here to try the app](https://heartdiseaseprediction-cga7ejarf8ykjlyuw7vhcu.streamlit.app/#913007c6)

---

## About the Project

The Heart Disease Prediction system uses supervised learning algorithms to analyze patient data and predict the possibility of heart disease. The model is trained on key clinical attributes such as age, gender, blood pressure, cholesterol level, ECG results, heart rate, and more. After comparing Logistic Regression and Support Vector Machine (SVM), we chose the SVM model for deployment based on slightly better accuracy during training.

The app allows users (patients, doctors, or researchers) to input medical information and get an instant risk prediction, helping support quicker medical decisions.

---

## Features

- Cleaned and preprocessed dataset for better model performance
- Built and compared Logistic Regression and SVM models
- Used accuracy metrics for model evaluation
- Pickle used to save the final trained model
- Interactive web app created using Streamlit
- Simple and clean UI for user input and prediction display

---

## Tech Stack

- **Language:** Python
- **Libraries & Tools:**
  - `pandas`, `numpy` – data handling and analysis
  - `matplotlib`, `seaborn` – data visualization
  - `scikit-learn` – machine learning models
  - `pickle` – model saving
  - `streamlit` – web app deployment

---

## Model Accuracy

### Logistic Regression
- **Training Accuracy:** 85.12%
- **Testing Accuracy:** 81.97%

### Support Vector Machine (SVM)
- **Training Accuracy:** 85.54%
- **Testing Accuracy:** 81.97%

 **Final Model Chosen:** Support Vector Machine (SVM)  
Although both models performed similarly on the test data, SVM had a slightly better training score and was more consistent during multiple evaluations.

**conclusion**
This project shows how machine learning can be applied in the healthcare domain to support early detection of heart disease. By leveraging clinical data and combining it with reliable ML models, it provides a fast, accessible, and practical tool for health risk prediction. With a simple UI and real-time prediction capability, it has potential for real-world use and continuous improvement through advanced features and tuning

