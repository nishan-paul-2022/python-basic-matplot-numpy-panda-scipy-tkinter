import pandas as pd
import numpy as np


def series():
        data = np.array(['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's'])
        idx = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
        ser = pd.Series(data, index=idx)
        print(ser, end='\n\n')
        print(ser[17], end='\n\n')
        print(ser.head(10), end='\n\n')
        print(ser.tail(n=10), end='\n\n')


def data_frame():
        lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']  # list of strings
        df = pd.DataFrame(lst)
        print(df, end='\n\n')

        data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
                'Age': [27, 24, 22, 32],
                'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
                'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

        df = pd.DataFrame(data)
        print(df, end='\n\n')
        print(df[['Name', 'Qualification']], end='\n\n')


def read_csv():
        data = pd.read_csv('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/pd1_data_frame.csv', index_col='Name')
        first = data.loc['Avery Bradley']
        second = data.loc['R.J. Hunter']
        third = data['Age']
        print(first, end='\n\n')
        print(second, end='\n\n')
        print(third, end='\n\n')


def read_csv_2():
        data = pd.read_csv('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/pd1_data_frame.csv', index_col="Name")
        row2 = data.iloc[3]
        row9 = data.iloc[10]
        print(row2, end='\n\n')
        print(row9, end='\n\n')


def missing_value():
        dict = {'First Score': [100, 90, np.nan, 95],
                'Second Score': [30, 45, 56, np.nan],
                'Third Score': [np.nan, 40, 80, 98]}

        df = pd.DataFrame(dict)
        print(df.isnull(), end='\n\n')
        print(df.fillna(0), end='\n\n')
        print(df.dropna(inplace=True), end='\n\n')


def traverse():
        dict = {'name': ["aparna", "pankaj", "sudhir", "Geeku"],
                'degree': ["MBA", "BCA", "M.Tech", "MBA"],
                'score': [90, 40, 80, 98]}

        df = pd.DataFrame(dict)
        for i, j in df.iterrows():
                print(i, j, end='\n\n')

        columns = list(df)
        for i in columns:
                print(df[i][2])


def save_data():
        # assigning three series to s1, s2, s3
        s1 = pd.Series([0, 4, 8])
        s2 = pd.Series([1, 5, 9])
        s3 = pd.Series([2, 6, 10])

        dframe = pd.DataFrame([s1, s2, s3])  # taking index and column values
        dframe.columns = ['Geeks', 'For', 'Geeks']  # assign column name

        # write data to csv E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter
        dframe.to_csv('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/csave1.csv', index=False)
        dframe.to_csv('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/csave2.csv', index=True)


def missing_data():
        dframe = pd.DataFrame({'Geeks': [23, 24, 22], 'For': [10, 12, np.nan], 'geeks': [0, np.nan, np.nan]}, columns=['Geeks', 'For', 'geeks'])

        # This will remove all the rows with NAN values | If axis is not defined then it is along rows / axis = 0
        dframe.dropna(inplace=True), print(dframe)
        dframe.dropna(axis=1, inplace=True), print(dframe)


def group_by():
        dframe = pd.DataFrame({'Geeks': [23, 24, 22], 'For': [10, 12, np.nan], 'geeks': [0, np.nan, np.nan]}, columns=['Geeks', 'For', 'geeks'])

        # Apply groupby and aggregate function |  max to find max value of column
        outcome = dframe.groupby(['Geeks']).max()
        print(outcome)


if __name__ == '__main__':
        series()
        read_csv()
        read_csv_2()
        missing_value()
        traverse()
        save_data()
        missing_data()
        group_by()

# https://www.geeksforgeeks.org/python-pandas-dataframe/
# https://www.geeksforgeeks.org/data-analysis-visualization-python-set-2/