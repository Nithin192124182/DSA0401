import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
a={'age':[23,23,27,27,39,41,47,49],
    '%fat':[9.5,26.5,7.8,17.8,31.4,25.9,27.4,27.2]}
b=pd.DataFrame(a)
print(b)
c=b['age'].mean()
print("MEAN OF AGE=",c)
d=b['%fat'].mean()
print("MEAN OF %FAT=",d)
print("MEDIAN OF AGE=",b['age'].median())
print("MEDIAN OF %FAT=",b['%fat'].median())
print("SD OF AGE=",b['age'].std())
print("SD OF %FAT=",b['%fat'].std())
b.plot(kind="box",x="age",y="%fat",color="blue")
plt.show()
b.plot(kind="scatter",x="age",y="%fat",color="cyan")
plt.grid()
plt.show()
