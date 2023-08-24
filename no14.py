import pandas as pd

data={
    "cus_id":[1,2,3,4,5,6],
    "cus_name":["nithin","kishore","sai nithin","nithin sai","sai kishore","rocky"],
    "cus_age":[20,30,20,25,25,25]
    }

data1=pd.DataFrame(data)
group=data1.groupby('cus_age')['cus_id']
print(group.count())
