import pandas as pd
from text import encode
import matplotlib.pyplot as plt

bad = pd.read_excel('./dataset/badword.xlsx', encoding='utf-8-sig')
good = pd.read_excel('./dataset/goodword.xlsx', encoding='utf-8-sig')

print(len(bad), len(good))

df = pd.concat([bad, good])
print(len(df))

df.dropna(how='any', inplace=True)
print(len(df))


for i in range(len(df)):
    d = df.iloc[i]
    df.iloc[i] = [encode(d[0]) , d[1]]

df['length'] = [len(df.iloc[i][0]) for i in range(len(df))]
print(df.head())

plt.hist(df['length'], bins=df['length'].max())
plt.show()