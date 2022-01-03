# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 00:49:50 2021

@author: cprusty58@gmail.com
@name: Chandan Prusty

"""
import pandas as pd
import Dataframe_Reader.readAirlinesData as data

#print(data.airlinesDelayDf.columns)

dfClean = data.airlinesDelayDf
dfClean['date'] = pd.to_datetime(dfClean['date'],format='%Y-%m').dt.strftime('%Y-%m')

print("Count of Records Before Cleaning --> ",len(dfClean))

#2. Data Cleaning and Filtering the unneccessary records
dfClean = dfClean[(dfClean['date']>='2018-01') & (dfClean['date']<='2019-12') & (dfClean['arr_flights'].notnull())
                  & (dfClean['carrier'].notnull()) & (dfClean['carrier_name'].notnull()) &
                      (dfClean['airport'].notnull()) & (dfClean['airport_name'].notnull())]

print("Count of Records After Cleaning -->", len(dfClean))

#3. Filtering Only tenessee airports
tenessee_airports = dfClean.loc[dfClean.airport_name.str.contains("TN")]
print("Tenessee Airports")
print(tenessee_airports.airport_name.unique())

#Another Way
sampleDf = dfClean
sampleDf['TN'] = sampleDf['airport_name'].map(lambda x: x.find("TN"))

lstTN = set(sampleDf[sampleDf['TN']!=-1]['airport_name'])
print(lstTN)

