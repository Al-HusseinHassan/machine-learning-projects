import streamlit as st
import os
import joblib
import pandas as pd
from config import PROJECTS_PATH
from core.model_features_loader import get_best_model, get_features_types

st.title("Prediction")


best_model = get_best_model()

if best_model is None:
    st.write("No Model Detected For This Dataset")
    st.stop()

if st.session_state.get('current_dataset') != st.session_state.dataset_path:

    st.session_state.current_dataset = st.session_state.dataset_path

    st.session_state.features_name = get_features_types()
    if st.session_state.features_name is None:
        st.write("No Features Detected For This Dataset")
        st.stop()        

    st.session_state.features_input = {}


for feature, itstype in st.session_state.features_name.items():
    if itstype == 'int64':
        st.session_state.features_input[feature] = st.number_input(feature, step = 1)
    elif itstype == 'float64':
        st.session_state.features_input[feature] = st.number_input(feature, step = 0.01)
    elif itstype == 'bool':
        st.session_state.features_input[feature] = st.selectbox(feature, [True, False])
    else:
        st.session_state.features_input[feature] = st.selectbox(feature, itstype)


if st.button("Predict"):
    with st.spinner("Predicting ..."):
        features = pd.DataFrame([st.session_state.features_input])
        prediction = best_model.predict(features)
        st.write("Prediction: ", prediction[0])