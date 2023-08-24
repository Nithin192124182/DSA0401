import pandas as pd

data={
    "user_id":[1,2,3,4,5,6],
    "user_review":["good","bad","not bad","poor","nice","excellent"],
    "frequency":["good","Excellent","nice","worst","poor","worst"]
    }

data1=pd.DataFrame(data)
group=data1.groupby('frequency')['user_review']
print(group.count())
