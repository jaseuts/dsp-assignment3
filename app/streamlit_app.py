import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

from src import data, text, numeric, datetime

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
    
    # Student A Liam Huang 14035606
    uploadfile = st.file_uploader("Upload file", accept_multiple_files=False, key='csvupload')
    if uploadfile is not None:
        extension = uploadfile.name.split('.')[1]
        # To ensure a CSV file to be uploaded before the app proceeds to the next step of displaying information
        if extension.upper() != 'CSV':
            st.warning('**:warning: This app only accepts CSV file type. Please re-upload another file **')
            # st.info('**Please re-upload another file**')
        else:
            try:
                df = pd.read_csv(uploadfile)
                # initialise Dataset class object
                ds = data.Dataset(uploadfile.name, df)
            
                st.header('1. Overall Information')
                    
                st.markdown('**Name of Table: **' + str(ds.get_name()))
                if ds.get_n_rows() > 0:     
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


                # Student B
                    st.header('2. Numeric Column Information')
                    k = 1
                    for col in ds.get_numeric_columns():
                        dnc = numeric.NumericColumn(col, df[col])
                        st.subheader('2.' + str(k) + ' Field Name: ' + '_' + dnc.get_name() + '_')
                        k +=1
                        dnc_index = ['Number of Unique Values',
                                    'Number of Rows with Missing Values',
                                    'Number of Rows with 0','Number of Rows with Negative Values',
                                    'Average Value','Standard Deviation Value',
                                    'Minimum Value','Maximum Value','Median Value']
                        dnc_data = np.array([str(dnc.get_unique()), str(dnc.get_missing()), 
                                             str(dnc.get_zeros()),str(dnc.get_negatives()),
                                             str(dnc.get_mean()), str(dnc.get_std()), str(dnc.get_min()),
                                             str(dnc.get_max()),str(dnc.get_median())])
                        df_dnc = pd.DataFrame(index=dnc_index, data=dnc_data, columns=['value'])
                        st.dataframe(df_dnc)
                        st.markdown('**Histogram**')
                        st.altair_chart(dnc.get_histogram())
                        st.markdown('**Most Frequent Values**')
                        st.dataframe(dnc.get_frequent())
                
                
                # Student C Jason 01066846
                    st.header('3. Text Column Information')
                    i = 1
                    for col in ds.get_text_columns():
                        tc = text.TextColumn(serie=ds.df[col])
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
                    

                # Student D Darren 13867270
                    st.header('4. Datetime Column Information')
                    if ds.get_date_columns():
                        j = 1
                        for col in ds.get_date_columns():
                            date_col = datetime.DateColumn(col, df[col])
                            st.subheader('4.' + str(j) + ' Field Name: ' + '_' + date_col.get_name() + '_')
                            j += 1
                    
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
                    else:
                            st.warning('**:warning: No datetime columns detected.**')
                else:
                    st.warning('**:warning: The uploaded CSV file has no row of data, can not proceed to analysis, please try another CSV file!**')

            except pd.errors.EmptyDataError:
                st.warning('**:warning: The uploaded CSV file is empty (has no data)!**')      

                



if __name__ == '__main__':
    main()