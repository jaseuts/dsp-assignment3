# To be filled by students
import unittest
from dataclasses import dataclass
from numpy import float64, nan
import pandas.util.testing
import pandas as pd
import numpy as np
import altair as alt

from src.numeric import NumericColumn

# set random seed to get reproducible
np.random.seed(123)
# numeric Dataset object
df_test_numeric_dummy = pandas.util.testing.makeDataFrame()

test_numeric_a = pd.Series(df_test_numeric_dummy['A'])

test_dummy_numeric_class = numeric.NumericColumn('A', test_numeric_a)


# dummy numeric Dataset object
# dummy numeric dataframe structure:
#                   A         B         C         D
#TcCIMrtQ75 -1.259659  0.893222 -0.145566  1.894676
#wHGXVjGUGV -0.385488  0.511878 -1.024901  1.105101
#zto9KGqeX3  0.758383 -0.869044 -1.757400  1.482068
#dcuNcuV49W -3.784642  2.398402 -1.249110 -0.599708
#hPJ8C0MHv2 -1.219263 -1.001390  1.058280  1.412895
#EBIHmOdQfa -0.369502  1.602473 -0.541819 -0.525902
#lI6kwnsKpR  0.123483  1.498786  2.571775  2.635685
#B9SE0gTZAq -0.533096  0.525211  1.347616 -1.368201
#go0Nl2hbR6  0.567914  0.831080  0.258946 -1.762127
#L3zYu4Xmsr -0.348613  0.022368 -0.348282 -0.553883
#bZS1PW4BXw -0.685031 -0.069009 -0.780482  1.119004
#ddlvzNPIdl  2.554368 -1.933373 -0.120759 -0.352290
#dZ4EgjxoMt -0.448151 -0.592466  0.088379  0.397137
#5gm2BMr9Uk -0.952395 -0.944294 -1.338411  0.132680
#J0JbVTqfOT  1.855988  1.301994 -1.968150  1.047859
#wUp7OzTXaJ -0.599239 -1.130536 -0.218138 -0.063608
#DbteEhDM8b  0.498082  1.656255  0.206562 -0.672409
#0mdSZhMygn -1.258226  1.098565 -0.856458  0.837372
#CSuK3WG5Oy  1.913999  0.236945  0.596262  0.665597
#066TniogbE -0.140763  1.647150 -1.439107  0.541241
#gO3kmmzQ7X -0.239352 -0.009658  0.627442  0.160226
#hnS7b3Po4x -2.823893 -0.992432 -0.307774 -0.049669
#HdryUxfHYL -2.324336  0.523320  1.654477  1.195414
#csUT5JsBU2 -0.076584 -0.931956  0.638576  1.050641
#3jrdlAC4lk -0.498165  2.266338  0.345144 -0.760375
#dT667xzB5U  2.076313  0.539784  0.141896 -0.071401
#7dJov72W4x -1.928535 -0.091474  1.075287 -0.502588
#xKefW48jcL  1.647860 -1.991864 -2.015380  0.764496
#Hf8jp7CckK -1.004482 -0.241881  0.214884 -0.823370
#dWdxB3ILXx -0.901356  0.210780 -1.050826  0.077420

class testDataClass(unittest.TestCase):
    def test_class_function(self):
        self.assertTrue(test_dummy_numeric_class.serie.equals(test_numeric_a))
        self.assertEqual(test_dummy_numeric_class.col_name, 'A')

    def test_get_name(self):
        self.assertEqual(test_dummy_numeric_class.get_name(), 'A')
        self.assertEqual(test_dummy_numeric_class.get_name(), test_dummy_numeric_class.col_name)

    def test_get_unique(self):
        # the serie has no repeated value
        self.assertEqual(test_dummy_numeric_class.get_unique(), len(test_dummy_numeric_class.serie))
        # test on temp serie with repeated values
        temp_data = {'a':1, 'b':2, 'c':1, 'd':1}
        temp = pd.Series(data=temp_data, index=['a','b','c','d'])
        temp_data_class = numeric.NumericColumn('temp', temp)
        self.assertEqual(temp_data_class.get_unique(), 2)

    def test_get_missing(self):
        self.assertEqual(test_dummy_numeric_class.get_missing(), 0)
        # test on temp serie with missing values
        temp_data = {'a':2, 'b':nan, 'c':nan, 'd':1}
        temp = pd.Series(data=temp_data, index=['a','b','c','d'])
        temp_data_class = numeric.NumericColumn('temp', temp)
        self.assertEqual(temp_data_class.get_unique(), 2)

    def test_get_zeros(self):
        self.assertEqual(test_dummy_numeric_class.get_zeros(), 0)
        # test on temp serie with 0 values
        temp_data = {'a':1, 'b':0, 'c':0, 'd':0}
        temp = pd.Series(data=temp_data, index=['a','b','c','d'])
        temp_data_class = numeric.NumericColumn('temp', temp)
        self.assertEqual(temp_data_class.get_zeros(), 3)

    def test_get_negatives(self):
        self.assertEqual(test_dummy_numeric_class.get_negatives(), 21)

    def test_get_mean(self):
        self.assertEqual(test_dummy_numeric_class.get_mean(), test_numeric_a.mean())

    def test_get_std(self):
        self.assertEqual(test_dummy_numeric_class.get_std(), test_numeric_a.std())

    def test_get_min(self):
        self.assertEqual(test_dummy_numeric_class.get_min(), test_numeric_a.min())
        
    def test_get_max(self):
        self.assertEqual(test_dummy_numeric_class.get_max(), test_numeric_a.max())

    def test_get_median(self):
        self.assertEqual(test_dummy_numeric_class.get_median(), test_numeric_a.median())

    def test_get_histogram(self):
        self.assertIsInstance(test_dummy_numeric_class.get_histogram(), alt.Chart)

    def test_get_frequent(self):
        self.assertIsInstance(test_dummy_numeric_class.get_frequent(), pd.DataFrame)
        self.assertEqual(test_dummy_numeric_class.get_frequent()['value'].tolist(), test_numeric_a.value_counts().head(20).index.tolist())
        self.assertEqual(test_dummy_numeric_class.get_frequent()['occurrence'].tolist(), test_numeric_a.value_counts().head(20).values.tolist())
        self.assertEqual(test_dummy_numeric_class.get_frequent()['percentage'].tolist(), (test_numeric_a.value_counts().head(20).values/len(test_numeric_a)).tolist())

        # use temp data series for testing (0 has 3 occurrences, 0.75 percentage . 1 has 1 occurrence, 0.25 percentage)
        temp_data = {'a':1, 'b':0, 'c':0, 'd':0}
        temp = pd.Series(data=temp_data, index=['a','b','c','d'])
        temp_data_class = numeric.NumericColumn('temp', temp)
        self.assertEqual(temp_data_class.get_frequent()['value'].tolist(), temp.value_counts().head(4).index.tolist())
        self.assertEqual(temp_data_class.get_frequent()['occurrence'].tolist(), temp.value_counts().head(4).values.tolist())
        self.assertEqual(temp_data_class.get_frequent()['percentage'].tolist(), (temp.value_counts().head(4).values/len(temp)).tolist())

if __name__ == '__main__':
    unittest.main()
