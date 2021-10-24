# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd


@dataclass
class TextColumn:
  col_name: str
  serie: pd.Series
  
  def get_name(self):
    """
    Return name of selected column
    """
    self.col_name = self.serie.name 
    return None

  def get_unique(self):
    """
    Return number of unique values for selected column
    """
    unique_vals = len(self.serie.unique())
    return unique_vals

  def get_missing(self):
    """
    Return number of missing values for selected column
    """
    na_count = self.series.isna().sum()
    return na_count

  def get_empty(self):
    """
    Return number of rows with empty string for selected column
    """
    empty_count = pd.isna(self.serie).sum()
    return empty_count

  def get_whitespace(self):
    """
    Return number of rows with only whitespaces for selected column
    """
    whitespace_count = self.serie.str.isspace().sum()
    return whitespace_count

  def get_lowercase(self):
    """
    Return number of rows with only lower case characters for selected column
    """
    lower_ocunt = self.serie.str.islower().sum()
    return lower_count

  def get_uppercase(self):
    """
    Return number of rows with only upper case characters for selected column
    """
    upper_count = self.serie.str.isupper().sum()
    return upper_count
  
  def get_alphabet(self):
    """
    Return number of rows with only alphabet characters for selected column
    """
    alphabet_count = self.serie.str.isalpha().sum()
    return alphabet_count

  def get_digit(self):
    """
    Return number of rows with only numbers as characters for selected column
    """
    digit_count = self.serie.str.isdigit().sum()
    return digit_count

  def get_mode(self):
    """
    Return the mode value for selected column
    """
    mode_val = ', '.join(self.serie.mode().tolist()
    return mode_val


  def get_barchart(self):
    """
    Return the generated bar chart for selected column
    """
    freq = self.serie.value_counts().to_frame().reset_index()
    fig = alt.Chart(freq, title='Bar Chart').mark_bar().encode(
        x=alt.X('index', title=self.col_name, sort=None), 
        y=alt.Y(col[1], title='Count of Records')
        ).configure_title(anchor='start')
    return fig

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    freq = self.serie.value_counts().to_frame().reset_index()
    freq.columns = ['value', 'occurrence']
    freq['percentage'] = freq['occurrence'] / freq['occurrence'].sum()
    return freq