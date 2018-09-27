'''
CSIWx_EDA_092018.py imports comma-separaterd value Wx data from
 a text file, loads it into a pandas dataframe, where then the user can
 explore...

 Data used (initially) was downloaded from the WeatherFlow DataScope website
 for the period September 09 through the 15, 2018. All of the logged data for
 that time is included:

Station id: 148142  (spot id: 175109)
Station name and location: Croatan Sound at 35.8694 N, 75.66337 W
Station elevation = 0 feet, datum is unknown
Data units: mph, F, feet, mBars, sec, mm, %

Requirements (script written, tested, and run using):
- numpy: 1.14.3
- pandas: 0.23.4
- matplotlib:
- seaborn: 0.8.1

Created on Thu Sep 27 14:03:13 2018

@author: paulp
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# hey, I know that this is hard-coded (evil!) but just get over it, okay?
data_path = '/Users/paulp/GoogleDrive/projects/CSI_Wx/data/'
file_name = 'obs-175109-20180909_000000_to_20180915_235959.csv'

df = pd.read_csv(data_path + file_name).drop(['spot_id', 'name', 'lat', 'lon',
'ground_elevation', 'station_id', 'station_elevation', 'units_wind',
'units_temp'], axis=1)

# convert logger date-time strings to Python date time types:
df['timestamp_local'] = pd.to_datetime(df['timestamp_local'])
df['time_utc'] = pd.to_datetime(df['timestamp_utc'])

# set dataframe index to timestamp_utc:
df.set_index(df['time_utc'], drop=False, inplace=True)

# Q: Is there a correlation between sound water and air temperatures?
#   first, plot the two temperatures against one another:

plt.plot(df['time_utc'], df['atemp'], c='red')
plt.plot(df['time_utc'], df['wtemp'], c='blue')
plt.xticks(rotation = 45)
plt.show()
# this week included a visit from hurricane Florence, which almost certainly
# explains the seemingly unusual dip in the sound water temps beginning
# mid-week
df.corr()
