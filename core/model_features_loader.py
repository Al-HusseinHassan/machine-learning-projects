import streamlit as st
import os
import joblib
from config import PROJECTS_PATH

def get_best_model():
    project_name = st.session_state.project
    project_path = os.path.join(PROJECTS_PATH, project_name)
    project_files = os.listdir(project_path)
    for file in project_files:
        if file == 'best_model.joblib':
            file_path = os.path.join(project_path, file)
            best_model = joblib.load(file_path)
            return best_model
    return None

def get_features_types():
    project_name = st.session_state.project
    project_path = os.path.join(PROJECTS_PATH, project_name)
    project_files = os.listdir(project_path)
    for file in project_files:
        if file == 'features_types.joblib':
            file_path = os.path.join(project_path, file)
            features_types = joblib.load(file_path)
            return features_types
    return None