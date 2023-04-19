# -*- coding: utf-8 -*-
"""homework-1-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OAWx3IEzVr8ZSCSNsMKA4G_vpoxvdVhD
"""

import pandas as pd
import numpy as np

df=pd.read_csv("project_data.csv")

print(df.shape)

df_close=df[["<CLOSE>"]]
df_day=df[["<DTYYYYMMDD>"]]

from numpy.ma.core import reshape
l=len(df_close)
print(l)
values_close=reshape(df_close,(1,len(df_close)))
days=reshape(df_day,(1,len(df_day)))

values_close_arr=np.array(values_close)
days_arr=np.array(days)

import matplotlib.pyplot as plt

df_close_arr=df_close.values
df_day_arr=df_day.values

plt.plot(df_day_arr,df_close_arr)

dy=df_close_arr[1:]-df_close_arr[:-1]
dx=df_day_arr[1:]-df_day_arr[:-1]

ydot=dy/dx
plt.plot(df_day_arr[:-1],ydot,label="ydot")

sets=[]
sets_predict=[]

len_df=df_close_arr.size
len_set=10
len_sets=len_df-len_set+1
for i in range(0,len_sets):
  sets.append(df_close_arr[i:i+len_set])
  if i==(len_sets-1):
    print(i)
    break
  if df_close_arr[i+len_set]>df_close_arr[i+len_set-1]:
    val="True"
  else:
    val="False"
  sets_predict.append(val) 

print(sets[0:2])
print(sets_predict[0:15])