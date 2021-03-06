# To be filled by students
from typing import Sized
import streamlit as st
from dataclasses import dataclass
import pandas as pd
import math
import altair as alt


# In case the uploaded csv file has more than 5000 rows
alt.data_transformers.disable_max_rows()



@dataclass
class NumericColumn:
    col_name: str = None
    serie: pd.Series = None
 
    def get_name(self):
        """
        Return name of selected column
        """
        return self.col_name

    def get_unique(self):
        """
        Return number of unique values for selected column
        """
        numberunique = self.serie.nunique()
        return numberunique

    def get_missing(self):
        """
        Return number of missing values for selected column
        """
        missing_value = self.serie.isna().sum()
        return missing_value

    def get_zeros(self):
        """
        Return number of occurrence of 0 value for selected column
        """
        numberofzeros = (self.serie == 0).sum(axis=0)
        return numberofzeros

    def get_negatives(self):
        """
        Return number of negative values for selected column
        """
        negativevals = (self.serie < 0).sum(axis=0)
        return negativevals

    def get_mean(self):
        """
        Return the average value for selected column
        """
        averagevalue = self.serie.mean()
        return averagevalue

    def get_std(self):
        """
        Return the standard deviation value for selected column
        """
        standarddev = self.serie.std()
        return standarddev
  
    def get_min(self):
        """
        Return the minimum value for selected column
        """
        minval = self.serie.min()
        return minval

    def get_max(self):
        """
        Return the maximum value for selected column
        """
        maxval = self.serie.max()
        return maxval

    def get_median(self):
        """
        Return the median value for selected column
        """
        medvalue = self.serie.median()
        if math.isnan(medvalue):
            st.warning(self.col_name + ' column has no values')
        return medvalue

    def get_histogram(self):
        """
        Return the generated histogram for selected column
        """
        return alt.Chart(pd.DataFrame(self.serie)).mark_bar().encode(alt.X(self.col_name, bin=alt.Bin(maxbins=50)), y='count()',)

    def get_frequent(self):
        """
        Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
        """
        n = 20
        if n <= self.get_unique():
	        buffer_value = self.serie.value_counts().head(20).index
	        buffer_data = self.serie.value_counts().head(20).values
	        df_buffer = pd.DataFrame({'value':buffer_value,'occurrence':buffer_data,'percentage':(buffer_data/self.serie.size)})
        else:
            n = self.get_unique()
            buffer_value = self.serie.value_counts().head(n).index
            buffer_data = self.serie.value_counts().head(n).values
            df_buffer = pd.DataFrame({'value':buffer_value,'occurrence':buffer_data,'percentage':(buffer_data/self.serie.size)})
            st.warning('There is less then 20 records,  ' + str(n) + ' will only be displayed')

        return df_buffer

