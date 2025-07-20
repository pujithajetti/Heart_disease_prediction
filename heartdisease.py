import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import base64

# Page configuration
st.set_page_config(
    page_title="Heart Disease Prediction System",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    /* Global Styles */
    .main {
        font-family: 'Inter', sans-serif;
    }
    
    /* Header Styling */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .main-header h1 {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-header p {
        font-size: 1.2rem;
        opacity: 0.9;
        margin-bottom: 0;
    }
    
    /* Card Styling */
    .prediction-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        border: 1px solid #e0e6ed;
        margin-bottom: 2rem;
    }
    
    .input-section {
        background: #f8fafc;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        margin-bottom: 1.5rem;
    }
    
    .section-title {
        color: #2d3748;
        font-weight: 600;
        font-size: 1.3rem;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #667eea;
    }
    
    /* Result Styling */
    .result-positive {
        background: linear-gradient(135deg, #ff6b6b, #ee5a52);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        font-weight: 600;
        font-size: 1.2rem;
        margin: 1rem 0;
        box-shadow: 0 5px 15px rgba(255, 107, 107, 0.3);
    }
    
    .result-negative {
        background: linear-gradient(135deg, #51cf66, #40c057);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        font-weight: 600;
        font-size: 1.2rem;
        margin: 1rem 0;
        box-shadow: 0 5px 15px rgba(81, 207, 102, 0.3);
    }
    
    /* Button Styling */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 10px;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Input Fields */
    .stNumberInput > div > div > input {
        border-radius: 8px;
        border: 2px solid #e2e8f0;
        padding: 0.5rem;
    }
    
    .stSelectbox > div > div > select {
        border-radius: 8px;
        border: 2px solid #e2e8f0;
        padding: 0.5rem;
    }
    
    /* Info Cards */
    .info-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #667eea;
        box-shadow: 0 3px 10px rgba(0,0,0,0.05);
        margin: 1rem 0;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 5px 15px rgba(240, 147, 251, 0.3);
    }
    
    /* Animation */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .fade-in {
        animation: fadeIn 0.8s ease-out;
    }
</style>
""", unsafe_allow_html=True)

# Load the saved models
@st.cache_resource
def load_model():
    try:
        model = pickle.load(open('heart_disease_model.sav', 'rb'))
        return model
    except FileNotFoundError as e:
        st.error(f"⚠️ Error loading model: {e}")
        st.info("Please ensure 'heart_disease_model.sav' is in the same directory as this script.")
        return None

heart_disease_model = load_model()

# Sidebar navigation with enhanced styling
with st.sidebar:
    st.markdown("### 🏥 Navigation")
    selected = option_menu(
        '',
        ['🏠 Overview', '❤️ Heart Disease Prediction', '📊 Health Tips', '📈 Risk Factors'],
        icons=['house', 'heart-pulse-fill', 'lightbulb', 'graph-up'],
        default_index=0,
        styles={
            "container": {"padding": "1rem", "background-color": "transparent"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0.5rem 0",
                "padding": "1rem",
                "border-radius": "10px",
                "background-color": "rgba(255,255,255,0.1)",
                "color": "white",
                "font-weight": "500",
            },
            "nav-link-selected": {
                "background": "linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%)",
                "color": "#2d3748",
                "font-weight": "600",
                "box-shadow": "0 4px 12px rgba(0,0,0,0.1)"
            },
            "icon": {"color": "white", "font-size": "20px", "margin-right": "10px"},
        }
    )

# Overview Page
if selected == '🏠 Overview':
    # Main header
    st.markdown("""
    <div class="main-header fade-in">
        <h1>❤️ Heart Disease Prediction System</h1>
        <p>Advanced AI-powered cardiovascular health assessment</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="info-card fade-in">
            <h3>🎯 Accurate Predictions</h3>
            <p>Machine learning model trained on clinical data to provide reliable heart disease risk assessment.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card fade-in">
            <h3>⚡ Instant Results</h3>
            <p>Get immediate risk assessment based on your health parameters and medical indicators.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="info-card fade-in">
            <h3>🛡️ Preventive Care</h3>
            <p>Early detection helps in taking preventive measures and lifestyle modifications.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # System information
    st.markdown("### 📋 System Information")
    
    info_col1, info_col2 = st.columns(2)
    
    with info_col1:
        st.markdown("""
        <div class="prediction-card">
            <h4>🏥 About Heart Disease</h4>
            <p>Heart disease refers to several types of heart conditions, including:</p>
            <ul>
                <li><strong>Coronary Artery Disease:</strong> Most common type, affects blood flow to the heart</li>
                <li><strong>Heart Attack:</strong> When blood flow to part of the heart is blocked</li>
                <li><strong>Heart Failure:</strong> When the heart can't pump blood as well as it should</li>
                <li><strong>Arrhythmia:</strong> Irregular heartbeat</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with info_col2:
        st.markdown("""
        <div class="prediction-card">
            <h4>🔍 How It Works</h4>
            <ol>
                <li><strong>Input Parameters:</strong> Enter your health metrics and medical history</li>
                <li><strong>AI Analysis:</strong> Our machine learning model analyzes your data</li>
                <li><strong>Risk Assessment:</strong> Get your personalized heart disease risk prediction</li>
                <li><strong>Recommendations:</strong> Receive guidance based on your results</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)

# Health Tips Page
elif selected == '📊 Health Tips':
    st.markdown("""
    <div class="main-header fade-in">
        <h1>💡 Heart Health Tips</h1>
        <p>Evidence-based recommendations for cardiovascular wellness</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="prediction-card">
            <h3>🍎 Dietary Recommendations</h3>
            <ul>
                <li>Eat plenty of fruits and vegetables</li>
                <li>Choose whole grains over refined grains</li>
                <li>Include lean proteins (fish, poultry, legumes)</li>
                <li>Limit saturated and trans fats</li>
                <li>Reduce sodium intake</li>
                <li>Stay hydrated with plenty of water</li>
            </ul>
        </div>
        
        <div class="prediction-card">
            <h3>🏃‍♂️ Physical Activity</h3>
            <ul>
                <li>Aim for 150 minutes of moderate exercise weekly</li>
                <li>Include strength training 2-3 times per week</li>
                <li>Take regular walks throughout the day</li>
                <li>Use stairs instead of elevators when possible</li>
                <li>Find activities you enjoy to stay consistent</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="prediction-card">
            <h3>😌 Stress Management</h3>
            <ul>
                <li>Practice meditation or deep breathing</li>
                <li>Get adequate sleep (7-9 hours nightly)</li>
                <li>Maintain social connections</li>
                <li>Engage in hobbies and relaxing activities</li>
                <li>Consider professional help if needed</li>
            </ul>
        </div>
        
        <div class="prediction-card">
            <h3>🚭 Lifestyle Factors</h3>
            <ul>
                <li>Avoid smoking and secondhand smoke</li>
                <li>Limit alcohol consumption</li>
                <li>Maintain a healthy weight</li>
                <li>Monitor blood pressure regularly</li>
                <li>Get regular health checkups</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Risk Factors Page
elif selected == '📈 Risk Factors':
    st.markdown("""
    <div class="main-header fade-in">
        <h1>⚠️ Heart Disease Risk Factors</h1>
        <p>Understanding what increases your risk</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="prediction-card">
            <h3>🔴 Non-Modifiable Risk Factors</h3>
            <p><strong>These factors cannot be changed:</strong></p>
            <ul>
                <li><strong>Age:</strong> Risk increases with age (men 45+, women 55+)</li>
                <li><strong>Gender:</strong> Men have higher risk at younger ages</li>
                <li><strong>Family History:</strong> Genetic predisposition matters</li>
                <li><strong>Ethnicity:</strong> Some groups have higher risk</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="prediction-card">
            <h3>🟡 Modifiable Risk Factors</h3>
            <p><strong>These factors can be controlled:</strong></p>
            <ul>
                <li><strong>High Blood Pressure:</strong> >140/90 mmHg</li>
                <li><strong>High Cholesterol:</strong> LDL >100 mg/dL</li>
                <li><strong>Smoking:</strong> Damages blood vessels</li>
                <li><strong>Diabetes:</strong> High blood sugar levels</li>
                <li><strong>Obesity:</strong> BMI >30</li>
                <li><strong>Physical Inactivity:</strong> Sedentary lifestyle</li>
                <li><strong>Poor Diet:</strong> High in saturated fats</li>
                <li><strong>Excessive Alcohol:</strong> >2 drinks/day for men</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Risk visualization
    st.markdown("### 📊 Risk Factor Impact")
    
    # Create a sample risk factor chart
    risk_data = {
        'Risk Factor': ['Smoking', 'High BP', 'High Cholesterol', 'Diabetes', 'Obesity', 'Inactivity'],
        'Relative Risk': [2.5, 2.1, 1.8, 2.0, 1.5, 1.4],
        'Population %': [20, 45, 35, 11, 36, 25]
    }
    
    risk_df = pd.DataFrame(risk_data)
    
    fig = px.bar(risk_df, x='Risk Factor', y='Relative Risk', 
                 title='Relative Risk of Heart Disease by Factor',
                 color='Relative Risk', color_continuous_scale='Reds')
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Inter", size=12),
        title_font=dict(size=18, color='#2d3748')
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Heart Disease Prediction Page
elif selected == '❤️ Heart Disease Prediction':
    if heart_disease_model is None:
        st.error("❌ Model not loaded. Please check the model file.")
        st.stop()
    
    st.markdown("""
    <div class="main-header fade-in">
        <h1>🔍 Heart Disease Risk Assessment</h1>
        <p>Enter your health parameters for personalized prediction</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create input form
    with st.form("prediction_form"):
        # Patient Information Section
        st.markdown('<div class="section-title">👤 Patient Information</div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            age = st.number_input('🎂 Age (years)', min_value=1, max_value=120, value=50, 
                                help="Patient's age in years")
            
        with col2:
            sex = st.selectbox('⚧️ Sex', 
                             options=[0, 1], 
                             format_func=lambda x: "Female" if x == 0 else "Male",
                             help="Biological sex of the patient")
            
        with col3:
            cp = st.selectbox('💢 Chest Pain Type', 
                            options=[0, 1, 2, 3],
                            format_func=lambda x: {
                                0: "Typical Angina", 
                                1: "Atypical Angina", 
                                2: "Non-Anginal Pain", 
                                3: "Asymptomatic"
                            }[x],
                            help="Type of chest pain experienced")
        
        # Vital Signs Section
        st.markdown('<div class="section-title">🩺 Vital Signs & Lab Values</div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            trestbps = st.number_input('🩸 Resting Blood Pressure (mmHg)', 
                                     min_value=80.0, max_value=250.0, value=120.0,
                                     help="Blood pressure when at rest")
            
            chol = st.number_input('🧪 Serum Cholesterol (mg/dl)', 
                                 min_value=100.0, max_value=600.0, value=240.0,
                                 help="Cholesterol level in blood")
        
        with col2:
            fbs = st.selectbox('🍬 Fasting Blood Sugar > 120 mg/dl', 
                             options=[0, 1],
                             format_func=lambda x: "No" if x == 0 else "Yes",
                             help="Whether fasting blood sugar exceeds 120 mg/dl")
            
            thalach = st.number_input('❤️ Maximum Heart Rate', 
                                    min_value=60.0, max_value=220.0, value=150.0,
                                    help="Maximum heart rate achieved during stress test")
        
        with col3:
            restecg = st.selectbox('📈 Resting ECG Results', 
                                 options=[0, 1, 2],
                                 format_func=lambda x: {
                                     0: "Normal", 
                                     1: "ST-T Wave Abnormality", 
                                     2: "Left Ventricular Hypertrophy"
                                 }[x],
                                 help="Resting electrocardiogram results")
            
            exang = st.selectbox('🏃‍♂️ Exercise-Induced Angina', 
                               options=[0, 1],
                               format_func=lambda x: "No" if x == 0 else "Yes",
                               help="Chest pain induced by exercise")
        
        # Advanced Parameters Section
        st.markdown('<div class="section-title">🔬 Advanced Parameters</div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            oldpeak = st.number_input('📉 ST Depression', 
                                    min_value=0.0, max_value=10.0, value=1.0, step=0.1,
                                    help="ST depression induced by exercise relative to rest")
        
        with col2:
            slope = st.selectbox('📊 Slope of Peak Exercise ST Segment', 
                               options=[0, 1, 2],
                               format_func=lambda x: {
                                   0: "Upsloping", 
                                   1: "Flat", 
                                   2: "Downsloping"
                               }[x],
                               help="Slope of the peak exercise ST segment")
        
        with col3:
            ca = st.selectbox('🩻 Major Vessels Colored by Fluoroscopy', 
                            options=[0, 1, 2, 3],
                            format_func=lambda x: f"{x} vessels",
                            help="Number of major vessels colored by fluoroscopy (0-3)")
        
        # Final parameter
        col1, col2, col3 = st.columns(3)
        with col2:
            thal = st.selectbox('🧬 Thalassemia', 
                              options=[0, 1, 2, 3],
                              format_func=lambda x: {
                                  0: "Normal", 
                                  1: "Fixed Defect", 
                                  2: "Reversible Defect",
                                  3: "Not Available"
                              }[x],
                              help="Blood disorder affecting hemoglobin")
        
        # Prediction button
        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button('🔮 Predict Heart Disease Risk', 
                                        help="Click to get your heart disease risk assessment")
        
        if submitted:
            try:
                # Prepare features for prediction
                features = [[age, sex, cp, trestbps, chol, fbs, restecg, 
                           thalach, exang, oldpeak, slope, ca, thal]]
                
                # Make prediction
                prediction = heart_disease_model.predict(features)
                probability = heart_disease_model.predict_proba(features)[0]
                
                # Display results
                st.markdown("### 📋 Prediction Results")
                
                if prediction[0] == 1:
                    risk_percentage = probability[1] * 100
                    st.markdown(f"""
                    <div class="result-positive">
                        <h3>⚠️ HIGH RISK DETECTED</h3>
                        <p>The model indicates a <strong>{risk_percentage:.1f}% probability</strong> of heart disease presence.</p>
                        <p><strong>Recommendation:</strong> Please consult a cardiologist immediately for further evaluation.</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Additional recommendations for high risk
                    st.markdown("""
                    <div class="prediction-card">
                        <h4>🚨 Immediate Actions Recommended:</h4>
                        <ul>
                            <li>Schedule an appointment with a cardiologist</li>
                            <li>Consider stress testing or cardiac catheterization</li>
                            <li>Review and optimize current medications</li>
                            <li>Implement lifestyle changes immediately</li>
                            <li>Monitor symptoms closely</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
                    
                else:
                    risk_percentage = probability[0] * 100
                    st.markdown(f"""
                    <div class="result-negative">
                        <h3>✅ LOW RISK DETECTED</h3>
                        <p>The model indicates a <strong>{risk_percentage:.1f}% probability</strong> of no heart disease.</p>
                        <p><strong>Recommendation:</strong> Continue maintaining a healthy lifestyle and regular checkups.</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Preventive recommendations for low risk
                    st.markdown("""
                    <div class="prediction-card">
                        <h4>💚 Preventive Care Recommendations:</h4>
                        <ul>
                            <li>Maintain regular exercise routine</li>
                            <li>Follow a heart-healthy diet</li>
                            <li>Monitor blood pressure and cholesterol annually</li>
                            <li>Avoid smoking and limit alcohol</li>
                            <li>Manage stress effectively</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Risk factors analysis
                st.markdown("### 📊 Risk Factors Analysis")
                
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    age_risk = "High" if age > 55 else "Low"
                    st.markdown(f"""
                    <div class="metric-card">
                        <h4>Age Risk</h4>
                        <h2>{age_risk}</h2>
                        <p>Age: {age} years</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    bp_risk = "High" if trestbps > 140 else "Normal"
                    st.markdown(f"""
                    <div class="metric-card">
                        <h4>Blood Pressure</h4>
                        <h2>{bp_risk}</h2>
                        <p>{trestbps} mmHg</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col3:
                    chol_risk = "High" if chol > 240 else "Normal"
                    st.markdown(f"""
                    <div class="metric-card">
                        <h4>Cholesterol</h4>
                        <h2>{chol_risk}</h2>
                        <p>{chol} mg/dl</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col4:
                    hr_risk = "Concerning" if thalach < 100 else "Good"
                    st.markdown(f"""
                    <div class="metric-card">
                        <h4>Max Heart Rate</h4>
                        <h2>{hr_risk}</h2>
                        <p>{thalach} bpm</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Disclaimer
                st.markdown("""
                <div class="info-card">
                    <h4>⚠️ Important Disclaimer</h4>
                    <p>This prediction tool is for educational purposes only and should not replace professional medical advice. 
                    Always consult with qualified healthcare professionals for proper diagnosis and treatment. 
                    The model's accuracy may vary based on individual factors not captured in this assessment.</p>
                </div>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"❌ Error in prediction: {e}")
                st.info("Please check all input values and try again.")

# Footer
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #6b7280; border-top: 1px solid #e5e7eb; margin-top: 3rem;">
    <p>💝 Built with Streamlit • AI-Powered Healthcare • © 2024</p>
    <p style="font-size: 0.9em;">This tool is for educational purposes only. Always consult healthcare professionals.</p>
</div>
""", unsafe_allow_html=True)
