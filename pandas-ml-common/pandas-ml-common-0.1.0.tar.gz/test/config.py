import os
from pandas_ml_common import pd


TEST_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "SPY.csv")
TEST_DF = pd.read_csv(TEST_FILE, index_col='Date', parse_dates=True)
