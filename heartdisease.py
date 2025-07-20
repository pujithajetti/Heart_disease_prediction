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
    
    .input-container {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border: 1px solid #e9ecef;
    }
    
    .feature-info {
        background: #e3f2fd;
        padding: 0.5rem;
        border-radius: 5px;
        margin-top: 0.5rem;
        font-size: 0.9rem;
        color: #1976d2;
    }
</style>
""", unsafe_allow_html=True)

# Load the saved model with better error handling
@st.cache_resource
def load_model():
    try:
        model = pickle.load(open('heart_disease_model.sav', 'rb'))
        return model, None
    except FileNotFoundError:
        return None, "Model file 'heart_disease_model.sav' not found. Please ensure the model file is in the same directory."
    except Exception as e:
        return None, f"Error loading model: {str(e)}"

# Load model
heart_disease_model, error_message = load_model()

# Sidebar navigation with enhanced styling
with st.sidebar:
    st.markdown("<div style='text-align: center; padding: 1rem;'>", unsafe_allow_html=True)
    st.markdown("# 🏥 Medical AI", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    selected = option_menu(
        'Navigation',
        ['🏠 Overview', '❤️ Heart Disease Prediction', '📊 About Model'],
        icons=['house-door', 'heart-pulse', 'graph-up'],
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "#FF6B6B", "font-size": "18px"}, 
            "nav-link": {
                "font-size": "16px", 
                "text-align": "left", 
                "margin": "0px", 
                "--hover-color": "#eee",
                "border-radius": "10px",
                "margin-bottom": "5px"
            },
            "nav-link-selected": {
                "background-color": "#FF6B6B",
                "color": "white",
                "font-weight": "bold"
            },
        }
    )

# Overview Page
if selected == '🏠 Overview':
    st.markdown('<h1 class="main-header">❤️ Heart Disease Prediction System</h1>', unsafe_allow_html=True)
    
    # Hero section
    st.markdown('''
    <div class="info-card">
        <h2>🎯 Early Detection Saves Lives</h2>
        <p style="font-size: 1.1rem;">
            Our AI-powered system helps predict heart disease risk using advanced machine learning algorithms. 
            Get instant predictions based on key health indicators and take proactive steps towards better heart health.
        </p>
    </div>
    ''', unsafe_allow_html=True)
    
    # Features section
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('''
        <div class="metric-card">
            <h3>🚀 Fast Prediction</h3>
            <p>Get results in seconds with our optimized ML model</p>
        </div>
        ''', unsafe_allow_html=True)
    
    with col2:
        st.markdown('''
        <div class="metric-card">
            <h3>🎯 High Accuracy</h3>
            <p>Trained on comprehensive medical datasets</p>
        </div>
        ''', unsafe_allow_html=True)
    
    with col3:
        st.markdown('''
        <div class="metric-card">
            <h3>🔒 Secure</h3>
            <p>Your health data is processed securely</p>
        </div>
        ''', unsafe_allow_html=True)
    
    # How it works section
    st.markdown('<h2 class="sub-header">🔍 How It Works</h2>', unsafe_allow_html=True)
    
    steps_col1, steps_col2 = st.columns(2)
    with steps_col1:
        st.markdown("""
        **Step 1: Input Health Parameters** 📝  
        Enter your medical information including age, blood pressure, cholesterol levels, and other key indicators.
        
        **Step 2: AI Analysis** 🧠  
        Our trained machine learning model analyzes your data using proven medical patterns.
        """)
    
    with steps_col2:
        st.markdown("""
        **Step 3: Get Prediction** 📊  
        Receive an instant prediction about heart disease risk along with confidence metrics.
        
        **Step 4: Take Action** 💪  
        Use the results to consult with healthcare professionals and make informed decisions.
        """)
    
    # Disclaimer
    st.markdown("""
    ---
    **⚠️ Important Disclaimer:** This tool is for educational and screening purposes only. 
    Always consult with qualified healthcare professionals for proper medical diagnosis and treatment.
    """)

# About Model Page
elif selected == '📊 About Model':
    st.markdown('<h1 class="main-header">📊 Model Information</h1>', unsafe_allow_html=True)
    
    # Model status
    if heart_disease_model is not None:
        st.markdown('''
        <div class="prediction-negative">
            ✅ Model Status: Loaded Successfully
        </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown(f'''
        <div class="prediction-positive">
            ❌ Model Status: {error_message}
        </div>
        ''', unsafe_allow_html=True)
    
    # Model details
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('''
        <div class="metric-card">
            <h3>🔬 Model Type</h3>
            <p>Machine Learning Classification Model</p>
        </div>
        ''', unsafe_allow_html=True)
        
        st.markdown('''
        <div class="metric-card">
            <h3>📊 Input Features</h3>
            <p>13 key medical indicators</p>
        </div>
        ''', unsafe_allow_html=True)
    
    with col2:
        st.markdown('''
        <div class="metric-card">
            <h3>🎯 Output</h3>
            <p>Binary classification (Positive/Negative)</p>
        </div>
        ''', unsafe_allow_html=True)
        
        st.markdown('''
        <div class="metric-card">
            <h3>⚡ Processing Time</h3>
            <p>< 1 second per prediction</p>
        </div>
        ''', unsafe_allow_html=True)
    
    # Feature descriptions
    st.markdown('<h2 class="sub-header">📋 Input Features Explained</h2>', unsafe_allow_html=True)
    
    feature_descriptions = {
        "Age": "Patient's age in years",
        "Sex": "0 = Female, 1 = Male",
        "Chest Pain Type": "0-3 scale indicating different types of chest pain",
        "Resting Blood Pressure": "Blood pressure at rest (mm Hg)",
        "Cholesterol": "Serum cholesterol level (mg/dl)",
        "Fasting Blood Sugar": "Whether fasting blood sugar > 120 mg/dl",
        "Resting ECG": "Resting electrocardiogram results (0-2)",
        "Max Heart Rate": "Maximum heart rate achieved during exercise",
        "Exercise Angina": "Exercise-induced chest pain (0 = No, 1 = Yes)",
        "ST Depression": "ST depression induced by exercise",
        "ST Slope": "Slope of the peak exercise ST segment",
        "Major Vessels": "Number of major vessels colored by fluoroscopy (0-3)",
        "Thalassemia": "Blood disorder indicator (0-3)"
    }
    
    for feature, description in feature_descriptions.items():
        st.markdown(f"**{feature}:** {description}")

# Heart Disease Prediction Page
elif selected == '❤️ Heart Disease Prediction':
    st.markdown('<h1 class="main-header">❤️ Heart Disease Prediction</h1>', unsafe_allow_html=True)
    
    # Check if model is loaded
    if heart_disease_model is None:
        st.error(f"⚠️ {error_message}")
        st.stop()
    
    st.markdown("Please fill in all the required medical parameters below to get your heart disease risk prediction.")
    
    # Create tabs for better organization
    tab1, tab2 = st.tabs(["📝 Input Parameters", "ℹ️ Parameter Guide"])
    
    with tab1:
        # Input fields organized in columns
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="input-container">', unsafe_allow_html=True)
            st.markdown("### 👤 Personal Information")
            age = st.number_input('Age (years)', min_value=1, max_value=120, value=50, help="Enter your age")
            sex = st.selectbox('Sex', 
                             options=[0, 1], 
                             format_func=lambda x: "Female" if x == 0 else "Male",
                             help="Select your biological sex")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="input-container">', unsafe_allow_html=True)
            st.markdown("### 🩺 Chest Pain & Symptoms")
            cp = st.selectbox('Chest Pain Type', 
                            options=[0, 1, 2, 3],
                            format_func=lambda x: ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"][x],
                            help="Type of chest pain experienced")
            exang = st.selectbox('Exercise-Induced Chest Pain', 
                               options=[0, 1],
                               format_func=lambda x: "No" if x == 0 else "Yes",
                               help="Does exercise cause chest pain?")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="input-container">', unsafe_allow_html=True)
            st.markdown("### 🩸 Blood Tests")
            chol = st.number_input('Serum Cholesterol (mg/dl)', 
                                 min_value=100, max_value=600, value=200,
                                 help="Total cholesterol level in blood")
            fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', 
                             options=[0, 1],
                             format_func=lambda x: "No" if x == 0 else "Yes",
                             help="Is fasting blood sugar greater than 120 mg/dl?")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="input-container">', unsafe_allow_html=True)
            st.markdown("### 💓 Heart Measurements")
            trestbps = st.number_input('Resting Blood Pressure (mm Hg)', 
                                     min_value=80, max_value=250, value=120,
                                     help="Blood pressure when at rest")
            thalach = st.number_input('Maximum Heart Rate Achieved', 
                                    min_value=60, max_value=250, value=150,
                                    help="Highest heart rate during exercise test")
            oldpeak = st.number_input('ST Depression', 
                                    min_value=0.0, max_value=10.0, value=0.0, step=0.1,
                                    help="ST depression induced by exercise")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="input-container">', unsafe_allow_html=True)
            st.markdown("### 📈 ECG & Advanced Tests")
            restecg = st.selectbox('Resting ECG Results', 
                                 options=[0, 1, 2],
                                 format_func=lambda x: ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"][x],
                                 help="Resting electrocardiogram results")
            slope = st.selectbox('ST Segment Slope', 
                               options=[0, 1, 2],
                               format_func=lambda x: ["Upsloping", "Flat", "Downsloping"][x],
                               help="Slope of peak exercise ST segment")
            ca = st.selectbox('Major Vessels (0-3)', 
                            options=[0, 1, 2, 3],
                            help="Number of major vessels colored by fluoroscopy")
            thal = st.selectbox('Thalassemia', 
                              options=[0, 1, 2, 3],
                              format_func=lambda x: ["Normal", "Fixed Defect", "Reversible Defect", "Not Described"][x],
                              help="Blood disorder test result")
            st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### 📖 Parameter Explanations")
        
        explanations = {
            "**Age**": "Your current age in years. Heart disease risk generally increases with age.",
            "**Sex**": "Biological sex. Males typically have higher risk at younger ages.",
            "**Chest Pain Type**": "Different types indicate varying risk levels:\n- Typical Angina: Classic heart-related chest pain\n- Atypical Angina: Similar but not classic pattern\n- Non-Anginal: Chest pain not related to heart\n- Asymptomatic: No chest pain symptoms",
            "**Resting Blood Pressure**": "Blood pressure when relaxed. Normal range is typically 90-120 mm Hg.",
            "**Cholesterol**": "Total cholesterol in blood. Higher levels (>240 mg/dl) increase heart disease risk.",
            "**Fasting Blood Sugar**": "Blood sugar after fasting. >120 mg/dl may indicate diabetes risk.",
            "**Resting ECG**": "Heart electrical activity at rest. Abnormalities may indicate heart problems.",
            "**Max Heart Rate**": "Peak heart rate during exercise test. Lower values may indicate heart problems.",
            "**Exercise Chest Pain**": "Pain triggered by physical activity often indicates heart issues.",
            "**ST Depression**": "Measure of heart stress during exercise. Higher values indicate more stress.",
            "**ST Slope**": "Pattern of heart response to exercise:\n- Upsloping: Generally better\n- Flat/Downsloping: May indicate problems",
            "**Major Vessels**": "Coronary arteries with significant blockage (0 = better, 3 = worse).",
            "**Thalassemia**": "Blood disorder that can affect heart health."
        }
        
        for param, explanation in explanations.items():
            with st.expander(param):
                st.write(explanation)
    
    # Prediction button and results
    st.markdown("---")
    
    # Center the prediction button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        predict_button = st.button('🔍 Predict Heart Disease Risk', 
                                 help="Click to get your heart disease risk prediction")
    
    if predict_button:
        try:
            # Prepare features
            features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, 
                               thalach, exang, oldpeak, slope, ca, thal]])
            
            # Make prediction
            with st.spinner('Analyzing your health data...'):
                prediction = heart_disease_model.predict(features)
                prediction_proba = None
                
                # Try to get probability if available
                try:
                    prediction_proba = heart_disease_model.predict_proba(features)
                except:
                    pass
            
            # Display results
            st.markdown("---")
            st.markdown('<h2 class="sub-header">📊 Prediction Results</h2>', unsafe_allow_html=True)
            
            if prediction[0] == 1:
                st.markdown('''
                <div class="prediction-positive">
                    ⚠️ HIGH RISK: The model indicates a higher probability of heart disease
                </div>
                ''', unsafe_allow_html=True)
                
                st.markdown("""
                ### 🚨 Recommended Actions:
                - **Consult a cardiologist immediately** for proper diagnosis
                - Schedule comprehensive heart tests (ECG, Echo, Stress Test)
                - Monitor blood pressure and cholesterol regularly
                - Adopt heart-healthy lifestyle changes
                - Consider medication as prescribed by your doctor
                """)
                
            else:
                st.markdown('''
                <div class="prediction-negative">
                    ✅ LOW RISK: The model indicates a lower probability of heart disease
                </div>
                ''', unsafe_allow_html=True)
                
                st.markdown("""
                ### 💚 Recommendations:
                - **Continue maintaining healthy habits**
                - Regular check-ups with your healthcare provider
                - Maintain healthy diet and exercise routine
                - Monitor key health indicators periodically
                - Stay aware of heart disease risk factors
                """)
            
            # Show probability if available
            if prediction_proba is not None:
                prob_no_disease = prediction_proba[0][0] * 100
                prob_disease = prediction_proba[0][1] * 100
                
                st.markdown("### 📈 Confidence Levels:")
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("No Heart Disease", f"{prob_no_disease:.1f}%")
                with col2:
                    st.metric("Heart Disease", f"{prob_disease:.1f}%")
            
            # Additional information
            st.markdown("""
            ---
            **⚠️ Important Medical Disclaimer:**
            
            This prediction is based on a machine learning model and should not replace professional medical advice. 
            The results are for screening purposes only. Always consult qualified healthcare professionals for 
            proper medical diagnosis, treatment recommendations, and health management decisions.
            
            **For Emergency:** If you're experiencing chest pain, shortness of breath, or other concerning symptoms, 
            seek immediate medical attention or call emergency services.
            """)
            
        except Exception as e:
            st.error(f"❌ Error in prediction: {str(e)}")
            st.info("Please check your input values and try again. If the problem persists, contact support.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p>💡 Built with Streamlit | ❤️ For Educational Purposes | 🔬 AI-Powered Health Screening</p>
    <p><small>Version 2.0 | Always consult healthcare professionals for medical decisions</small></p>
</div>
""", unsafe_allow_html=True)
