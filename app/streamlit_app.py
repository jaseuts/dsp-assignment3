# To be filled by students
import streamlit as st
import pandas as pd
import numpy as np

from src import data, text, numeric, datetime




def main():
    st.title('App Team 12 - Assignment 03')

    # Student A
    uploadfile = st.file_uploader("Upload file", accept_multiple_files=False, type=['csv'], key='csvupload')
    if uploadfile is not None:
        df = pd.read_csv(uploadfile)
        # initialise Dataset class object
        ds = data.Dataset(uploadfile.name, df)
     
        st.header('1. Overall Information')
            
        #st.markdown('**Name of File: **' + ds.get_name())
            
        st.markdown('**Number of Rows: **' + str(ds.get_n_rows()))
            
        st.markdown('**Number of Columns: **' + str(ds.get_n_cols()))
            
        st.markdown('**Number of Duplicated Rows: **' + str(ds.get_n_duplicates()))
            
        st.markdown('**Number of Rows with missing Values: **' + str(ds.get_n_missing()))
            
        st.markdown('**List of Columns: **')
        st.write(', '.join(ds.get_cols_list()))
            
        st.markdown('**Type of Columns: **')
        st.dataframe(pd.DataFrame(ds.get_cols_dtype()).rename(columns={0:'type'}))
        
        number = st.slider('Select the number of rows to be displayed', min_value=1, max_value=df.shape[0], key='slider01')
        st.markdown('**Top Rows of Table: **')
        st.dataframe(ds.get_head(number))
        st.markdown('**Botton Rows of Table **')
        st.dataframe(ds.get_tail(number))
        st.markdown('**Random Sample Rows of Table **')
        st.dataframe(ds.get_sample(number))     
            
        #option = st.selectbox('Which column do you want to convert to date', (df.columns.insert(0, '<select>')), index=0, key='selectionbox01')
        #try:
        #    ds.df[option] = pd.to_datetime(ds.df[option])
        #    st.write(ds.get_cols_dtype())
        #except:
        #    st.error('Data type not available, try something else')     

        multi_option = st.multiselect('Which columns do you want to convert to dates', (df.columns))
        try:
            for mo in multi_option:
                ds.df[mo] = pd.to_datetime(ds.df[mo])         
            col_numeric = ds.get_numeric_columns()  # numeric dataframe
            col_string = ds.get_text_columns()      # object dataframe (may need to convert to string)
            col_date = ds.get_date_columns()        # date dataframe
            #st.write(ds.get_cols_dtype())
        except:
            st.error('This data type is not available, try something else')

    # Student B
        st.header('2. Numeric Column Information')

    
    # Student C
        st.header('3. Text Column Information')

    
    # Student D
        
        



if __name__ == '__main__':
    main()