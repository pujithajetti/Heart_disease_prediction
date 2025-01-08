import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved models
try:
    heart_disease_model = pickle.load(open(r'C:\Users\Admin\OneDrive\Desktop\Heart Disease Prediction\heart_disease_model.sav', 'rb'))
except FileNotFoundError as e:
    st.error(f"Error loading models: {e}")

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        'Disease Prediction System',
        ['Overview', 'Heart Disease Prediction'],
        icons=['info-circle', 'heart-pulse'],  # Fix: Added missing comma
        default_index=0,
        styles={
            "nav-link-selected": {"background-color": "#FF6347"},
            "icon": {"color": "white", "font-size": "18px"},
        }
    )

# Overview Page
if selected == 'Overview':
    st.title('Heart Disease Prediction System')
    st.write("""
    This system provides predictions for heart disease:
    - **Heart Disease**: A range of conditions affecting the heart, including coronary artery disease and more.

    Use the sidebar to select a disease prediction module, input the required parameters, and get an instant prediction.
    """)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction')

    # Input fields
    col1, = st.columns(1)  # Fix: Unpack the column list correctly
    with col1:
        age = st.number_input('Age', min_value=0, format="%d")
        sex = st.selectbox('Sex (0: Female, 1: Male)', [0, 1])
        cp = st.number_input('Chest Pain Type (0-3)', min_value=0, max_value=3, format="%d")
        trestbps = st.number_input('Resting Blood Pressure', min_value=0.0)
        chol = st.number_input('Serum Cholesterol (mg/dl)', min_value=0.0)
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl (0: No, 1: Yes)', [0, 1])
        restecg = st.number_input('Resting ECG (0-2)', min_value=0, max_value=2, format="%d")
        thalach = st.number_input('Max Heart Rate Achieved', min_value=0.0)
        exang = st.selectbox('Exercise-Induced Angina (0: No, 1: Yes)', [0, 1])
        oldpeak = st.number_input('ST Depression', min_value=0.0)
        slope = st.number_input('Slope of ST Segment (0-2)', min_value=0, max_value=2, format="%d")
        ca = st.number_input('Major Vessels (0-3)', min_value=0, max_value=3, format="%d")
        thal = st.number_input('Thalassemia (0-3)', min_value=0, max_value=3, format="%d")

    # Prediction
    if st.button('Predict Heart Disease', help="Click to predict"):
        try:
            features = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
            prediction = heart_disease_model.predict(features)
            result = "The person has heart disease" if prediction[0] == 1 else "The person does not have heart disease"
            st.success(result)
        except Exception as e:
            st.error(f"Error in prediction: {e}")
