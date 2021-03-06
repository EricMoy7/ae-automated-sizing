#CSV Reader/Writer
import xlwings as xw

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.colorbar
from matplotlib import ticker, cm
from parfor import parfor


#File Inputs
file_name = 'AE442Sizing.xlsx'
sht_name = 'Sheet1'

wb = xw.Book(file_name)
sht = wb.sheets[sht_name]

#Set iteration column
iter_col = 'G'

#Requirements
Range_Requirement = f'{iter_col}5'
BFL_Requirement = f'{iter_col}6'

#Inputs
Wing_Area = f'{iter_col}9'
AR = f'{iter_col}10'

#Guess
FN_Guess = f'{iter_col}11'
W_Fuel_Guess = f'{iter_col}12'
Delta_Weight_Guess = f'{iter_col}13'

#Calculations
Range = f'{iter_col}2'
BFL = f'{iter_col}3'

FN_Calc = f'{iter_col}15'
W_Fuel_Calc = f'{iter_col}16'
Delta_Weight_Calc = f'{iter_col}17'
TW = f'{iter_col}18'

Empty_Weight = f'{iter_col}29'
LFL = f'{iter_col}206'
Wing_Loading = f'{iter_col}188'
Ramp_Weight = f'{iter_col}20'
Fuel_Weight = f'{iter_col}16'


#Set while loop precision
pres = 5

def Looper(x_var, y_var, r1, r2, r3, r4, v1, v2, z_var, constraint, constraint_value):
    data_array = []

    EW, RW, FW = z_var

    data1 = open('Empty_Weight_Main', 'w')
    data2 = open('Ramp_Weight_Main', 'w')
    data3 = open('Fuel_Weight_Main', 'w')

    if (not constraint):
        for i in v1:
            sht.range(x_var).value = i
            row_array = []
            for j in v2:
                sht.range(y_var).value = j
                counter = 0
                broken = False
                while (round(sht.range(Range_Requirement).value, pres) != round(sht.range(Range).value) and round(sht.range(BFL_Requirement).value, pres) != round(sht.range(BFL).value, pres)):
                    FN = sht.range(FN_Calc).value
                    W = sht.range(W_Fuel_Calc).value
                    DW = sht.range(Delta_Weight_Calc).value

                    sht.range(FN_Guess).value = FN
                    sht.range(W_Fuel_Guess).value = W
                    sht.range(Delta_Weight_Guess).value = DW

                    if ( counter > 1000):
                        broken = True
                        break
                    counter += 1

                if (broken):
                    data1.write(f'{i},{j},NaN\n')
                    data2.write(f'{i},{j},NaN\n')
                    data3.write(f'{i},{j},NaN\n')
                else:
                    data1.write(f'{i},{j},{sht.range(EW).value}\n')
                    data2.write(f'{i},{j},{sht.range(RW).value}\n')
                    data3.write(f'{i},{j},{sht.range(FW).value}\n')
                
                sht.range(FN_Guess).value = 10000
                sht.range(W_Fuel_Guess).value = 1000
                sht.range(Delta_Weight_Guess).value = 100

                row_array.append(sht.range(EW).value)
            data_array.append(row_array)

        return data_array

r1 = 300
r2 = 1000
r3 = 2
r4 = 8

# v1 = np.arange(r3,r4,1)
# v2 = np.arange(r1,r2,50)

v1 = np.linspace(r3,r4,15)
v2 = np.linspace(r1,r2,15)

data = Looper(AR, Wing_Area, r1, r2, r3, r4, v1, v2, z_var = (Empty_Weight, Ramp_Weight, Fuel_Weight), constraint = None, constraint_value = None)

# array = np.array(data)
# plt.contourf(np.linspace(r3,r4,len(v2)),np.linspace(r1,r2,len(v1)), np.flip(array), 30)

# cbar = plt.colorbar()
# plt.show()
