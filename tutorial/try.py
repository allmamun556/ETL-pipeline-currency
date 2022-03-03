data={'EquipmentHeader': {'OEMName': 'JOHN DEERE', 'Model': '5080R', 'EquipmentID': '5080R', 'SerialNumber': 'L05080R570753', 'PIN': 'L05080R570753'}, 
'Location': {'Latitude': '49.539944', 'Longitude': '7.881778'}, 'CumulativeIdleHours': {'Hour': '91.03'}, 
'CumulativeOperatingHours': {'Hour': '2556.25'}, 
'DEFRemaining': {'Percent': '34.00'}, 'FuelRemaining': {'Percent': '87.20'}}







#print(data.keys())


from unicodedata import name
from matplotlib.pyplot import axis
import pandas as pd
list1=[]
for i in data.keys():
 list1.append(i)

df = pd.Series(list1, name=)

print(pd.DataFrame(df))


#print(data.values())


list2=[]
for i in data.values():
 list2.append(i)



df2 = pd.Series(list2)
print(pd.DataFrame(df2))





