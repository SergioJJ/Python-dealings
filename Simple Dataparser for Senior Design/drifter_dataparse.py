## -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:45:41 2020

@author: sergi
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


TEMP_MAX = 120 #120 degrees F
TDS_MAX = 1200
SAL_SCALE = 1.0 # sal values from 0 to 1
COND_MAX = 1200 #200000 is the max for conductivity reading
BATT_MAX = 4.3 # this value is dependenta on battery setup, showing overvoltage
BATT_MIN = 3.0
#DATA = open(r"C:\Users\sergi\Documents\A.NOTES\Senior Design\Deployment\2nd attempt\first week\DATA_03212020") 
DATA = pd.read_csv("DATA.csv",dtype = np.float64, usecols = [1,2,3,4,5,6])
TIMEINDEX = pd.read_csv("DATA.csv",dtype = str,  usecols = [0])


PLOT_SIZE = (30,5)
DPI = 300 #plot quality dots per inch


fig1 = plt.figure(figsize = PLOT_SIZE)
fig1.suptitle('Temp Sensors INT and EXT ',)
plt.plot(TIMEINDEX.TIME, DATA.EXT)
plt.plot(TIMEINDEX.TIME, DATA.INT)
plt.xlabel('Date-Time')
plt.ylabel('Temperature F')
plt.legend(['Blue - Ext, Orange - Int'])
plt.xticks(rotation = 90)
plt.ylim(0, TEMP_MAX)  # sets from 0F to 120F, may need to increase
plt.savefig('files/TEMPs.png', dpi = DPI)
plt.show()


fig2 = plt.figure(figsize = PLOT_SIZE)
fig2.suptitle('Total Dissolved Solids')
plt.plot(TIMEINDEX.TIME,DATA.TDS)  ##unit 2 - 100000 ppm
plt.xlabel('Date-Time')
plt.ylabel('TDS ppm')
plt.xticks(rotation = 90)
plt.ylim(0, TDS_MAX) #100000 ) #is the total range of TDS measurement
plt.savefig('files/TDS.png', dpi = DPI)
plt.show()


fig3 = plt.figure(figsize = PLOT_SIZE)
fig3.suptitle('Salinity')
plt.plot(TIMEINDEX.TIME,DATA.SAL)
plt.xticks(rotation = 90)
plt.xlabel('Date-Time')
plt.ylabel('TDS ppm')
plt.ylim(0, SAL_SCALE)
plt.savefig('files/SAL.png', dpi = DPI)
plt.show()


fig4 = plt.figure(figsize = PLOT_SIZE)
fig4.suptitle('Conductivity')
plt.plot(TIMEINDEX.TIME, DATA.COND)  ## unit 5 uS/cm - 200,000 uS    micro Siemen
plt.xticks(rotation = 90)
plt.xlabel('Date-Time')
plt.ylabel('Conductivity microS')
plt.ylim(0, COND_MAX) #200000 ) # is max limit of K1 range
plt.savefig('files/COND.png', dpi = DPI)
plt.show()



fig5 = plt.figure(figsize = PLOT_SIZE)
fig5.suptitle('Main battery volatge')
plt.plot(TIMEINDEX.TIME,DATA.BATT) #one graph
plt.xticks(rotation = 90)
plt.xlabel('Date-Time')
plt.ylabel('BATT VOLT *BATT %WIP*')
plt.ylim(BATT_MIN, BATT_MAX)   #####try to get battery voltage as this is not useful
plt.savefig('files/BATT.png', dpi = DPI)
plt.show()
