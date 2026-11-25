import config
import streamlit as st
from core.extract_content import extract_specific_content

df = st.session_state.dataset

if df is not None:
    st.title(st.session_state.project)

    st.write("## Problem") 
    st.write("### Description")
    st.write(extract_specific_content("### Description"))
    st.write("### Solution")
    st.write(extract_specific_content("### Solution"))


    st.write("## Overview")

    n_rows =  len(df)
    columns = df.columns.to_list()

    selected_columns_to_show = st.multiselect("Select Columns To Show", columns, default=columns)
    selected_n_rows = st.slider("Select The Number Of Records", min_value = 0, max_value = n_rows, step=1, value=n_rows//4)
    st.write(st.session_state.dataset.loc[0:selected_n_rows, selected_columns_to_show])

    st.write("## Insights")
    st.write("Records")
    st.write(n_rows)
    st.write("Features")
    st.write(extract_specific_content("### Features"))
    st.write("Target")
    st.write(extract_specific_content("### Target"))

else:
    st.warning("Please Select Dataset To Start")
