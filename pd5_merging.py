import pandas as pd


data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

data2 = {'Name': ['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'],
         'Age': [17, 14, 12, 52],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']}

df = pd.DataFrame(data1, index=[0, 1, 2, 3])
df1 = pd.DataFrame(data2, index=[4, 5, 6, 7])
result = pd.concat([df, df1])
print(result, end='\n\n')

df = pd.DataFrame(data1, index=[0, 1, 2, 3])
df1 = pd.DataFrame(data2, index=[2, 3, 6, 7])

result1 = df.append(df1)
result2 = pd.concat([df, df1], ignore_index=True)
result3 = pd.concat([df, df1], keys=['x', 'y'])
result4 = pd.concat([df, df1], axis=1, join='inner')
result5 = pd.concat([df, df1], axis=1, sort=False)

print('df.append(pd3_df1.csv)\n', result1, end='\n\n')
print('pd.concat([df, pd3_df1.csv], ignore_index=True)\n', result2, end='\n\n')
print('pd.concat([df, pd3_df1.csv], keys=["x", "y"])\n', result3, end='\n\n')
print('pd.concat([df, pd3_df1.csv], axis=1, join="inner")\n', result4, end='\n\n')
print('pd.concat([df, pd3_df1.csv], axis=1, sort=False)\n', result5, end='\n\n')


# https://www.geeksforgeeks.org/python-pandas-merging-joining-and-concatenating/