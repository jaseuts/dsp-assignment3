# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd
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
        return self.serie.nunique()

    def get_missing(self):
        """
        Return number of missing values for selected column
        """
        return self.serie.isna().sum()

    def get_zeros(self):
        """
        Return number of occurrence of 0 value for selected column
        """
        return (self.serie == 0).sum(axis=0)

    def get_negatives(self):
        """
        Return number of negative values for selected column
        """
        return (self.serie < 0).sum(axis=0)

    def get_mean(self):
        """
        Return the average value for selected column
        """
        return self.serie.mean()

    def get_std(self):
        """
        Return the standard deviation value for selected column
        """
        return self.serie.std()
  
    def get_min(self):
        """
        Return the minimum value for selected column
        """
        return self.serie.min()

    def get_max(self):
        """
        Return the maximum value for selected column
        """
        return self.serie.max()

    def get_median(self):
        """
        Return the median value for selected column
        """
        return self.serie.median()

    def get_histogram(self):
        """
        Return the generated histogram for selected column
        """
        return alt.Chart(pd.DataFrame(self.serie)).mark_bar().encode(alt.X(self.col_name, bin=alt.Bin(maxbins=50)), y='count()',)

    def get_frequent(self):
        """
        Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
        """
        n = len(self.serie)
        if n >= 20:
	        buffer_value = self.serie.value_counts().head(20).index
	        buffer_data = self.serie.value_counts().head(20).values
	        df_buffer = pd.DataFrame({'value':buffer_value,'occurrence':buffer_data,'percentage':(buffer_data/self.serie.size)})
        else:
            buffer_value = self.serie.value_counts().head(n).index
            buffer_data = self.serie.value_counts().head(n).values
            df_buffer = pd.DataFrame({'value':buffer_value,'occurrence':buffer_data,'percentage':(buffer_data/self.serie.size)})
        return df_buffer