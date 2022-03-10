import pandas as pd


def string():
    data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
            'Age': [27, 24, 22, 32],
            'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
            'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

    df = pd.DataFrame(data)
    df['Name'] = df['Name'].str.lower()
    print(df, end='\n\n')

    df['Address'] = df['Address'].str.upper()
    print(df, end='\n\n')


def replacing_1():
    data = pd.read_csv('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/pd1_data_frame.csv')
    data['Age'] = data['Age'].replace(25.0, "Twenty five")
    filter = data['Age'] == 'Twenty five'  # creating a filter for age column where age = 'Twenty five'
    outcome = data.where(filter).dropna()
    print(outcome, end='\n\n')


def replacing_2():
    data = pd.read_csv('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/pd1_data_frame.csv')
    data['Team'] = data['Team'].str.replace('boston', 'New Boston', case=False)
    filter = data["Team"] == "New Boston Celtics"
    outcome = data.where(filter).dropna()
    print(outcome, end='\n\n')


def concat():
    data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
            'Age': [27, 24, 22, 32],
            'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
            'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

    df = pd.DataFrame(data)
    new = df['Address'].copy()
    df['Name'] = df['Name'].str.cat(new, sep=', ')  # concatenating address with name column and overwriting name column
    print(df)


if __name__ == '__main__':
    string()
    replacing_1()
    replacing_2()
    concat()