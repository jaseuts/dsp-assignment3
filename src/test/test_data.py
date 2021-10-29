# To be filled by students
import unittest
from dataclasses import dataclass
from numpy import float64
import pandas.util.testing
import pandas as pd

import sys
sys.path.insert(0, '..')

import data

# empty Dataset object
test_empty_data_class = data.Dataset()
n = 1

# dummy Dataset object
# dummy dataframe structure:
#   A       B       C       D
#0  0.0     0.0     foo1    2009-01-01
#1  1.0     1.0     foo3    2009-01-02
#2  2.0     0.0     foo2    2009-01-05
#3  3.0     1.0     foo4    2009-01-06
#4  4.0     0.0     foo5    2009-01-07
df_test_dummy = pandas.util.testing.makeMixedDataFrame()
# use dataframe name for the object:
name_df = 'df_test_dummy'
test_dummy_data_class = data.Dataset(name_df, df_test_dummy)
m = 2


class Test_Empty_Data(unittest.TestCase):    
    def test_empty_class_function(self):
        self.assertIsNone(test_empty_data_class.df)
        self.assertIsNone(test_empty_data_class.name)

    def test_empty_get_name(self):
        self.assertIsNone(test_empty_data_class.get_name())

    def test_empty_get_n_nows(self):    
        # get_n_rows() should raise AttributeError when none type dataframe is passed
        try:
            test_empty_data_class.get_n_rows()
        except AttributeError as e:
            assert e
        else:
            raise AssertionError('get_n_rows():Expected to raise ArributeError')

    def test_empty_get_n_cols(self):    
        # get_n_cols() should raise AttributeError when none type dataframe is passed
        try:
            test_empty_data_class.get_n_cols()
        except AttributeError as e:
            assert e
        else:
            raise AssertionError('get_n_cols():Expected to raise ArributeError')

    def test_empty_get_cols_list(self):    
        # get_cols_list() should raise AttributeError when none type dataframe is passed
        try:
            test_empty_data_class.get_cols_list()
        except AttributeError as e:
            assert e
        else:
            raise AssertionError('get_cols_list():Expected to raise ArributeError')
    
    def test_empty_get_cols_dtype(self):
        # get_cols_dtype() should raise AttributeError when none type dataframe is passed
        try:
            test_empty_data_class.get_cols_dtype()
        except AttributeError as e:
            assert e
        else:
            raise AssertionError('get_cols_dtype():Expected to raise ArributeError')

    def test_empty_get_n_duplicates(self):
        # get_n_duplicates() should raise AttributeError when none type dataframe is passed
        try:
            test_empty_data_class.get_n_duplicates()
        except AttributeError as e:
            assert e
        else:
            raise AssertionError('get_n_duplicates():Expected to raise ArributeError')

    def test_empty_get_n_missing(self):
        # get_n_missing() should raise AttributeError when none type dataframe is passed
        try:
            test_empty_data_class.get_n_missing()
        except AttributeError as e:
            assert e
        else:
            raise AssertionError('get_n_missing():Expected to raise ArributeError') 

    def test_empty_get_head(self):
        # get_head() should raise AttributeError when none type dataframe is passed
        try:
            test_empty_data_class.get_head(n)
        except AttributeError as e:
            assert e
        else:
            raise AssertionError('get_head():Expected to raise ArributeError') 

    def test_empty_get_tail(self):
        # get_tail() should raise AttributeError when none type dataframe is passed
        try:
            test_empty_data_class.get_tail(n)
        except AttributeError as e:
            assert e
        else:
            raise AssertionError('get_tail():Expected to raise ArributeError') 

    def test_empty_get_sample(self):
        # get_sample() should raise AttributeError when none type dataframe is passed
        try:
            test_empty_data_class.get_sample(n)
        except AttributeError as e:
            assert e
        else:
            raise AssertionError('get_sample():Expected to raise ArributeError')     

    def test_empty_get_numeric_columns(self):
        # get_numeric_columns() should raise AttributeError when none type dataframe is passed
        try:
            test_empty_data_class.get_numeric_columns()
        except AttributeError as e:
            assert e
        else:
            raise AssertionError('get_numeric_columns():Expected to raise ArributeError') 

    def test_empty_get_text_columns(self):
        # get_text_columns() should raise AttributeError when none type dataframe is passed
        try:
            test_empty_data_class.get_text_columns()
        except AttributeError as e:
            assert e
        else:
            raise AssertionError('get_text_columns():Expected to raise ArributeError') 

    def test_empty_get_date_columns(self):
        # get_date_columns() should raise AttributeError when none type dataframe is passed
        try:
            test_empty_data_class.get_date_columns()
        except AttributeError as e:
            assert e
        else:
            raise AssertionError('get_date_columns():Expected to raise ArributeError') 


class Test_Dummy_Data(unittest.TestCase):
    def test_dummy_class_function(self):
        self.assertEqual(test_dummy_data_class.name, name_df)
        self.assertTrue(df_test_dummy.equals(test_dummy_data_class.df))

    def test_dummy_get_name(self):
        self.assertEqual(test_dummy_data_class.get_name(), name_df)

    def test_dummy_get_n_rows(self):
        self.assertEqual(test_dummy_data_class.get_n_rows(), 5)

    def test_dummy_get_n_cols(self):
        self.assertEqual(test_dummy_data_class.get_n_cols(), 4)

    def test_dummy_get_cols_list(self):
        self.assertEqual(test_dummy_data_class.get_cols_list(), ['A', 'B', 'C', 'D'])

    def test_dummy_get_cols_dtype(self):
        self.assertEqual(test_dummy_data_class.get_cols_dtype(), {'A':'float64', 'B':'float64', 'C':'object', 'D':'datetime64[ns]'})
        obj_df = test_dummy_data_class.df.astype(object)
        obj_dummy_data_class = data.Dataset(name_df, obj_df)
        self.assertEqual(obj_dummy_data_class.get_cols_dtype(), {'A':'object', 'B':'object', 'C':'object', 'D':'object'})

    def test_dummy_get_n_duplicates(self):
        self.assertEqual(test_dummy_data_class.get_n_duplicates(), 0)
        dup_df = test_dummy_data_class.df.append(test_dummy_data_class.df)
        dup_dummy_data_class = data.Dataset(name_df, dup_df)
        self.assertEqual(dup_dummy_data_class.get_n_duplicates(), 5)

    def test_dummy_get_n_missing(self):
        self.assertEqual(test_dummy_data_class.get_n_missing(), 0)
        # replace all the 0 in the dataframe to None (Null)
        mis_df = test_dummy_data_class.df.replace([0], [None])
        mis_dummy_data_class = data.Dataset(name_df, mis_df)
        # 4 cells in 3 rows has 0 replaced to Null
        self.assertEqual(mis_dummy_data_class.get_n_missing(), 3)

    def test_dummy_get_head(self):
        self.assertTrue(df_test_dummy.head(m).equals(test_dummy_data_class.get_head(m)))

    def test_dummy_get_tail(self):
        self.assertTrue(df_test_dummy.tail(m).equals(test_dummy_data_class.get_tail(m)))

    def test_dummy_get_sample(self):
        # buffer the sample dataframe in case of sample function re-ran
        buffer_sample = test_dummy_data_class.get_sample(m)
        # use index for comparison
        self.assertTrue(buffer_sample.equals(df_test_dummy.iloc[buffer_sample.index]))

    def test_dummy_get_numeric_columns(self):
        self.assertEqual(test_dummy_data_class.get_numeric_columns(), ['A', 'B'])

    def test_dummy_get_text_columns(self):
        self.assertEqual(test_dummy_data_class.get_text_columns(), ['C'])

    def test_dummy_get_date_columns(self):
        self.assertEqual(test_dummy_data_class.get_date_columns(), ['D'])
    
    
if __name__ == '__main__':
    unittest.main()