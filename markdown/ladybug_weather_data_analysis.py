#%%
from ladybug.epw import EPW
import os
os.chdir(r'C:\dev\pyCTE')
print( os.getcwd())


#%% Read EPW file
epw_data = EPW('data/WeatherData/zonac_a3.epw')

# Access location data
location = epw_data.location
print(location)
#%%
dry_bulb_temp = epw_data.dry_bulb_temperature
print(dry_bulb_temp)

relative_humidity = epw_data.relative_humidity
print(relative_humidity)
