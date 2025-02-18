import pandas as pd

data = pd.read_csv("HousePointsList2025.csv", header=None) #not all the columns have categories

#print(data)
Name = []
House = []
Points = []
Level = []
Email = []


for x, row in data.iterrows():
    Name.append(data[0][x])
    House.append(data[1][x])
    Points.append(data[2][x])    
    Level.append(data[3][x])    
    Email.append(data[4][x])
    
for x in Name:
    if not isinstance(x, str):
        print('f')