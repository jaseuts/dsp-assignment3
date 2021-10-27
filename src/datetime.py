import streamlit as st
import altair as alt
from dataclasses import dataclass
import pandas as pd
import datetime


@dataclass
class DateColumn:
  col_name: str
  serie: pd.Series

  def get_name(self):
    """
    Return name of selected column
    """
    return self.col_name

  def get_unique(self):
    """
    Return number of unique values for selected column
    """
    unique = self.serie.unique()
    return len(unique)

  def get_missing(self):
    """
    Return number of missing values for selected column
    """
    missing = self.serie.isna()
    return sum(missing)

  def get_weekend(self):
    """
    Return number of occurrence of days falling during weekend (Saturday and Sunday)
    """
    dates = self.serie
    weekend = dates[(dates.dt.weekday == 5) | (dates.dt.weekday == 6)]
    return len(weekend)

  def get_weekday(self):
    """
    Return number of weekday days (not Saturday or Sunday)
    """
    dates = self.serie
    weekday = dates[(dates.dt.weekday != 5) & (dates.dt.weekday != 6)]
    return len(weekday)
  
  def get_future(self):
    """
    Return number of cases with future dates (after today)
    """
    now = datetime.datetime.now()
    dates = self.serie
    future = dates[dates.dt.date > now.date()]
    return len(future)

  def get_empty_1900(self):
    """
    Return number of occurrence of 1900-01-01 value
    """
    dates = self.serie
    date_1900 = dates[dates.dt.date == datetime.date(1900,1,1)]
    return len(date_1900)

  def get_empty_1970(self):
    """
    Return number of occurrence of 1970-01-01 value
    """
    dates = self.serie
    date_1970 = dates[dates.dt.date == datetime.date(1970,1,1)]
    return len(date_1970)

  def get_min(self):
    """
    Return the minimum date
    """
    return min(self.serie)

  def get_max(self):
    """
    Return the maximum date 
    """
    return max(self.serie)

  def get_barchart(self):
    """
    Return the generated bar chart for selected column
    """
    freq = self.serie.value_counts().to_frame().reset_index()
    fig = alt.Chart(freq, title='Bar Chart').mark_bar().encode(
        x=alt.X('index', title=self.col_name, sort=None), 
        y=alt.Y(0, title='Count of Dates')
        ).configure_title(anchor='start')
    return None

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    counts = self.serie.value_counts()
    percents = self.serie.value_counts(normalize=True)
    freq_df = pd.DataFrame(data={
          'Frequency':counts,
          'Percetage':percents
          })
    freq_df = freq_df.sort_values('Frequency',ascending=False)
    return freq_df.head(20)