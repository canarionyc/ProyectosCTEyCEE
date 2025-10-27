#%%
import os
print(os.getcwd())
import epw



#%% Read an EPW file
epw_data = epw.epw()
epw_data.read('data/WeatherData/zonac_a3.epw')

# Access weather data
weather_data = epw_data.weatherdata
location_data = epw_data.location
