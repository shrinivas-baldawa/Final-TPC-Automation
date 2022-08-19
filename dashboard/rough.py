import pandas as pd
df = pd.read_excel('media/Students.xlsx')
lst = []

for i in range(len(df)):
    lst.append(df.iloc[i])

for column in lst:
    print(column[3])