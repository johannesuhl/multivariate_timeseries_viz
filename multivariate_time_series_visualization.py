# -*- coding: utf-8 -*-
"""
Created on Sun Nov 08 05:57:16 2020

@author: Johannes
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib
matplotlib.rcParams['font.sans-serif'] = "Arial"
matplotlib.rcParams['font.family'] = "sans-serif"
matplotlib.rcParams['font.size'] = 4 

##### load template time series data from UCI Machine Learning Repository
##### Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.
##### we use the Ozone Level Detection Data Set (Zhang et al.)
##### https://archive.ics.uci.edu/ml/datasets/ozone+level+detection

### the 8-hours dataset:
dataurl=r'https://archive.ics.uci.edu/ml/machine-learning-databases/ozone/eighthr.data'
namesurl=r'https://archive.ics.uci.edu/ml/machine-learning-databases/ozone/eighthr.names'
data = pd.read_csv(dataurl,sep=",",header=None)
data = data.drop(labels=data.columns[-1],axis=1)
colnames = pd.read_csv(namesurl,sep=":")

### the 1-hours dataset:
#dataurl=r'https://archive.ics.uci.edu/ml/machine-learning-databases/ozone/onehr.data'
#namesurl=r'https://archive.ics.uci.edu/ml/machine-learning-databases/ozone/onehr.names'
#data = pd.read_csv(dataurl,sep=",",header=None)
#data = data.drop(labels=data.columns[-1],axis=1)
#colnames = pd.read_csv(namesurl,sep=":",skiprows=53)

data.columns=colnames[colnames.columns[0]].values
data=data.replace('?',np.nan)
data=data.dropna()
for col in data.columns[1:]:
    data[col]=data[col].map(float)
plotarr = np.rot90(data.drop(labels='Date',axis=1).values)

plotarr_scaled = []
#scale the time series of each variable between 0 and 1:
scaler = MinMaxScaler(feature_range=(0, 1))
for row in plotarr:                
    X = row
    Xres = X.reshape(-1, 1)
    scaler.fit(Xres)
    Xtrans = scaler.transform(Xres)  
    rescaled = Xtrans.reshape(1, -1)[0]
    plotarr_scaled.append(rescaled)                  
plotarr_scaled=np.array(plotarr_scaled)


fig, ax = plt.subplots(figsize=(10, 5))
ax.grid(False)
plt.imshow(plotarr_scaled, interpolation='none', cmap='spectral', aspect='auto')
ax.set_xticks(np.arange(len(data))[::25])
ax.set_xticklabels(data.iloc[::25, :].Date.values, rotation=45,  size = 4)     
ax.set_yticks(np.arange(0,data.columns[1:].shape[0]))
ax.set_yticklabels(data.columns[1:], rotation=0,  size = 4)     
plt.colorbar() 
plt.tight_layout()
plt.show()
fig.savefig('multivariate_timeseries_8hr.jpg', dpi=300)
plt.clf() 