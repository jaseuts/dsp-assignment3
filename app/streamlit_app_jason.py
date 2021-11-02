# WRITTEN BY JASON

import pandas as pd
import streamlit as st
import altair as alt

from src.data_jason import Dataset
from src.text import TextColumn

# In case the uploaded csv file has more than 5000 rows
alt.data_transformers.disable_max_rows()

def main():
    st.title('Data Explorer Tool')
    st.write('DSP Assignment 3 - Group 12')
    st.markdown('''
        **Authors**:
        * Darren Li
        * Jason Nguyen
        * Liam Huang
        * Nick Drage
    ''')
    st.write('##')
    
    upload_file = st.file_uploader('Choose a CSV file')
    
    if upload_file: 
        extension = upload_file.name.split('.')[1]
        # To ensure a CSV file to be uploaded before the app proceeds to the next step of displaying information
        if extension.upper() != 'CSV':
            st.warning('**:warning: This app only accepts CSV file type. Please re-upload another file **')
            # st.info('**Please re-upload another file**')
        else:
            try:
                data = pd.read_csv(upload_file)
                data.columns.name = upload_file.name  
                # Instantiate a Dataset class
                ds = Dataset(df=data)
                ds.get_name()

                st.header('1. Overall Information')
                '**Name of Table:**', ds.name
                '**Number of Rows:**', str(ds.get_n_rows())
                '**Number of Columns:**', str(ds.get_n_cols())
                '**Number of Duplicated Rows:**', str(ds.get_n_duplicates())
                '**Number of Rows with Missing Values:**', str(ds.get_n_missing())
                '**List of Columns:**'
                st.text(', '.join(ds.get_cols_list()))

                '**Type of Columns:**'
                st.dataframe(pd.DataFrame.from_dict(ds.get_cols_dtype(), orient='index', columns=['type']))
                
                rows = st.slider('Select the number of rows to be displayed', min_value=5, max_value=ds.df.shape[0], value=5)
                '**Top Rows of Table**'
                st.dataframe(ds.get_head(n=rows))

                '**Bottom Rows of Table**'
                st.dataframe(ds.get_tail(n=rows))

                '**Random Sample Rows of Table**'
                st.dataframe(ds.get_sample(n=rows))
                
                cols = st.multiselect('Which columns do you want to convert to dates', 
                                    ds.df.columns.tolist()
                                    )
                for col in cols:
                    if ds.df[col].dtypes in ['object', 'datetime']:
                        try:
                            ds.df[col] = pd.to_datetime(ds.df[col])
                            st.success('** Successfully converted column ' + col + ' into datetime**')
                        except ValueError as e:
                            st.error('Parsing column ' + col + ':\n\t to_datetime error (' + str(e) + ')')
                    else:
                        st.error("Column " + col + " has numeric type, shouldn't be converted into datetime")

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
                    
            except pd.errors.EmptyDataError:
                st.warning('**:warning: The uploaded CSV file is empty (has no data)!**')      

if __name__ == '__main__':
    main()
