import pandas as pd

df=pd.read_csv("../Dataset/SalesTransactions.csv",
               encoding='utf-8', dtype='unicode',
               low_memory=False)
print(df)