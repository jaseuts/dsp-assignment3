import unittest
import pandas as pd
import datetime
import numpy as np
import altair as alt

from src.datetime import DateColumn

class TestDateTime(unittest.TestCase):
    def setUp(self) -> None:
        simple_dates = [datetime.datetime(2022,1,1),datetime.datetime(1900,1,1),
                        datetime.datetime(1900,1,1),datetime.datetime(1970,1,1)
                        ]
        bad_dates = [np.nan,None]
        self.simple_dates = DateColumn('simple',pd.Series(simple_dates))
        self.bad_dates = DateColumn('bad',pd.Series(bad_dates))
    
    def tearDown(self) -> None:
        del self.simple_dates
        del self.bad_dates
        

    def test_name(self):
        self.assertEqual( self.simple_dates.get_name(), 'simple')
        self.assertEqual( self.bad_dates.get_name(), 'bad')

    def test_unique(self):
        self.assertEqual( self.simple_dates.get_unique(), 3)
        self.assertEqual( self.bad_dates.get_unique(), 1)

    def test_missing(self):
        self.assertEqual( self.simple_dates.get_missing(), 0)
        self.assertEqual( self.bad_dates.get_missing(), 2)
    
    def test_weekend(self):
        self.assertEqual( self.simple_dates.get_weekend(), 1)
        self.assertEqual( self.bad_dates.get_weekend(), 0)

    def test_weekday(self):
        self.assertEqual( self.simple_dates.get_weekday(), 3)
        self.assertEqual( self.bad_dates.get_weekday(), 0)
    
    def test_future(self):
        self.assertEqual( self.simple_dates.get_future(), 1)
        self.assertEqual( self.bad_dates.get_future(), 0)
    
    def test_empty_1900(self):
        self.assertEqual( self.simple_dates.get_empty_1900(), 2)
        self.assertEqual( self.bad_dates.get_empty_1900(), 0)
    
    def test_empty_1970(self):
        self.assertEqual( self.simple_dates.get_empty_1970(), 1)
        self.assertEqual( self.bad_dates.get_empty_1970(), 0)
    
    def test_min(self):
        simple_min = datetime.datetime(1900,1,1)
        bad_min = self.bad_dates.get_min()
        self.assertEqual( self.simple_dates.get_min(), simple_min)
        self.assertTrue(np.isnan(bad_min))
    
    def test_max(self):
        simple_max = datetime.datetime(2022,1,1)
        bad_min = self.bad_dates.get_max()
        self.assertEqual( self.simple_dates.get_max(), simple_max)
        self.assertTrue(np.isnan(bad_min))

    def test_barchart(self):
        
        self.assertIsInstance(self.simple_dates.get_barchart(), alt.Chart)

    def test_frequency(self):
        actual_frame =pd.DataFrame(data={
            'Frequency':[2,1,1],
            'Percentage':[0.5,0.25,0.25]
        },index = [datetime.datetime(1900,1,1),datetime.datetime(2022,1,1),
                   datetime.datetime(1970,1,1)])

        return_df = self.simple_dates.get_frequent()
        self.assertTrue(return_df.equals(actual_frame))

if __name__ == '__main__':
    unittest.main()
    print('done!')