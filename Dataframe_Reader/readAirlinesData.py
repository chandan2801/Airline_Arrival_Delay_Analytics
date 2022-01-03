# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 00:12:50 2021

@author: cprusty58@gmail.com
@name: Chandan Prusty

"""
import pandas as pd
import Dataframe_Reader

current_directory = Dataframe_Reader.current_dir()
print("current directory:",current_directory)
#current_directory = current_directory[:current_directory.rindex("\\")]

#print(current_directory)

#Reading 2018 airlines delay data
df2018 = pd.read_csv(current_directory + "\\delays_2018.csv")

#Reading 2019 airlines delay data
df2019 = pd.read_csv(current_directory + "\\delays_2019.csv")

#concat
airlinesDelayDf = pd.concat([df2018,df2019],ignore_index=True)

#1. Total Number of Rows Imported
print(len(airlinesDelayDf))



