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
    n_rows = self.df.shape[0]
    return n_rows

  def get_n_cols(self):
    """
      Return number of columns of loaded dataset
    """
    n_cols = self.df.shape[1]
    return n_cols

  def get_cols_list(self):
    """
      Return list column names of loaded dataset
    """
    cols_list = self.df.columns.map(str)
    return cols_list

  def get_cols_dtype(self):
    """
      Return dictionary with column name as keys and data type as values
    """
    #return self.df.dtypes.astype(str).reset_index().rename(columns={'index':'column', 0:'type'}).set_index('column')
    cols_dtype = self.df.dtypes.astype(str)#.to_dict()
    return cols_dtype
  
  def get_n_duplicates(self):
    """
      Return number of duplicated rows of loaded dataset
    """
    n_duplicates = sum(self.df.duplicated())
    return n_duplicates

  def get_n_missing(self):
    """
      Return number of rows with missing values of loaded dataset
    """
    n_missing = sum(self.df.isnull().any(axis=1))
    return n_missing

  def get_head(self, n):
    """
      Return Pandas Dataframe with top rows of loaded dataset
    """
    head = self.df.head(n)
    return head

  def get_tail(self, n):
    """
      Return Pandas Dataframe with bottom rows of loaded dataset
    """
    tail = self.df.tail(n)
    return tail

  def get_sample(self, n):
    """
      Return Pandas Dataframe with random sampled rows of loaded dataset
    """
    sample = self.df.sample(n)
    return sample

  def get_numeric_columns(self):
    """
      Return list column names of numeric type from loaded dataset
    """
    numeric_columns = self.df.select_dtypes(include='number')
    return numeric_columns

  def get_text_columns(self):
    """
      Return list column names of text type from loaded dataset
    """
    text_columns = self.df.select_dtypes(include='object')
    return text_columns

  def get_date_columns(self):
    """
      Return list column names of datetime type from loaded dataset
    """
    date_columns = self.df.select_dtypes(include=['datetime','timedelta'])
    return date_columns
