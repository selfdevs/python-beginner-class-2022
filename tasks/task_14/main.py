# example dataframe
# import python pandas package
import pandas as pd

# import the numpy package
import numpy as np

# def pp(start, end, n):
#     start_u = start.value//10**9
#     end_u = end.value//10**9
#
#     return pd.DatetimeIndex((10**9*np.random.randint(start_u, end_u, n, dtype=np.int64)).view('M8[ns]'))
#
# # create a dataframe
# df = pd.DataFrame({'A': pp(pd.Timestamp('20130101'), pd.Timestamp('20130104'), 20), 'B': pp(pd.Timestamp('20140101'), pd.Timestamp('20140104'), 20)})
#
# df['time_diff'] = df['B'] - df['A']
# print(df)


# importing packages
import datetime
import pandas as pd

n_days = 10

# today's date in timestamp
base = pd.Timestamp.today()

# calculating timestamps for the next 10 days
timestamp_list = [base + datetime.timedelta(days=x) for x in range(5)]

# iterating through timestamp_list
for x in timestamp_list:
	print(x)

df = pd.DataFrame({'A': timestamp_list, 'B': timestamp_list})
df['time_diff'] = df['B'] - df['A']

print(df)
