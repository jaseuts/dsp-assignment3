# To be filled by students
import streamlit as st
import pandas as pd

st.title('App Team 12 - Assignment 03')
uploadfile = st.file_uploader("Upload file", accept_multiple_files=False, type=['csv'], key='csvupload')
if uploadfile is not None:
    df = pd.read_csv(uploadfile, nrows=1000, parse_dates=['Date/Time'])
    upload = st.checkbox('Show data', key='csvcheck')
    if upload:    
        st.dataframe(df)

