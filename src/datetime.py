# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd
import datetime


@dataclass
class DateColumn:
  col_name: str
  series: pd.Series

  def get_name(self):
    """
    Return name of selected column
    """
    return self.col_name

  def get_unique(self):
    """
    Return number of unique values for selected column
    """
    unique = self.series.unique()
    return len(unique)

  def get_missing(self):
    """
    Return number of missing values for selected column
    """
    missing = self.series.isna()
    return sum(missing)

  def get_weekend(self):
    """
    Return number of occurrence of days falling during weekend (Saturday and Sunday)
    """
    dates = self.series
    weekend = dates[(dates.dt.weekday == 5) | (dates.dt.weekday == 6)]
    return len(weekend)

  def get_weekday(self):
    """
    Return number of weekday days (not Saturday or Sunday)
    """
    dates = self.series
    weekday = dates[(dates.dt.weekday != 5) & (dates.dt.weekday != 6)]
    return len(weekday)
  
  def get_future(self):
    """
    Return number of cases with future dates (after today)
    """
    now = datetime.datetime.now()
    dates = self.series
    future = dates[dates.dt.date > now.date()]
    return None

  def get_empty_1900(self):
    """
    Return number of occurrence of 1900-01-01 value
    """
    dates = self.series
    date_1900 = dates[dates.dt.date == datetime.date(1900,1,1)]
    return len(date_1900)

  def get_empty_1970(self):
    """
    Return number of occurrence of 1970-01-01 value
    """
    dates = self.series
    date_1970 = dates[dates.dt.date == datetime.date(1970,1,1)]
    return len(date_1970)
    return None

  def get_min(self):
    """
    Return the minimum date
    """
    return min(self.series)

  def get_max(self):
    """
    Return the maximum date 
    """
    return max(self.series)

  def get_barchart(self):
    """
    Return the generated bar chart for selected column
    """
    return None

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    return None