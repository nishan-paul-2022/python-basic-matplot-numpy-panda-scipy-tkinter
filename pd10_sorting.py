import pandas as pd

data = pd.read_csv('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/pd1_data_frame.csv')
data.sort_values('Name', axis=0, ascending=True, inplace=True, na_position='last'), print(data)
data.sort_values('Salary', axis=0, ascending=True, inplace=True, na_position='first'), print(data)
data.sort_values(['Team', 'Name'], axis=0, ascending=True, inplace=True), print(data)
data.sort_values(['Team', 'Age', 'Height'], axis=0, ascending=[False, True, False], inplace=True), print(data)

# https://www.geeksforgeeks.org/python-pandas-dataframe-sort_values-set-1/
# https://www.geeksforgeeks.org/python-pandas-dataframe-sort_values-set-2/