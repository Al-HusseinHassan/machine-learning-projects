import streamlit as st
import joblib
from huggingface_hub import list_repo_files
from core.asset_loader import download_asset

def get_ready_asset(file_type, progress_message):
    project_name = st.session_state.project
    project_path = f"machine-learning-projects-assets/{project_name}/"
    files_paths = list_repo_files(
        repo_id = st.secrets["HF_REPO_ID"],
        repo_type = "dataset",
        token = st.secrets["HF_TOKEN"]
    )
    for file_path in files_paths:
        if file_path.startswith(project_path) and file_path.endswith(file_type):
            progress_container = st.empty()
            progress_bar = progress_container.progress(
                0,
                text=progress_message
            )
            asset_file = download_asset(file_path, progress_bar)
            asset = joblib.load(asset_file)
            progress_container.empty()
            return asset
    return None