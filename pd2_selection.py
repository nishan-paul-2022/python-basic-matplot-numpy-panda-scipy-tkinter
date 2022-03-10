import pandas as pd


def fst():
    data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
            'Age': [27, 24, 22, 32],
            'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
            'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

    df = pd.DataFrame(data)
    print(df[['Name', 'Qualification']], end='\n\n')


def sec():
    data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
            'Height': [5.1, 6.2, 5.1, 5.2],
            'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}

    df = pd.DataFrame(data)
    address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']
    df['Address'] = address
    print(df, end='\n\n')


def thrd():
    data = pd.read_csv('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/pd1_data_frame.csv', index_col='Name')
    first = data.loc['Avery Bradley']
    second = data.loc['R.J. Hunter']
    print(first, end='\n\n')
    print(second, end='\n\n')


def frth():
    df = pd.read_csv('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/pd1_data_frame.csv', index_col="Name")
    new_row = pd.DataFrame({'Name': 'new_row', 'Team': 'Boston', 'Number': 3, 'Position': 'PG',
                            'Age': 33, 'Height': '6-2', 'Weight': 189, 'College': 'MIT', 'Salary': 99999},
                            index=[0])
    df = pd.concat([new_row, df]).reset_index(drop=True)
    print(df.head(5), end='\n\n')


def fifth():
    data = pd.read_csv('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/pd1_data_frame.csv', index_col='Name')
    data.drop(['Avery Bradley', 'John Holland', 'R.J. Hunter', 'R.J. Hunter'], inplace=True)
    print(data, end='\n\n')


fst()
sec()
thrd()
frth()
fifth()

# https://www.geeksforgeeks.org/dealing-with-rows-and-columns-in-pandas-dataframe/