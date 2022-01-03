# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 00:53:32 2021

@author: cprusty58@gmail.com
@name: Chandan Prusty

"""

import pandas as pd
import Dataframe_Reader
import Dataframe_Reader.dataCleaning as data
import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap
import cartopy.crs as crs
import cartopy.feature as cfeature
import warnings

warnings.filterwarnings("ignore")

current_directory = Dataframe_Reader.current_dir()
#print(current_directory)
#current_directory = current_directory[:current_directory.rindex("\\")]
dfAirportCoordinates = pd.read_csv(current_directory+ "\\airports_coordinates.csv")
print(len(dfAirportCoordinates))

dfAirports = data.dfClean[['airport','airport_name']].drop_duplicates().reset_index(drop = True)

dfAirports = pd.merge(dfAirports,dfAirportCoordinates, on='airport')


#4. Plotting out Airports in US map.
fig = plt.figure(figsize=(12,10))

ax = fig.add_subplot(1,1,1, projection=crs.PlateCarree())

ax.stock_img()
ax.coastlines()
ax.add_feature(cfeature.STATES)

ax.set_extent([-135, -66.5, 20, 55],
              crs=crs.PlateCarree()) ## Important


plt.scatter(x=dfAirports.long, y=dfAirports.lat,
            color="red",
            s=1,
            alpha=0.8,
            transform=crs.PlateCarree()) ## Important

plt.show()