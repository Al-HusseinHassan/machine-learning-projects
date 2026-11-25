import streamlit as st
import os
import joblib
from config import PROJECTS_PATH
from huggingface_hub import list_repo_files
from core.asset_loader import download_asset

def get_best_model():
    project_name = st.session_state.project
    project_path = f"machine-learning-projects-assets/{project_name}/"
    files_paths = list_repo_files(
        repo_id = st.secrets["HF_REPO_ID"],
        repo_type = "dataset",
        token = st.secrets["HF_TOKEN"]
    )
    for file_path in files_paths:
        if file_path.startswith(project_path) and file_path.endswith("best_model.joblib"):
            progress_container = st.empty()
            progress_bar = progress_container.progress(
                0,
                text="Preparing best model download..."
            )
            model_file = download_asset(file_path, progress_bar)
            best_model = joblib.load(model_file)
            progress_container.empty()
            return best_model
    return None


def get_features_types():
    project_name = st.session_state.project
    project_path = f"machine-learning-projects-assets/{project_name}/"
    files_paths = list_repo_files(
        repo_id = st.secrets["HF_REPO_ID"],
        repo_type = "dataset",
        token = st.secrets["HF_TOKEN"]
    )
    for file_path in files_paths:
        if file_path.startswith(project_path) and file_path.endswith("features_types.joblib"):
            progress_container = st.empty()
            progress_bar = progress_container.progress(
                0,
                text="Preparing features types download..."
            )
            features_types_file = download_asset(file_path, progress_bar)
            features_types = joblib.load(features_types_file)
            progress_container.empty()
            return features_types
    return None