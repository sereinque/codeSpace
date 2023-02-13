import pandas as pd
import matplotlib.pyplot as plt

mary_count=[]
year=[]
inityear=1922
plt.ion()

while True:
    year.append(inityear)
    try:
        file="sourse/yob%d.txt" % inityear
        inityear+=1
        print(inityear)
        data=pd.read_csv(file,header=None)
    except:
        break
    try:
        mary_data=data[data[0]=='Mary']
        mary_count.append(mary_data.iloc[0,2]+mary_data.iloc[1,2])
        plt.plot(year,mary_count,color='r')
        plt.pause(0.01)
    except:
        pass
plt.savefig("Mary.png")
print("end")

    
    