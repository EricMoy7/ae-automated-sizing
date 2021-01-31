import xlwings as xw
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.colorbar
from matplotlib import ticker, cm

wb = xw.Book('AE442Sizing.xlsx')
sht = wb.sheets['Sheet1']

working_col = 'E'

Range = f'{working_col}2'
BFL = f'{working_col}3'

Range_Requirement = f'{working_col}5'
BFL_Requirement = f'{working_col}6'

Wing_Area = f'{working_col}9'
AR = f'{working_col}10'

#Guess
FN_Guess = f'{working_col}11'
W_Fuel_Guess = f'{working_col}12'
Delta_Weight_Guess = f'{working_col}13'

#Calculated Value
FN_Calc = f'{working_col}15'
W_Fuel_Calc = f'{working_col}16'
Delta_Weight_Calc = f'{working_col}17'

Range_Req = sht.range(Range_Requirement).value
BFL_Req = sht.range(BFL_Requirement).value

#Weight Interations

precision = 5
def Looper(var1, var2, r1, r2, r3, r4, v1, v2):
    EW = []
    WA = []
    AR = []

    for i in v1:
        sht.range(var1).value = i
        place_array = []
        for j in v2:
            sht.range(var2).value = j
            counter = 0
            while (round(Range_Req, precision) != round(sht.range(Range).value,precision) and round(BFL_Req, precision) != round(sht.range(BFL).value, precision)):
                FN = sht.range(FN_Calc).value
                W = sht.range(W_Fuel_Calc).value
                DW = sht.range(Delta_Weight_Calc).value

                sht.range(FN_Guess).value = FN
                sht.range(W_Fuel_Guess).value = W
                sht.range(Delta_Weight_Guess).value = DW
                if (counter > 1000):
                    sht.range(f'{working_col}29').value = 0
            WA.append(i)
            AR.append(j)
            place_array.append(sht.range(f'{working_col}29').value)
            counter += 1

        EW.append(place_array)

    return {'Empty Weight': EW, 'Wing Area': WA, 'Aspect Ratio': AR}

r1 = 200
r2 = 800
r3 = 3
r4 = 12

v1 = list(range(r3,r4))
v2 = list(range(r1,r2,50))

data = Looper(AR, Wing_Area, r1, r2, r3, r4, v1, v2)
array = np.array(data['Empty Weight'])
print(array)

# print(len(data['Wing Area']), len(data['Aspect Ratio']),data['Empty Weight'])

plt.contourf(np.linspace(r3,r4,len(v2)),np.linspace(r1,r2,len(v1)), array)
plt.colorbar()
plt.show()




