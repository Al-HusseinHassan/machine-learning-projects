from config import PROJECTS_PATH
import pandas as pd
import os
from huggingface_hub import list_repo_files
import streamlit as st
from core.model_features_loader import get_best_model
from core.asset_loader import download_asset

def get_datasets_path():
    datasets_path = {}
    projects_names = os.listdir(PROJECTS_PATH)
    hf_files_paths = list_repo_files(
        st.secrets["HF_REPO_ID"],
        repo_type="dataset",
        token=st.secrets["HF_TOKEN"])
    for project_name in projects_names:
        hf_project_path = f"machine-learning-projects-assets/{project_name}/"
        for hf_project_file in hf_files_paths:
            if hf_project_file.startswith(hf_project_path) and hf_project_file.endswith(".csv"):
                hf_dataset_path = hf_project_file
                datasets_path[project_name] = hf_dataset_path
                break
    return datasets_path

def get_data(path: str, progress_bar) -> pd.DataFrame:
    dataset_path = download_asset(path, progress_bar)
    return pd.read_csv(dataset_path)