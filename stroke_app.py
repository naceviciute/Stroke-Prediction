import streamlit as st
import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder, OneHotEncoder
from sklearn.linear_model import LogisticRegression

X_train = pd.read_csv('X_train.csv')

numeric_features = ["age", "avg_glucose_level", "bmi"]
binary_features = ["gender", "hypertension", "heart_disease", "ever_married", "Residence_type"]
categorical_features = ["work_type", "smoking_status"]

numeric_transformer = StandardScaler()
binary_transformer = OrdinalEncoder()
categorical_transformer = OneHotEncoder(handle_unknown="ignore")

preprocessor = ColumnTransformer(
    transformers=[
        ("numeric", numeric_transformer, numeric_features),
        ("binary", binary_transformer, binary_features),
        ("categorical", categorical_transformer, categorical_features)
    ]
)

preprocessor.fit(X_train)

logreg_model = joblib.load('logreg_model.joblib')  # You need to replace this with your trained logistic regression model

st.set_page_config(page_title="Stroke Prediction")
st.title('Stroke Prediction')

with st.expander('About this app'):
  st.markdown('**What can this app do?**')
  st.info('This app helps users to assess their risk of stroke based on their personal data. Given their demographic and health information, a predictive model analyzes this data to determine whether a person is in a risk group for stroke.')

  st.markdown('**How to use the app?**')
  st.warning('To engage with the app, go to the sidebar and fill in the data.')

with st.sidebar:
    st.header('Input data')

    with st.container():
        gender = st.radio('Gender', ['Male', 'Female'])
        age = st.slider('Age', min_value=0, max_value=90, value=20, step=1)
        hypertension = st.selectbox('Hypertension', ['Yes', 'No'])
        heart_disease = st.selectbox('Heart Disease', ['Yes', 'No'])
        ever_married = st.selectbox('Ever Married', ['Yes', 'No'])
        work_type = st.selectbox('Work Type', ['Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked'])
        Residence_type = st.selectbox('Residence Type', ['Urban', 'Rural'])
        bmi = st.slider('BMI', min_value=10.0, max_value=100.0, value=25.0, step=0.1)
        avg_glucose_level = st.slider('Average Glucose Level', min_value=50, max_value=250, value=100, step=1)
        smoking_status = st.selectbox('Smoking Status', ['Unknown', 'never smoked', 'formerly smoked', 'smokes'])
    
input_data = pd.DataFrame({
    'gender': [gender],
    'age': [age],
    'hypertension': [1 if hypertension == 'Yes' else 0],
    'heart_disease': [1 if heart_disease == 'Yes' else 0],
    'ever_married': [ever_married],
    'work_type': [work_type],
    'Residence_type': [Residence_type],
    'avg_glucose_level': [avg_glucose_level],
    'bmi': [bmi],
    'smoking_status': [smoking_status]
})

preprocessed_data = preprocessor.transform(input_data)

y_pred_logreg = logreg_model.predict_proba(preprocessed_data)

new_threshold = 0.52

prob_positive_log = y_pred_logreg[:, 1]
y_pred_adj_log = (prob_positive_log >= new_threshold).astype(int)

if y_pred_adj_log[0] == 1:
    st.error("High Risk of Stroke")
else:
    st.success("No Risk of Stroke")