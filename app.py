from config import PROJECT_ROOT
import streamlit as st
import os
from core.data_loader import get_data, get_datasets_path

PAGES_PATH = os.path.join(PROJECT_ROOT, "pages")

overview_page = st.Page(f"{PAGES_PATH}/overview.py", title="Overview")
analysis_page = st.Page(f"{PAGES_PATH}/analysis.py", title="Analysis")
prediction_page = st.Page(f"{PAGES_PATH}/prediction.py", title="Prediction")

pages = st.navigation([overview_page, analysis_page, prediction_page])

with st.sidebar:
    datasets_path = get_datasets_path()
    projects_name = datasets_path.keys()
    project_name = st.selectbox("select the dataset to work with it", projects_name)
    st.session_state.project = project_name
    st.session_state.dataset_path = datasets_path[project_name]
    st.session_state.dataset = get_data(st.session_state.dataset_path)
    if st.session_state.dataset_path is not None:
        st.write(st.session_state.dataset_path)
    
pages.run()