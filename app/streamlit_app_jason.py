# To be filled by students
import pandas as pd
import streamlit as st


from src.data import Dataset
from src.text import TextColumn

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
        if extension.upper() != 'CSV':
            st.warning('**:warning: This app only accepts CSV file type**')
            st.info('**Please re-upload another file**')
        else:
            data = pd.read_csv(upload_file)
            data.columns.name = upload_file.name           
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
            #st.write(pd.DataFrame(ds.df.dtypes).astype(str).to_dict())
            #st.dataframe(pd.DataFrame(ds.get_cols_dtype().items(), columns=['type']))
            st.write(pd.DataFrame.from_dict(ds.get_cols_dtype(), orient='index', columns=['type']))
            
            rows = st.slider('Select the number of rows to be displayed', min_value=5, max_value=ds.df.shape[0], value=5)
            '**Top Rows of Table**'
            ds.get_head(n=rows)

            '**Bottom Rows of Table**'
            ds.get_tail(n=rows)

            '**Random Sample Rows of Table**'
            ds.get_sample(n=rows)
            
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

            # for testing. remove later
            st.dataframe(pd.DataFrame.from_dict(ds.get_cols_dtype(), orient='index', columns=['type']))

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

        

if __name__ == '__main__':
    main()
