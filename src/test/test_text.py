# WRITTEN BY JASON

import unittest
import pandas as pd
import altair as alt
from io import StringIO
from pandas.testing import assert_frame_equal

# Prefer to <set PYTHONPATH "${PYTHONPATH}:/path/to/the/project/folder">
# in the Dockerfile than to <set ENV PYTHONPATH "${PYTHONPATH}:/src">

from src.text import TextColumn



data = """
index,contributed_by
1,LIAM
2,Darren
3,jason
4,Nick
5, 
6,LIAM
7,
8,jason
"""
df = pd.read_csv(StringIO(data))

tc = TextColumn(serie=df['contributed_by'])

class TestTextColumnClass(unittest.TestCase):
    def test_get_name(self):
        tc.get_name()
        self.assertEqual(tc.col_name, 'contributed_by')
              
    def test_get_unique(self):
        result = tc.get_unique()
        self.assertEqual(result, 6)       
        
    def test_get_missing(self):
        result = tc.get_missing()
        self.assertEqual(result, 1)

    def test_gget_empty(self):
        result = tc.get_empty()
        self.assertEqual(result, 1)
    
    def test_get_whitespace(self):
        result = tc.get_whitespace()
        self.assertEqual(result, 1)
        
    def test_get_lowercase(self):
        result = tc.get_lowercase()
        self.assertEqual(result, 2)   
        
    def test_get_uppercase(self):
        result = tc.get_uppercase()
        self.assertEqual(result, 2) 
        
    def test_get_alphabet(self):
        result = tc.get_alphabet()
        self.assertEqual(result, 6)    
        
    def test_get_digit(self):
        result = tc.get_digit()
        self.assertEqual(result, 0)
        
    def test_get_mode(self):
        result = tc.get_mode()
        self.assertEqual(result, 'LIAM, jason')

      
    def test_get_barchart(self):
        freq = df['contributed_by'].value_counts().to_frame().reset_index()
        
        tc.get_name()
        result = tc.get_barchart() 
        
        assert_frame_equal(result.data, freq)
        self.assertEqual(result.title, 'Bar Chart')
        self.assertEqual(result.mark, 'bar')
        self.assertEqual(result.encoding['x']['title'], 'contributed_by')
        self.assertEqual(result.encoding['y']['title'], 'Count of Records')
        
if __name__ == '__main__':
    unittest.main()