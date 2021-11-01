# To be filled by students
import streamlit as st
import pandas as pd
import numpy as np

import sys
sys.path.insert(0, '../src')

import data
import numeric


def main():
    st.title('App Team 12 - Assignment 03')

    # Student A
    uploadfile = st.file_uploader("Upload file", accept_multiple_files=False, type=['csv'], key='csvupload')
    if uploadfile is not None:
        df = pd.read_csv(uploadfile)
        # initialise Dataset class object
        ds = data.Dataset(uploadfile.name, df)
     
        st.header('1. Overall Information')
            
        st.markdown('**Name of Table: **' + ds.get_name())
            
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

    
    # Student C (jason 01066846)
        st.header('3. Text Column Information')
        i = 1
        for col in ds.get_text_columns():
            tc = TextColumn(serie=ds.df[col])
            tc.get_name()
            st.subheader('3.' + str(i) + ' Field Name: ' + '_' + tc.col_name + '_')
            i += 1

            content = {'Number of Unique Values': tc.get_unique(),
                'Number of Rows with Missing Values': tc.get_missing(),
                'Number of Empty Rows': tc.get_empty(),
                'Number of Rows with Only Whitespace': tc.get_whitespace(),
                'Number of Rows with Only Lowercases': tc.get_lowercase(),
                'Number of Rows with Only Uppercases': tc.get_uppercase(),
                'Number of Rows with Only Alphabet': tc.get_alphabet(),
                'Number of Rows with Only Digits': tc.get_digit(),
                'Mode Value': tc.get_mode()
            }   

            info = pd.DataFrame.from_dict(content, orient='index', columns=['value']).astype(str)
            st.dataframe(info)

            st.altair_chart(tc.get_barchart(), use_container_width=True)
            
            st.dataframe(tc.get_frequent())
        

    
    # Student D
        st.header('4. Datetime Column Information')



if __name__ == '__main__':
    main()