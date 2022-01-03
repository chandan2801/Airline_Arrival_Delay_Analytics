# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 23:48:30 2021

@author: cprusty58@gmail.com
@name: Chandan Prusty

"""
import pandas as pd
import Dataframe_Reader
import Dataframe_Reader.dataCleaning as data

print(len(data.dfClean))

resDf = data.dfClean.groupby(['airport','carrier']).arr_diverted.agg(len)

#5. Display the number of diverted flights for each carrier-airport pair.
crossDf = pd.crosstab(data.dfClean['carrier'], data.dfClean['airport'], values=data.dfClean['arr_diverted'], aggfunc='sum').fillna('')

