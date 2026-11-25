from config import PROJECTS_PATH
import re
import streamlit as st
import os

def extract_specific_content(heading):

    project_name = st.session_state.project
    project_path = os.path.join(PROJECTS_PATH, project_name)
    readme_path = os.path.join(project_path, "README.md")

    if not os.path.exists(readme_path):
        return None
    
    with open(readme_path, encoding='utf-8') as file:
        content = file.read()

        pattern = f"{re.escape(heading)}(.*?)(?=\n### |\n## |\Z)"
        match = re.search(pattern, content, re.DOTALL)

        return match.group(1).strip() if match else None
