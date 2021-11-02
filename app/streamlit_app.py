import streamlit as st
import pandas as pd
import numpy as np

from src import data, text, numeric, datetime


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

    
    #uploadfile = st.file_uploader("Upload file", accept_multiple_files=False, type=['csv'], key='csvupload')
    uploadfile = st.file_uploader('Choose a CSV file')

    if uploadfile is not None:

        extension = uploadfile.name.split('.')[1]
        # To ensure a CSV file to be uploaded before the app proceeds to the next step of displaying information
        if extension.upper() != 'CSV':
            st.warning('**:warning: This app only accepts CSV file type. Please re-upload another file **')
            # st.info('**Please re-upload another file**')
        else:
            try:
                df = pd.read_csv(uploadfile)

        #if df.empty:
        #    st.error('Please upload a non-empty csv file')
        #else:
            # initialise Dataset class object
                ds = data.Dataset(uploadfile.name, df)

    # Student A 
                st.header('1. Overall Information')            
                st.markdown('**Name of Table: **' + str(ds.get_name()))           
                st.markdown('**Number of Rows: **' + str(ds.get_n_rows()))           
                st.markdown('**Number of Columns: **' + str(ds.get_n_cols()))          
                st.markdown('**Number of Duplicated Rows: **' + str(ds.get_n_duplicates()))
                st.markdown('**Number of Rows with missing Values: **' + str(ds.get_n_missing()))
                st.markdown('**List of Columns: **')
                st.write(', '.join(ds.get_cols_list()))
                st.markdown('**Type of Columns: **')
                st.dataframe(pd.DataFrame(ds.get_cols_dtype(), index=['type']).transpose())
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
                # data seperation by types
                multi_option = st.multiselect('Which columns do you want to convert to dates', (df.columns))
                try:
                    for mo in multi_option:
                        ds.df[mo] = pd.to_datetime(ds.df[mo])         
                    col_numeric = ds.df[ds.get_numeric_columns()]  # numeric dataframe
                    col_text = ds.df[ds.get_text_columns()]        # object dataframe (may need to convert to string)
                    col_date = ds.df[ds.get_date_columns()]        # date dataframe
                    #st.write(ds.get_cols_dtype())
                except:
                    st.error('This data type is not available, try something else')


    # Student B
                st.header('2. Numeric Column Information')

    

    # Student C
                st.header('3. Text Column Information')



    # Student D

                st.header('4. Datetime Column Information')
                date_option = st.selectbox('Which column do you want to look at?', (col_date))
                if date_option:
                    date_col = datetime.DateColumn(date_option,df[date_option])
                    st.subheader('Field Name: ' + date_col.get_name())
                    date_index = ['Number of Unique Values','Number of Rows with Missing Values',
                                 'Number of Weekend Dates','Number of Weekday Dates',
                                 'Number of Dates in Future','Count of 1900-01-01',
                                 'Count of 1970-01-01', 'Minimum Value','Maximium Value']
                    date_attr = [date_col.get_unique(),date_col.get_missing(), date_col.get_weekend(),
                                date_col.get_weekday(),date_col.get_future(), date_col.get_empty_1900(),
                                date_col.get_empty_1970(),date_col.get_min(),date_col.get_max()]
                    date_attr = [str(i) for i in date_attr]
                    attr_df = pd.DataFrame(data = date_attr,index=date_index,columns=['Value'])
                    st.table(attr_df)

                    st.altair_chart(date_col.get_barchart(), use_container_width=True)

                    st.table(date_col.get_frequent())
                    
            
            except pd.errors.EmptyDataError:
                st.warning('**:warning: The uploaded CSV file is empty (has no data)!**')
        


if __name__ == '__main__':
    main()