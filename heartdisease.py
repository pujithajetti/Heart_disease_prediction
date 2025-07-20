import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Heart Disease Prediction System",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #FF6B6B;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    
    .sub-header {
        font-size: 1.5rem;
        color: #4ECDC4;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    
    .info-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #FF6B6B;
        margin: 0.5rem 0;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
    }
    
    .prediction-positive {
        background: linear-gradient(135deg, #ff6b6b, #ee5a52);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
        margin: 1rem 0;
        box-shadow: 0 4px 16px rgba(255, 107, 107, 0.3);
    }
    
    .prediction-negative {
        background: linear-gradient(135deg, #4ecdc4, #44a08d);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
        margin: 1rem 0;
        box-shadow: 0 4px 16px rgba(78, 205, 196, 0.3);
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-weight: bold;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Load the saved model
@st.cache_resource
def load_model():
    try:
        model = pickle.load(open('heart_disease_model.sav', 'rb'))
        return model, None
    except FileNotFoundError:
        return None, "Model file 'heart_disease_model.sav' not found."
    except Exception as e:
        return None, f"Error loading model: {str(e)}"

# Load model
heart_disease_model, error_message = load_model()

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        'Disease Prediction System',
        ['Overview', 'Heart Disease Prediction'],
        icons=['info-circle', 'heart-pulse'],
        default_index=0,
        styles={
            "nav-link-selected": {"background-color": "#FF6347"},
            "icon": {"color": "white", "font-size": "18px"},
        }
    )

# Overview Page
if selected == 'Overview':
    st.markdown('<h1 class="main-header">❤️ Heart Disease Prediction System</h1>', unsafe_allow_html=True)
    
    st.markdown('''
    <div class="info-card">
        <h2>🎯 AI-Powered Heart Health Assessment</h2>
        <p style="font-size: 1.1rem;">
            This system provides predictions for heart disease using advanced machine learning algorithms. 
            Heart disease refers to a range of conditions affecting the heart, including coronary artery disease and more.
        </p>
    </div>
    ''', unsafe_allow_html=True)
    
    # Features section
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('''
        <div class="metric-card">
            <h3>🚀 Fast Prediction</h3>
            <p>Get results in seconds</p>
        </div>
        ''', unsafe_allow_html=True)
    
    with col2:
        st.markdown('''
        <div class="metric-card">
            <h3>🎯 High Accuracy</h3>
            <p>Trained on medical datasets</p>
        </div>
        ''', unsafe_allow_html=True)
    
    with col3:
        st.markdown('''
        <div class="metric-card">
            <h3>🔒 Secure</h3>
            <p>Your data is processed securely</p>
        </div>
        ''', unsafe_allow_html=True)
    
    st.write("""
    **How to use:**
    - Use the sidebar to select the Heart Disease Prediction module
    - Input the required medical parameters
    - Get an instant prediction with recommendations
    """)
    
    st.markdown("""
    ---
    **⚠️ Disclaimer:** This tool is for educational and screening purposes only. 
    Always consult with qualified healthcare professionals for proper medical diagnosis and treatment.
    """)

# Heart Disease Prediction Page
elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction')
    
    # Check if model is loaded
    if heart_disease_model is None:
        st.error(f"⚠️ {error_message}")
        st.stop()
    
    # Input fields in a clean layout
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input('Age', min_value=0, format="%d")
        sex = st.selectbox('Sex (0: Female, 1: Male)', [0, 1])
        cp = st.number_input('Chest Pain Type (0-3)', min_value=0, max_value=3, format="%d")
        trestbps = st.number_input('Resting Blood Pressure', min_value=0.0)
        chol = st.number_input('Serum Cholesterol (mg/dl)', min_value=0.0)
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl (0: No, 1: Yes)', [0, 1])
        restecg = st.number_input('Resting ECG (0-2)', min_value=0, max_value=2, format="%d")
    
    with col2:
        thalach = st.number_input('Max Heart Rate Achieved', min_value=0.0)
        exang = st.selectbox('Exercise-Induced Angina (0: No, 1: Yes)', [0, 1])
        oldpeak = st.number_input('ST Depression', min_value=0.0)
        slope = st.number_input('Slope of ST Segment (0-2)', min_value=0, max_value=2, format="%d")
        ca = st.number_input('Major Vessels (0-3)', min_value=0, max_value=3, format="%d")
        thal = st.number_input('Thalassemia (0-3)', min_value=0, max_value=3, format="%d")
    
    # Prediction button
    if st.button('Predict Heart Disease', help="Click to predict"):
        try:
            # Prepare features
            features = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
            
            # Make prediction
            with st.spinner('Analyzing...'):
                prediction = heart_disease_model.predict(features)
            
            # Display results with enhanced styling
            if prediction[0] == 1:
                st.markdown('''
                <div class="prediction-positive">
                    ⚠️ The person has heart disease
                </div>
                ''', unsafe_allow_html=True)
                
                st.markdown("""
                **Recommendations:**
                - Consult a cardiologist immediately
                - Schedule comprehensive heart tests
                - Monitor vital signs regularly
                - Adopt heart-healthy lifestyle changes
                """)
                
            else:
                st.markdown('''
                <div class="prediction-negative">
                    ✅ The person does not have heart disease
                </div>
                ''', unsafe_allow_html=True)
                
                st.markdown("""
                **Recommendations:**
                - Continue maintaining healthy habits
                - Regular check-ups with healthcare provider
                - Maintain healthy diet and exercise routine
                """)
            
        except Exception as e:
            st.error(f"Error in prediction: {e}")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem;'>
    <p>💡 Built with Streamlit | ❤️ For Educational Purposes | 🔬 AI-Powered Health Screening</p>
</div>
""", unsafe_allow_html=True)
