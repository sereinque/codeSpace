import pandas as pd
data=pd.read_csv("./sourse/yob1922.txt",header=None)
mary_data=data[data[0]=='Mary']
print(mary_data)
print(mary_data.iloc[0,2]+mary_data.iloc[1,2])
