# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd


@dataclass
class Dataset:
  name: str
  df: pd.DataFrame
  
  def get_name(self):
    """
    Return filename of loaded dataset
    """
    return self.name

  def get_n_rows(self):
    """
      Return number of rows of loaded dataset
    """
    return str(self.df.shape[0])

  def get_n_cols(self):
    """
      Return number of columns of loaded dataset
    """
    return str(self.df.shape[1])

  def get_cols_list(self):
    """
      Return list column names of loaded dataset
    """
    return self.df.columns.map(str)

  def get_cols_dtype(self):
    """
      Return dictionary with column name as keys and data type as values
    """
    #return self.df.dtypes.astype(str).reset_index().rename(columns={'index':'column', 0:'type'}).set_index('column')
    return self.df.dtypes.astype(str)#.to_dict()
  
  def get_n_duplicates(self):
    """
      Return number of duplicated rows of loaded dataset
    """
    return sum(self.df.duplicated())

  def get_n_missing(self):
    """
      Return number of rows with missing values of loaded dataset
    """
    return sum(self.df.isnull().any(axis=1))

  def get_head(self, n):
    """
      Return Pandas Dataframe with top rows of loaded dataset
    """
    return self.df.head(n)

  def get_tail(self, n):
    """
      Return Pandas Dataframe with bottom rows of loaded dataset
    """
    return self.df.tail(n)

  def get_sample(self, n):
    """
      Return Pandas Dataframe with random sampled rows of loaded dataset
    """
    return self.df.sample(n)

  def get_numeric_columns(self):
    """
      Return list column names of numeric type from loaded dataset
    """
    return self.df.select_dtypes(include='number')

  def get_text_columns(self):
    """
      Return list column names of text type from loaded dataset
    """
    return self.df.select_dtypes(include='object')

  def get_date_columns(self):
    """
      Return list column names of datetime type from loaded dataset
    """
    return self.df.select_dtypes(include=['datetime','timedelta'])
