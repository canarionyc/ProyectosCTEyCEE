#%% setup
import pvlib
import os
os.chdir(r'C:\dev\pyCTE')
print( os.getcwd())

#%% Read EPW file
data, metadata = pvlib.iotools.read_epw('data/WeatherData/zonac_a3.epw')

# data is a pandas DataFrame with weather data
# metadata is a dictionary with location and other info
print(data.head())
print(metadata)
