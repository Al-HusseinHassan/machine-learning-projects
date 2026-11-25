from config import PROJECTS_PATH
import pandas as pd
import os
import streamlit as st
from core.model_features_loader import get_best_model

def get_datasets_path():
    datasets_path = {}
    projects_names = os.listdir(PROJECTS_PATH)
    for project_name in projects_names:
        project_path = os.path.join(PROJECTS_PATH, project_name)
        project_files = os.listdir(project_path)
        for project_file in project_files:
            if project_file.endswith(".csv"):
                dataset_path = os.path.join(PROJECTS_PATH, project_name, project_file)
                datasets_path[project_name] = dataset_path
                break
    return datasets_path

def get_data(path:str) -> pd.DataFrame:
    return pd.read_csv(path)